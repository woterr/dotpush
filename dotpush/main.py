import os
from . import constants
from .utils.config import _get_config
from .utils.init import _init
from .utils.backup import _backup
from .utils.git_init import _git_init
from .utils.git_push import _push
from .utils.add import _add_paths
from .utils.remove import _remove_paths
from .utils.listing import _list_paths


def init(service: str = None, force: bool = False):
    """Initializes DotPush"""
    _init(force)  # local init
    if service == "github":
        _git_init(force)


def backup():
    """The main backup tool for DotPush"""
    config = _get_config()
    paths = config.get("Files", "paths").split()
    backup_path = config.get("Settings", "backup_directory")
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


def add(paths):
    """Add a path to the tracking list."""
    _add_paths(paths)


def remove(paths):
    """Remove a path from the tracking list."""
    _remove_paths(paths)


def listing():
    """List all paths being tracked."""
    _list_paths()
