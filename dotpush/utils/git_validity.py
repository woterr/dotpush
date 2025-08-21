import requests


def _is_valid(token: str) -> bool:
    """
    Checks if a GitHub Personal Access Token is valid.

    Args:
        token (str): The PAT to validate.

    Returns:
        bool: True if the token is valid, False otherwise.
    """

    if not token:
        return False

    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {token}"}

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200

    except requests.exceptions.RequestException as e:
        # Handle network errors, etc.
        print(f"An error occurred while validating the token: {e}")
        return False
