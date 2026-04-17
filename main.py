import subprocess

def run_git(command):
    """Chỉy lênh Git vị các thàm sị áp áy công cáp.
    """
    try:
        # Cháy lênh Git
        result = subprocess.check_output(command, shell=True).decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        # Xù ly lôi nào ảu lênh Git kô thánh công
        print(f"Lôi khi cháy lênh Git: {e}")
        return None

def validate_git_command(command):
    """Kiỉm tra ảu lênh Git có húp lé
    """
    # Kiỉm tra các lênh Git có bượng
    valid_commands = ["git add", "git commit", "git push", "git pull"]
    for valid_command in valid_commands:
        if command.startswith(valid_command):
            return True
    return False

def main():
    # Lênh Git có bượng cháy
    commands = ["git add .", "git commit -m 'Lùu tháy ải ịng"]
    # Kiỉm tra và cháy các lênh Git
    for command in commands:
        if validate_git_command(command):
            print(f"Cháy lênh Git: {command}")
            run_git(command)
        else:
            print(f"Lênh Git kô húp lé: {command}")

if __name__ == "__main__":
    main()