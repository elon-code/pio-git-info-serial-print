# https://bitbucket.org/exploratorium/pio-git-info-serial-print/src/main/

# Importing the environment from PlatformIO and necessary modules
Import("env")

import subprocess
import os
import zlib  # For CRC calculation
import datetime

print("Embed Git Info Script has started")

# Function to gather git, system, and build information
def get_git_info():
    # Commands to extract various information
    commands = { # Comment out undesirable variables to save on storage
        'git_tag': "git describe --tags --always",
        'git_branch': "git rev-parse --abbrev-ref HEAD",
        'git_commit_hash': "git rev-parse HEAD",
        # 'git_date': "git log -1 --format=%cd", # I believe build date is better then git date. Git date can be found with commit hash
        # 'git_author': "git log -1 --format=%cn", # These are optional variables, they are not really necessary in printout
        # 'git_author_email': "git log -1 --format=%ce", # These are optional variables, they are not really necessary in printout
        'git_repo_url': "git config --get remote.origin.url",
        'local_user_name': "git config user.name",
        'local_user_email': "git config user.email",
        # 'folder_name': os.path.basename(os.getcwd()), # I feel git repo name is better, but may choose otherwise
        # 'computer_user': os.getlogin(), # I feel git user is better, but you may choose computer username
        # Adding build date and time
        'build_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # date of build
    }

    # Executing commands and collecting results
    info = {}
    for key, command in commands.items():
        try:
            if key in ['build_date', 'build_time', 'folder_name']:
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
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            return zlib.crc32(data)
    except Exception as e:
        return f"Error calculating CRC: {e}"

# Function to write the gathered information into a header file
def write_header(info, crc):
    header_path = os.path.join(env['PROJECT_DIR'], 'include', 'git_info.h')
    with open(header_path, 'w') as f:
        for key, value in info.items():
            # Writing each piece of information as a macro definition
            f.write(f"#define {key.upper()} \"{value}\"\n")
        # Writing CRC information
        f.write(f"#define MAIN_FILE_CRC {crc}\n")


# Main execution block
try:
    git_info = get_git_info()
    # Replace with the actual path to your main file
    main_file_crc = calculate_crc('src/main.cpp')  
    write_header(git_info, main_file_crc)
except Exception as e:
    print(f"An error occurred: {e}")

print("Embed Git Info Script has finished")
