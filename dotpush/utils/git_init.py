import os
import keyring
import requests
from .git_env import _env
from .git_check import _check_remote_repo
from .config import _get_config
from .. import constants


def _get_username_from_token(token: str) -> str | None:
    """
    This helper fetches the GitHub username which the
    PAT corresponds to.

    Args:
        token (str): GitHub PAT.

    Returns:
        username (str): Returns GitHub account username.
    """
    username_url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}

    try:
        response = requests.get(username_url, headers=headers)
        if response.status_code == 200:
            return response.json().get("login")
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def _create_remote_repository(
    repo_name: str, token: str, git_username: str, is_private: bool
) -> bool:
    """
    This helper creates a remote repository on GitHub.

    Args:
        repo_name (str): The repository name where DotFiles
                        will be pushed to.
        token (str): GitHub PAT.
        git_username (str): GitHub account username.
        is_private (bool): If the repository is private or not.

    Returns:
        bool: True if initialization was successfull. False otherwise.
    """

    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    data = {
        "name": repo_name,
        "private": is_private,
    }

    print(f"    -> Creating new private repository '{repo_name}' on GitHub...")
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(
            f"    -> Repository created successfully. https://github.com/{git_username}/{repo_name}/"
        )
        return True
    else:
        print("    -> Error: Failed to create repository.")
        print(f"    -> Response: {response.json()}")
        return False


def _git_init() -> bool:
    """
    This helper initializes the GitHub repository for DotPush backup directory.

    Args:
        git_username (str): GitHub account username.

    Returns:
        bool: True if initialization was successfull. False otherwise.
    """
    config = _get_config()
    if config.has_section("GitHub") and config.getboolean(
        "GitHub", "enabled", fallback=False
    ):
        print("GitHub integration is already enabled.")
        return

    print("    -> Enabling GitHub integration.")

    git_repo = _env()[1]
    token = keyring.get_password("dotpush", "github_token")

    if not token:
        print(
            "    -> Token not found. Please run 'dotpush init github' and provide one."
        )
        return False

    git_username = _get_username_from_token(token)
    if not git_username:
        print(
            "    -> Could not fetch username. The token is likely invalid or expired."
        )
        return False

    config_path = os.path.expanduser(constants.CONFIG_PATH)

    config.set("GitHub", "enabled", "True")
    config.set("GitHub", "username", git_username)
    config.set(
        "GitHub", "repository_url", f"https://github.com/{git_username}/{git_repo}"
    )

    with open(config_path, "w") as configfile:
        config.write(configfile)
    print("    -> Configuration saved.")

    if not _check_remote_repo(username=git_username, repo_name=git_repo):
        is_private = _get_config().getboolean("GitHub", "private", fallback=True)

        _create_remote_repository(
            repo_name=git_repo,
            token=token,
            git_username=git_username,
            is_private=is_private,
        )
        return True
    else:
        print("    -> Found existing repository on GitHub.")
        return True

    # get token
    # get repository
    # initialize repository
    # store username and repo name in config.ini
