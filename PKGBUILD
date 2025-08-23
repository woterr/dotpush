# Maintainer: Woter <your.email@example.com>

pkgname=dotpush
pkgver=1.0.0
pkgrel=1
pkgdesc="A tool to back up dotfiles and push to GitHub."
arch=('any')
url="https://github.com/woterr/dotpush"
license=('MIT')
depends=('python' 'python-keyring' 'python-requests' 'python-installer')
makedepends=('python-build' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('c3fece6fb7c33626401f6d855ecc989f42c2b041dfbb06068aeaea6762a79aac')
install='dotpush.install'

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"

    # python -m pip install --root="$pkgdir" --prefix=/usr dist/*.whl
    python -m installer --destdir="$pkgdir" dist/*.whl

    install -Dm644 "systemd/dotpush.service" "$pkgdir/usr/lib/systemd/user/dotpush.service"
    install -Dm644 "systemd/dotpush.timer" "$pkgdir/usr/lib/systemd/user/dotpush.timer"
}
