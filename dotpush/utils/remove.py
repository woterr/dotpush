import configparser
import os
from .. import constants


def _remove_paths(paths_to_remove: list) -> None:
    """
    This helper removes a given path into config.ini for
    the tracking list.

    Args:
        paths_to_add (list): List of source paths.
    """

    config_path = os.path.expanduser(constants.CONFIG_PATH)
    config = configparser.ConfigParser()
    config.read(config_path)
    paths = config.get("Files", "paths").split()
    home_dir = os.path.expanduser("~")

    for path in paths_to_remove:
        if path.startswith(home_dir):
            path = "~" + path[len(home_dir) :]

        if path in paths:
            paths.remove(path)
            print(f"    -> Path: {path} has been removed from the tracking list.")

    new_paths_string = " ".join(paths)
    config.set("Files", "paths", new_paths_string)

    try:
        with open(config_path, "w") as config_file:
            config.write(config_file)

        print("Configuration saved successfully.")
        print("Run dotpush backup to synchronize your backup folder.")
        print("Run dotpush push to synchronize your remote github repository.")
        return None
    except Exception as e:
        print(f"An error occurred while removing the path: {e}")
        return None
