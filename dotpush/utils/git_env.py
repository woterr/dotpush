import getpass
import keyring
from .git_validity import _is_valid


def _env() -> bool:
    """
    Stores the user token safely in Linux Secret Service.

    Returns:
        bool: True if keyring was successfull. False otherwise.
    """
    print("\nPlease provide a GitHub Personal Access Token.")
    print("Go to https://github.com/settings/tokens/new to create one.")
    print("The token needs the 'repo' scope.")

    while True:
        try:
            token = getpass.getpass("Paste your token and press Enter: ")

            if not token:
                print("nNo token provided. Aborting.")
                return False

            print("  -> Validating token with GitHub...")

            if _is_valid(token):
                keyring.set_password("dotpush", "github_token", token)
                print("\nToken saved securely Linux Secret Service.")
                return True
            else:
                print("\nThe token provided is invalid or expired. Please try again.")

        except (KeyboardInterrupt, EOFError):
            print("\n\nToken entry cancelled.")
            return False

        except Exception as e:
            print(f"\nAn error occurred while saving the token: {e}")
            return False
