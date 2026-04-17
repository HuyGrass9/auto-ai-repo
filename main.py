import subprocess
import argparse

def run_git(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error running Git command: {e}")
        return None

def validate_git_command(command):
    if not isinstance(command, str):
        raise ValueError("Command must be a string")
    valid_commands = ["git add", "git commit", "git push", "git pull"]
    for valid_command in valid_commands:
        if command.startswith(valid_command) and command.split()[0] == valid_command:
            return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Run a Git command")
    parser.add_argument("command", help="Git command to run")
    args = parser.parse_args()

    if validate_git_command(args.command):
        print(f"Running Git command: {args.command}")
        result = run_git(args.command)
        if result:
            print(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()