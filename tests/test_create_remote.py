from dotpush.utils.git_init import _create_remote_repository


def test_create_remote_repository(mocker):
    """
    Tests that the function returns True and calls the API correctly on success.
    """

    mock_response = mocker.Mock()
    mock_response.status_code = 201

    mock_post = mocker.patch("requests.post", return_value=mock_response)

    success = _create_remote_repository(
        repo_name="test_repo",
        git_username="test_username",
        is_private=True,
        token="test_token",
    )

    assert success is True

    mock_post.assert_called_once_with(
        "https://api.github.com/user/repos",
        headers={"Authorization": "token test_token"},
        json={"name": "test_repo", "private": True},
    )
