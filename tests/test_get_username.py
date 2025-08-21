from dotpush.utils.git_init import _get_username_from_token


def test_get_username_from_token_success(mocker):
    """
    Tests that the function returns a username when the API call is successful.
    """

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"login": "testuser"}

    mock_get = mocker.patch("requests.get", return_value=mock_response)
    username = _get_username_from_token("fake_token")

    assert username == "testuser"

    mock_get.assert_called_once_with(
        "https://api.github.com/user", headers={"Authorization": "token fake_token"}
    )


def test_get_username_from_token_failure(mocker):
    """
    Tests that the function returns None when the API call fails.
    """

    mock_response = mocker.Mock()
    mock_response.status_code = 401

    mocker.patch("requests.get", return_value=mock_response)

    username = _get_username_from_token("bad_token")

    assert username is None
