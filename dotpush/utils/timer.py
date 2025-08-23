import subprocess


def is_timer_active() -> bool:
    """
    This helper checks if the auto-push feature is
    enabled or not.

    Returns:
        bool: True if it is enabled.
    """

    try:
        subprocess.check_call(
            ["systemctl", "--user", "is-active", "--quiet", "dotpush.timer"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def enable_timer() -> None:
    """
    Enables the autopush feature
    """

    try:
        subprocess.check_call(
            ["systemctl", "--user", "enable", "--now", "dotpush.timer"]
        )
        print("Timer enabled successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable the timer. Error: {e}")
