# https://bitbucket.org/exploratorium/pio-git-info-serial-print

# Importing the environment from PlatformIO and necessary modules
Import("env")

import subprocess # For executing shell commands
import os      # For file path operations
import zlib  # For CRC calculation
import datetime # For build date/time

# Set to True to calculate the CRC of the main file and print it to the serial monitor
# The rest of the commands can be enabled/disabled in the get_git_info() function
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
    header_file_name = 'git_info.h'
    header_path = os.path.join("$PROGPATH",'include', header_file_name)
    # Construct the guard ID for the header file
    guard_id = header_file_name.replace('.', '_').upper()
    # Open the header file in write mode
    try:
        with open(header_path, 'w') as f:
            # Write the header guard
            f.write(f"#ifndef {guard_id}\n")
            f.write(f"#define {guard_id}\n")
            # Iterate over the Git information
            for key, value in info.items():
                # Write each piece of information as a const variable
                f.write(f"const char {key.upper()}[] = \"{value}\";\n")
            # Write the CRC information
            if USE_CRC:
                f.write(f"const long MAIN_FILE_CRC = {crc};\n")
            # End of header guard
            f.write(f"#endif // {guard_id}\n")
    except FileNotFoundError:
        print(f"Could not find the header file: {header_path}")
    except PermissionError:
        print(f"Error")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution block
try:
    git_info = get_git_info()
    # Replace with the actual path to your main file
    main_file_crc = calculate_crc('src/main.cpp')  
    write_header(git_info, main_file_crc)
except Exception as e:
    print(f"An error occurred: {e}")

print("Embed Git Info Script has finished")
