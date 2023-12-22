Import("env")

try:
    import subprocess
    import os
except ImportError:
    env.Execute("$PYTHONEXE -m pip install subprocess")
    env.Execute("$PYTHONEXE -m pip install os")

print("Embed Git Info Script has started")

def get_git_info():
    # Dictionary of git commands to extract various information
    commands = {
        'tag': "git describe --tags --always",
        'branch': "git rev-parse --abbrev-ref HEAD",
        'commit_hash': "git rev-parse HEAD",
        'date': "git log -1 --format=%cd",
        'author': "git log -1 --format=%cn",
        'author_email': "git log -1 --format=%ce",
        'repo_url': "git config --get remote.origin.url",
        'repo_name': os.path.basename(os.getcwd()),
    }

    info = {}
    for key, command in commands.items():
        try:
            if key == 'repo_name':
                result = commands[key]
            else:
                result = subprocess.check_output(command, shell=True).decode().strip()
            info[key] = result
        except subprocess.CalledProcessError:
            info[key] = "Unknown"

    return info

def write_header(info):
    header_path = os.path.join(env['PROJECT_DIR'], 'include', 'git_info.h')
    with open(header_path, 'w') as f:
        for key, value in info.items():
            f.write(f"#define GIT_{key.upper()} \"{value}\"\n")

try:
    git_info = get_git_info()
    write_header(git_info)
except Exception as e:
    print(f"An error occurred: {e}")

print("Embed Git Info Script has finished")