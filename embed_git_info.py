import subprocess

def get_git_info():
    commands = {
        'tag': "git describe --tags",
        'branch': "git rev-parse --abbrev-ref HEAD",
        'commit_hash': "git rev-parse HEAD",
        'date': "git log -1 --format=%cd",
        'author': "git log -1 --format=%cn",
        'author_email': "git log -1 --format=%ce",
        'repo_url': "git config --get remote.origin.url",
        'repo_name': "basename `git rev-parse --show-toplevel`"
    }

    info = {}
    for key, command in commands.items():
        try:
            result = subprocess.check_output(command, shell=True).decode().strip()
            info[key] = result
        except subprocess.CalledProcessError:
            info[key] = "Unknown"

    return info

def write_header(info):
    with open('git_info.h', 'w') as f:
        for key, value in info.items():
            f.write(f"#define GIT_{key.upper()} \"{value}\"\n")

if __name__ == "__main__":
    git_info = get_git_info()
    write_header(git_info)
