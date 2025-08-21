from datetime import datetime
from unittest import mock
from dotpush.utils.git_push import _initialize_git_repo, _subsequent_push


def test_first_push(mocker):
    """
    Tests that the first push/initializsation is called correctly.
    """

    mock_subprocess_run = mocker.patch("subprocess.run")
    mocker.patch("dotpush.utils.git_check._check_remote_repo", return_value=False)
    mocker.patch("dotpush.utils.git_init._create_remote_repository", return_value=True)

    _initialize_git_repo(
        username="test_user",
        repo_name="test_repo",
        token="test_token",
        directory="/fake/path",
    )

    # print("ACTUAL CALLS:", mock_subprocess_run.call_args_list) # Debug

    expected_commands = [
        mock.call(["git", "init"], cwd="/fake/path", check=True, capture_output=True),
        mock.call(
            ["git", "branch", "-M", "main"],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
        mock.call(
            ["git", "add", "."], cwd="/fake/path", check=True, capture_output=True
        ),
        mock.call(
            ["git", "commit", "-m", "Initial backup"],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
        mock.call(
            [
                "git",
                "remote",
                "add",
                "origin",
                "https://test_user:test_token@github.com/test_user/test_repo.git",
            ],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
        mock.call(
            ["git", "push", "-u", "origin", "main"],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
    ]

    mock_subprocess_run.assert_has_calls(expected_commands)

    assert mock_subprocess_run.call_count == 6


def test_subsequent_push(mocker):
    """
    Tests that every push (other than first one) is called correctly.
    """
    mock_datetime = mocker.patch("dotpush.utils.git_push.datetime")
    fake_time = datetime(2025, 8, 22, 12, 30, 0)
    mock_datetime.now.return_value = fake_time

    mock_git_status = mocker.Mock()
    mock_git_status.stdout = "M  .test_rc"

    mock_subprocess_run = mocker.patch("subprocess.run")
    mock_subprocess_run.return_value = mock_git_status

    mocker.patch("dotpush.utils.git_push.datetime.now", return_value=fake_time)
    commit_message = f"Update backup: {fake_time.strftime('%Y-%m-%d %H:%M:%S')}"

    _subsequent_push(directory="/fake/path")
    print("ACTUAL CALLS:", mock_subprocess_run.call_args_list)  # Debug

    expected_commands = [
        mock.call(
            ["git", "status", "--porcelain"],
            cwd="/fake/path",
            capture_output=True,
            text=True,
            check=True,
        ),
        mock.call(
            ["git", "add", "."], cwd="/fake/path", check=True, capture_output=True
        ),
        mock.call(
            ["git", "commit", "-m", commit_message],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
        mock.call(
            ["git", "push"],
            cwd="/fake/path",
            check=True,
            capture_output=True,
        ),
    ]

    mock_subprocess_run.assert_has_calls(expected_commands)
    assert mock_subprocess_run.call_count == 4
