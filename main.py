def greet_ai_repo(name: str = "AI Repo") -> None:
    """Prints a greeting message to the console."""
    print(f"Hello, {name}!")

def main() -> None:
    """Runs the main program."""
    greet_ai_repo()
    greet_ai_repo("Custom Name")

if __name__ == "__main__":
    main()