import subprocess
from pathlib import Path
import re

VALID_INTERVAL = re.compile(r"^\d+[smhd]$")  # e.g. 10m, 2h, 1d


def validate_interval(interval: str) -> bool:
    """
    Validate the given interval using regex.
    """
    return bool(VALID_INTERVAL.match(interval))


SYSTEMD_USER_DIR = Path.home() / ".config/systemd/user"
SERVICE_FILE = SYSTEMD_USER_DIR / "dotpush.service"
TIMER_FILE = SYSTEMD_USER_DIR / "dotpush.timer"


def write_unit(path: Path, content: str):
    """
    Write to path
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def _schedule(interval: str = "1hr", command: str = "dotpush push"):
    """
    This helper creates and writes dotpush.timer and dotpush.service to systemd.

    Args:
        interval (str): The timer interval.
        command (str): The command to enable timer for.
    """

    service = f"""[Unit]
    Description=Run dotpush command

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/{command}
    """

    timer = f"""[Unit]
    Description=Run dotpush every {interval}

    [Timer]
    OnUnitActiveSec={interval}
    Persistent=true

    [Install]
    WantedBy=timers.target
    """

    write_unit(SERVICE_FILE, service)
    write_unit(TIMER_FILE, timer)

    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    subprocess.run(
        ["systemctl", "--user", "enable", "--now", "dotpush.timer"], check=True
    )

    print(f"Scheduled dotpush every {interval}.")
