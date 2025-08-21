import os
import keyring
import requests


def _check(path: str) -> bool:
    """
    This helper checks if a repository is initialized at the given path.

    Args:
        path (str): The path to the directory (backup directory) to check.

    Returns:
        bool: True if it's a Git repository, False otherwise.
    """

    git_path = os.path.join(path, ".git")

    return os.path.isdir(git_path)


def _check_remote_repo(username: str, repo_name: str) -> bool:
    """
    This helper checks if the initialized repository is valid.

    Args:
        username (str): User's GitHub username.
        repo_name (str): Repository name.

    Returns:
        bool: True if repository exists. False otherwise.
    """
    token = keyring.get_password("dotpush", "github_token")
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)
    return response.status_code == 200
