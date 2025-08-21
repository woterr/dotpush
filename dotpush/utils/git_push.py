import keyring


def _push():
    token = keyring.get_password("dotpush", "github_token")
    print(token)
    # c c
    return None
