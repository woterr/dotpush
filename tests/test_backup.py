from dotpush.utils.backup import _backup


def test_backup_copies_files_and_directories(tmp_path):
    """
    Tests that the _backup function correctly copies both files and directories.
    """

    source_dir = tmp_path / "source"
    source_dir.mkdir()

    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    dummy_file = source_dir / ".test_rc"
    dummy_file.write_text("this is a test file")

    dummy_dir = source_dir / ".test_config"
    dummy_dir.mkdir()
    (dummy_dir / "settings.conf").write_text("some setting")

    paths_to_backup = [str(dummy_file), str(dummy_dir)]

    _backup(str(dest_dir), paths_to_backup)

    expected_file_path = dest_dir / ".test_rc"
    assert expected_file_path.exists()
    assert expected_file_path.is_file()

    expected_dir_path = dest_dir / ".test_config"
    assert expected_dir_path.exists()
    assert expected_dir_path.is_dir()

    assert (expected_dir_path / "settings.conf").exists()
