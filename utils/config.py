import configparser
import os

def _get_config(username=os.environ.get("USER")):
    """
    This helper fetches the system configuration/s set for DotPush.

    Args:
        username (str): The system username.
    
    Returns:
        config (ConfigParser): An object containing system configuration/s.
    """

    config = configparser.ConfigParser()
    files_read = config.read(f"/home/{username}/.config/dotpush/config.ini")

    if not files_read:
        raise FileNotFoundError("config.ini was not found. Create one in ~/.config/dotpush/ or run dotpush init")

    return config