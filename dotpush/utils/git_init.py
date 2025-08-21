import os
import keyring
from .git_env import _env


def _git_init(username: str = os.environ.get("USER")):
    """
    This helper initializes the GitHub repository for DotPush backup directory.

    Args:
        username (str): The system username.
    """
    if _env():
        token = keyring.get_password("dotpush", "github_token")
        print(token)

    # get token
    # get repository
    # initialize repository
    # store username and repo name in config.ini
