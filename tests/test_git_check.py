import os
from dotpush.utils.git_check import _check as is_git_repo


def test_is_git_repo_when_repo_exists(tmp_path):
    """
    Tests that is_git_repo returns True when a .git directory exists.
    """
    git_dir = os.path.join(tmp_path, ".git")
    os.makedirs(git_dir)

    result = is_git_repo(tmp_path)

    assert result is True


def test_is_git_repo_when_repo_does_not_exist(tmp_path):
    """
    Tests that is_git_repo returns False when no .git directory exists.
    """
    result = is_git_repo(tmp_path)

    assert result is False
