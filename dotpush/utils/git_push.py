import keyring
import subprocess
import os
from datetime import datetime
from .git_check import _check
from .config import _get_config


def _initialize_git_repo(
    username: str, repo_name: str, token: str, directory: str
) -> bool:
    """
    This helper initializes a repo and pushes to a new remote on GitHub for the first time.
    NOTE: This is different from /git_init.py

    Args:
        username (str): The user's GitHub username.
        repo_name (str): The name of the repository on GitHub.
        token (str): The user's PAT for authentication.
        backup_dir (str): The path to the local backup directory.

    Returns:
        bool: True if everything was successfull.
    """
    print("-> Initializing new Git repository...")

    try:
        # Command: git init
        subprocess.run(["git", "init"], cwd=directory, check=True, capture_output=True)

        # git branch -M main
        subprocess.run(
            ["git", "branch", "-M", "main"],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        # Command: git add .
        subprocess.run(
            ["git", "add", "."], cwd=directory, check=True, capture_output=True
        )

        # Command: git commit -m "Initial backup"
        subprocess.run(
            ["git", "commit", "-m", "Initial backup"],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        # https://<user>:<token>@github.com/<user>/<repo>.git.
        auth_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

        print("-> Linking to remote repository...")
        # Command: git remote add origin <url>
        subprocess.run(
            ["git", "remote", "add", "origin", auth_url],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        print("-> Pushing files to GitHub...")
        # Command: git push -u origin main
        subprocess.run(
            ["git", "push", "-u", "origin", "main"],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        print("First push successfull.")
        return True

    except subprocess.CalledProcessError as e:
        print("\nAn error occurred while running a Git command.")
        print(f"    Error: {e.stderr.decode('utf-8').strip()}")
        return False


def _subsequent_push(directory: str) -> bool:
    """
    This helper pushes the backup directory to GitHub.

    Args:
        backup_dir (str): The path to the local backup directory.

    Returns:
        bool: True if everything was successfull.
    """

    try:
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=directory,
            capture_output=True,
            text=True,
            check=True,
        )
        if not status_result.stdout.strip():
            print("No changes to commit. Already up-to-date.")
            return

        # Command: git add .
        subprocess.run(
            ["git", "add", "."], cwd=directory, check=True, capture_output=True
        )

        # Command: git commit -m "Initial backup"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Update backup: {current_time}"
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        print("-> Pushing files to GitHub...")
        # Command: git push
        subprocess.run(
            ["git", "push"],
            cwd=directory,
            check=True,
            capture_output=True,
        )

        print("Push successfull.")

    except subprocess.CalledProcessError as e:
        print("\nAn error occurred while running a Git command.")
        print(f"    Error: {e.stderr.decode('utf-8').strip()}")


def _push() -> None:
    """
    This helper pushes the current backup_directory to github.
    """
    config = _get_config()
    if not config.has_section("GitHub") or not config.getboolean("GitHub", "enabled"):
        print("GitHub integration is disabled or not configured.")
        print("To enable it, please run: dotpush init github")
        return
    username = config["GitHub"]["username"]
    repo_name = config["GitHub"]["repo_name"]
    backup_dir = os.path.expanduser(config["Settings"]["backup_directory"])
    token = keyring.get_password("dotpush", "github_token")

    if not _check(backup_dir):
        _initialize_git_repo(username, repo_name, token, backup_dir)
    else:
        _subsequent_push(backup_dir)

    return None
