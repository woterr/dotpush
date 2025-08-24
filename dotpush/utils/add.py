import configparser
import os
from .. import constants


def _add_paths(paths_to_add: list) -> None:
    """
    This helper appends a given path into config.ini for
    the tracking list.

    Args:
        paths_to_add (list): List of source paths.
    """

    config_path = os.path.expanduser(constants.CONFIG_PATH)
    config = configparser.ConfigParser()
    config.read(config_path)
    paths = config.get("Files", "paths").split()
    home_dir = os.path.expanduser("~")

    for path in paths_to_add:
        if not os.path.exists(os.path.expanduser(path)):
            print(f"    -> Path: {path} does not exist.")
            continue

        if path.startswith(home_dir):
            path = "~" + path[len(home_dir) :]

        if path in paths:
            print("    -> {path} already exists in your config file.")
            continue

        paths.append(path)
        print(f"    -> Path: {path} has been appended to the tracking list.")

    new_paths_string = " ".join(paths)
    config.set("Files", "paths", new_paths_string)

    try:
        with open(config_path, "w") as config_file:
            config.write(config_file)

        print("Configuration saved successfully.")
        return None
    except Exception as e:
        print(f"An error occurred while appending the path: {e}")
        return None
