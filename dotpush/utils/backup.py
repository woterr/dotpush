import shutil
import os


def _backup(backup_path: str, paths: list) -> None:
    """
    This helper backs up the given files into the specified directory.

    Args:
        backup_path (str): The path where the files are to be copied.
        paths (list): The list of paths to be copied.
    """
    print("Starting backup...")
    # Expand backup path
    full_backup_path = os.path.expanduser(backup_path)

    for source_path in paths:
        # Expand source path (files to be copied)
        full_source_path = os.path.expanduser(source_path)

        # Support basename for paths ending with `/`
        # (eg. '~/.config/Users/ which returns an empty string when basename is called)
        normalized_path = full_source_path.rstrip(os.sep)
        base_name = os.path.basename(normalized_path)

        if not base_name:
            print(
                f"    ->  Error: Could not determine a name for '{source_path}'. Skipping."
            )
            continue

        # backup path + basename
        # (eg. ~/.config/dotpush/backup + .bashrc => ~/.config/dotpush/backup/.bashrc)
        destination_path = os.path.join(full_backup_path, base_name)

        if os.path.exists(full_source_path):
            print(f"    -> Backing up {source_path}...")

            if os.path.islink(full_source_path):
                if os.path.lexists(destination_path):
                    os.remove(destination_path)

                shutil.copy2(full_source_path, destination_path, follow_symlinks=False)

            # Directories should be seperated from files
            if os.path.isdir(full_source_path):
                # Replace directory if it already exists
                if os.path.exists(destination_path):
                    shutil.rmtree(destination_path)
                shutil.copytree(full_source_path, destination_path)
            else:
                shutil.copy2(full_source_path, destination_path)

        else:
            print(f"    ->  Warning: Could not find {source_path}. Skipping.")
            continue

    print("\nBackup complete!")
