import configparser
import os
from .. import constants


def _init(username: str = os.environ.get("USER")) -> None:
    """
    This helper initializes the configuration file for DotPush

    Args:
        username (str): The system username.
    """
    config_path = f"/home/{username}/.config/dotpush/config.ini"
    if os.path.exists(config_path):
        print("DotPush is already initialized.")
    else:
        default_config = configparser.ConfigParser()

        default_config["GitHub"] = {
            "username": username,
            "repository_url": f"https://github.com/{username}/dotfiles",
            "auto_push": True,
        }

        default_config["Settings"] = {
            "backup_directory": constants.BACKUP_DIRECTORY,
            "compression": False,
        }

        default_config["Schedule"] = {"enabled": False, "frequency": "daily"}

        default_config["Files"] = {
            "paths": "~/.bashrc ~/.bash_profile ~/.profile ~/.aliases ~/.config/Code/User/ ~/.gitconfig ~/.config/fish/ ~/.local/share/fonts/ ~/.config/gtk-3.0/"
        }

        with open(config_path, "w") as config_file:
            default_config.write(config_file)

        print(f"Initized config.ini at {config_path}")

    return None
