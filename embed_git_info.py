# https://bitbucket.org/exploratorium/pio-git-info-serial-print

# Importing the environment from PlatformIO and necessary modules
Import("env")

import subprocess # For executing shell commands
import os      # For file path operations
import zlib  # For CRC calculation
import datetime # For build date/time

# Configuration flag for PROGMEM
USE_PROGMEM = False # Set to True if the target architecture is AVR
USE_CRC = False # Set to True to calculate the CRC of the main file

print("Embed Git Info Script has started")

# Function to gather git, system, and build information
def get_git_info():
    # Commands to extract various information
    commands = { # Comment out undesirable variables to save on storage
        'git_tag': "git describe --tags --always",
        'git_branch': "git rev-parse --abbrev-ref HEAD",
        'git_commit_hash': "git rev-parse HEAD",
        # 'git_date': "git log -1 --format=%cd", # I believe build date is better then git date. Git date can be found with commit hash
        'git_repo_url': "git config --get remote.origin.url",
        'git_user_name': "git config user.name",
        'git_user_email': "git config user.email",
        # 'folder_name': os.path.basename(os.getcwd()), # I feel git repo name is better, but may choose otherwise
        # 'computer_user': os.getlogin(), # I feel git user is better, but you may choose computer username
        'build_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # date of build
    }

    # Executing commands and collecting results
    info = {}
    for key, command in commands.items():
        try:
            if key in ['build_date', 'folder_name', 'computer_user']:
                # Directly using values for certain keys
                result = commands[key]
            else:
                # Executing shell commands for Git information
                result = subprocess.check_output(command, shell=True).decode().strip()
            info[key] = result
        except subprocess.CalledProcessError:
            # Handling command execution errors
            info[key] = "Unknown"

    return info

# Function to calculate the CRC of a given file
def calculate_crc(filename):
    if not USE_CRC: # If CRC is not desired,
        return None
    try: # Try to calculate the CRC when CRC is desired
        with open(filename, 'rb') as file: # Open the file in read mode
            data = file.read() # Read the file
            return zlib.crc32(data) # Calculate the CRC
    except Exception as e: # If an error occurs, print an error message
        return f"Error calculating CRC: {e}"


# Function to write the Git information and CRC to a header file
def write_header(info, crc):
    # Construct the path to the header file
    header_path = os.path.join(env['PROJECT_DIR'], 'include', 'git_info.h')

    # Open the header file in write mode
    with open(header_path, 'w') as f:
        if USE_PROGMEM:
            # If the target architecture is AVR
            f.write("#ifdef __AVR__\n")
            # Include the pgmspace.h library for PROGMEM
            f.write("#include <avr/pgmspace.h>\n")
            # Iterate over the Git information
            for key, value in info.items():
                # Write each piece of information as a const variable in PROGMEM
                f.write(f"const char {key.upper()}[] PROGMEM = \"{value}\";\n")
            # Write the CRC information in PROGMEM
            f.write(f"const long MAIN_FILE_CRC PROGMEM = {crc};\n")
            f.write("#else\n")
        # Iterate over the Git information
        for key, value in info.items():
            # Write each piece of information as a const variable
            f.write(f"const char {key.upper()}[] = \"{value}\";\n")
        # Write the CRC information
        if USE_CRC:
            f.write(f"const long MAIN_FILE_CRC = {crc};\n")
        if USE_PROGMEM:
            # End of conditional compilation
            f.write("#endif\n")

    # Add the path of the header file to the .gitignore file
    add_to_gitignore(header_path)

# Function to add a file path to the .gitignore file
def add_to_gitignore(file_path):
    # Convert the absolute path to a relative path
    relative_path = os.path.relpath(file_path)
    # Replace backslashes with forward slashes (so that )
    relative_path = relative_path.replace("\\", "/")

    # Check if the .gitignore file exists
    if os.path.exists('.gitignore'):
        # Open the .gitignore file in read and write mode
        with open('.gitignore', 'r+') as f:
            # Read the contents of the .gitignore file
            lines = f.read()
            # Check if the relative path is already in the .gitignore file
            if relative_path not in lines:
                # If it isn't, append it to a new line at the end of the file
                f.write(f'\n{relative_path}')
                # Print a message indicating that the file path was added
                print(f"Added {relative_path} to .gitignore. You may need to use command 'git rm --cached {relative_path}' to remove it from the repository.")
    else:
        # If the .gitignore file doesn't exist, print an error message
        print("Error: .gitignore file does not exist.")

# Main execution block
try:
    git_info = get_git_info()
    # Replace with the actual path to your main file
    main_file_crc = calculate_crc('src/main.cpp')  
    write_header(git_info, main_file_crc)
except Exception as e:
    print(f"An error occurred: {e}")

print("Embed Git Info Script has finished")
