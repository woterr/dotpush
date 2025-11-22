# DotPush

A lightweight tool that helps backup dotfiles and automatically push to a remote github repository.

---

[![Run Tests](https://github.com/woterr/dotpush/actions/workflows/tests.yml/badge.svg)](https://github.com/woterr/dotpush/actions/workflows/tests.yml) [![Run Linter and Formatter](https://github.com/woterr/dotpush/actions/workflows/ci.yml/badge.svg)](https://github.com/woterr/dotpush/actions/workflows/ci.yml)

![AUR Version](https://img.shields.io/aur/version/dotpush) ![AUR License](https://img.shields.io/aur/license/dotpush) ![AUR Maintainer](https://img.shields.io/aur/maintainer/dotpush)

[![Packaging status](https://repology.org/badge/vertical-allrepos/dotpush.svg)](https://repology.org/project/dotpush/versions)

## Links

- [Dotpush Wiki (Full documentation)](https://github.com/woterr/dotpush/wiki)
- [DotPush on AUR](https://aur.archlinux.org/packages/dotpush)

# Quick start
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

Or you can add/remove paths using:
```bash
dotpush add <path/s>
```
```bash
dotpush remove <path/s>
```

To list all paths being tracked:
```bash
dotpush list paths
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

5. Troubleshooting

If you have to reinitialize DotPush for your backup directory:

```bash
dotpush init --force
```

And for GitHub:

```bash
dotpush init github --force
```

## Contributing

Feel free to open issues or PRs. If you're unsure, just fork and experiment. Read [Developer Environment Wiki](https://github.com/woterr/dotpush/wiki/Developer-Environment) to get started.

## License

This project is licensed under the MIT License. Read [LICENSE](LICENSE) for full license text.
