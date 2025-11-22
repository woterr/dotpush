import getpass
import keyring
from .git_validity import _is_valid
from keyring.errors import NoKeyringError


def _env() -> tuple[bool, str | None]:
    """
    Stores the user token safely in Linux Secret Service.

    Returns:
        Tuple[bool, str]:
            bool: True if token was saved successfully. False otherwise.
            git_repository (str | None): The GitHub repository name.
    """
    print("\nPlease provide a GitHub Personal Access Token.")
    print("Go to https://github.com/settings/tokens/new to create one.")
    print("The token needs the 'repo' scope.")

    while True:
        try:
            token = getpass.getpass("Paste your token and press Enter: ")
            git_repository = input(
                "Enter the GitHub repository name to which DotFiles are to be saved (eg. 'mydotfiles'): "
            )

            if not token:
                print("\nNo token provided. Aborting.")
                return (False, git_repository)

            print("    -> Validating token with GitHub...")

            if _is_valid(token):
                try:
                    keyring.set_password("dotpush", "github_token", token)
                    return True
                except NoKeyringError:
                    print("\n[!] No secret storage backend available.")
                    print(
                        "    Install on Arch:\n"
                        "    sudo pacman -S libsecret gnome-keyring\n"
                    )
                    print("    Or: pip install keyrings.alt  # insecure fallback\n")
                    return False
                print("\nToken saved securely Linux Secret Service.")
                return (True, git_repository)
            else:
                print("\nThe token provided is invalid or expired. Please try again.")

        except (KeyboardInterrupt, EOFError):
            print("\nToken entry cancelled.")
            return (False, None)

        except Exception as e:
            print(f"\nAn error occurred while saving the token: {e}")
            return (False, None)
