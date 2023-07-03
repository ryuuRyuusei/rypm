"""Common functions for rypm."""

def confirm(message: str, default: bool | None = False):
    """Prompt for user confirmation."""
    valid = {"yes": True, "y": True, "no": False, "n": False}
    prompt = " [Y/n] " if default else " [y/N] "
    while True:
        choice = input(message + prompt).lower()
        if choice == "" and default is not None:
            return default
        if choice in valid:
            return valid[choice]
        print("Please respond with 'yes' or 'no' (or 'y' or 'n').")


__all__ = ["confirm"]
