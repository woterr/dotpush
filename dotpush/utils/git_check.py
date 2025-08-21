import os


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
