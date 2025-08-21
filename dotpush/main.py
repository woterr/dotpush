import os
from . import constants
from .utils.config import _get_config
from .utils.init import _init
from .utils.backup import _backup
from .utils.git_init import _git_init
from .utils.git_push import _push


def init(service: str = None):
    """Initializes DotPush"""
    _init()  # local init
    if service == "github":
        _git_init()


def backup():
    """The main backup tool for DotPush"""
    config = _get_config()
    paths = config.get("Files", "paths").split()
    backup_path = config["Settings"]["backup_directory"]
    if os.path.exists(os.path.expanduser(backup_path)):
        _backup(backup_path=backup_path, paths=paths)
    else:
        print(
            f"    -> Backup path not found. Creating backup in {constants.BACKUP_DIRECTORY}"
        )
        os.makedirs(os.path.expanduser(constants.BACKUP_DIRECTORY))
        _backup(backup_path=constants.BACKUP_DIRECTORY, paths=paths)


def push():
    """Autopush logic for the backup directory."""
    _push()
