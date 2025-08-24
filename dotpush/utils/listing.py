from .config import _get_config


def _list_paths() -> None:
    """
    Lists all paths present in the config file.
    """
    config = _get_config()
    paths = config.get("Files", "paths").split()

    if len(paths) == 0:
        print(
            "You are current tracking no files. Use dotpush add <path/s> to track files."
        )
    for i in paths:
        print(f"    -> {i}")

    return None
