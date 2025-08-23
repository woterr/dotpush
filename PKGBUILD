# Maintainer: Woter <im.woterr@gmail.com>

pkgname=dotpush
pkgver=1.0.2
pkgrel=1
pkgdesc="A tool to back up dotfiles and push to GitHub."
arch=('any')
url="https://github.com/woterr/dotpush"
license=('MIT')
depends=('python' 'python-keyring' 'python-requests' 'python-installer')
makedepends=('python-build' 'python-wheel' 'python-setuptools')
source=(source=("$pkgname-$pkgver.tar.gz::https://github.com/woterr/dotpush/archive/refs/tags/v$pkgver.tar.gz"))
sha256sums=('12c4efc5ec41d9c2c1c81584363696cb52c2ed02913c435de0b37e2b652f046d')
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
