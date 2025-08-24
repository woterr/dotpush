# DotPush

A lightweight tool that helps backup dotfiles and automatically push to a remote github repository.

---

[![Run Tests](https://github.com/woterr/dotpush/actions/workflows/tests.yml/badge.svg)](https://github.com/woterr/dotpush/actions/workflows/tests.yml) [![Run Linter and Formatter](https://github.com/woterr/dotpush/actions/workflows/ci.yml/badge.svg)](https://github.com/woterr/dotpush/actions/workflows/ci.yml)

[![AUR version](https://img.shields.io/aur/version/dotpush)](https://aur.archlinux.org/packages/dotpush)  ![AUR License](https://img.shields.io/aur/license/dotpush) ![AUR Popularity](https://img.shields.io/aur/popularity/:packageName)


## Features
- Backs up dotfiles and configuration directories.
- Secure GitHub push with token management.
- Autopush and backup feature that runs hourly.
- Preserve symlinks and file metadata.

## Installation

**Install from AUR**
```bash
yay -S dotpush
```

**Manual Installation**:

1. Clone the repository.
```bash
git clone https://github.com/woterr/dotpush.git
cd dotpush
```

2. Build the package:
```bash
makepkg -si
```

- `makepkg` reads your PKGBUILD, fetches the release tarball (from GitHub), checks SHA256, builds the wheel, installs everything including systemd service/timer files.
- `-s` ensures dependencies are installed.
- `-i` installs the package after building.

3. Verify installation:
```bash
dotpush --help
```

## Usage

1. Initialize DotPush.

```bash
dotpush init
```
(Run `dotpush init github` for GitHub integration)

2. Check `config.ini` and add paths as per requirement.

```bash
nano ~/.config/dotpush/config.ini
```

3. Backup your DotFiles.

```bash
dotpush backup
```

4. Manually push your DotFiles.

```bash
dotpush push
```

> [!NOTE]
> The automated `dotpush backup` and `dotpush push` can be enabled by running dotpush backup and push.

## Contributing

Feel free to open issues or PRs. If you're unsure, just fork and experiment.

## License

This project is licensed under the MIT License. Read [LICENSE](LICENSE) for full license text.
