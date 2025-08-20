import configparser
import os
import constants

def _init(username=os.environ.get("USER")):
    """
    This helper initializes the configuration file for DotPush

    Args:
        username (str): The system username.

    Returns:
        None
    """
    config_path = f"/home/{username}/.config/dotpush/config.ini"
    if os.path.exists(config_path):
        print("DotPush is already initialized.")
    else:
        default_config = configparser.ConfigParser()

        default_config['GitHub'] = {
            'username': username,
            'repository_url': f'https://github.com/{username}/dotfiles'
        }

        default_config['Settings'] = {
            'auto_push': True,
            'backup_directory': constants.BACKUP_DIRECTORY
        }

        default_config['FilesToTrack'] = {
            'file1': '~/.bashrc'
        }

        with open(config_path, "w") as config_file:
            default_config.write(config_file)
        
        print(f"Initized config.ini at {config_path}")

    return None