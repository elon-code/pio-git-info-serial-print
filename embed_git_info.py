import subprocess
import os

print("Embed Git Info Script has started")

try:
    def get_git_info():
        # Dictionary of git commands to extract various information
        commands = {
            'tag': "git describe --tags --always",  # Gets the latest tag
            'branch': "git rev-parse --abbrev-ref HEAD",  # Gets the current branch name
            'commit_hash': "git rev-parse HEAD",  # Gets the current commit hash
            'date': "git log -1 --format=%cd",  # Gets the date of the last commit
            'author': "git log -1 --format=%cn",  # Gets the author of the last commit
            'author_email': "git log -1 --format=%ce",  # Gets the email of the last commit author
            'repo_url': "git config --get remote.origin.url",  # Gets the repository URL
            'repo_name': os.path.basename(os.getcwd()),  # Gets the repository name using Python's os module
        }

        info = {}
        for key, command in commands.items():
            try:
                # Execute the command and store the result
                if key == 'repo_name':
                    result = commands[key]  # repo_name is already determined
                else:
                    result = subprocess.check_output(command, shell=True).decode().strip()
                info[key] = result
            except subprocess.CalledProcessError:
                # In case of an error, set the value to "Unknown"
                info[key] = "Unknown"

        return info

    def write_header(info):
        # Define the path to the header file using cross-platform path handling
        header_path = os.path.join('include', 'git_info.h')
        with open(header_path, 'w') as f:
            # Write the git information as preprocessor directives
            for key, value in info.items():
                f.write(f"#define GIT_{key.upper()} \"{value}\"\n")

    if __name__ == "__main__":
        # Main execution: Get git info and write to the header file
        git_info = get_git_info()
        write_header(git_info)

except Exception as e:
    # Catch and print any exceptions that occur
    print(f"An error occurred: {e}")

print("Embed Git Info Script has finished")
