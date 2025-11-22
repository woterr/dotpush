# Maintainer: Woter im.woterr@gmail.com

pkgname=dotpush
pkgver=1.1.0
pkgrel=1
pkgdesc="A tool to back up dotfiles and push to GitHub."
arch=('any')
url="https://github.com/woterr/dotpush"
license=('MIT')
depends=('python' 'python-keyring' 'python-requests' 'python-installer')
makedepends=('python-build' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/woterr/dotpush/releases/download/v$pkgver/dotpush-$pkgver.tar.gz")
sha256sums=('36d9ddf88314ac5a448e1ff380e63ed9e4e10b5ec4567c513a905cc9d0ffee92')
install='dotpush.install'

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname-$pkgver"

    python -m installer --destdir="$pkgdir" dist/*.whl

    install -Dm644 "systemd/dotpush.service" "$pkgdir/usr/lib/systemd/user/dotpush.service"
    install -Dm644 "systemd/dotpush.timer" "$pkgdir/usr/lib/systemd/user/dotpush.timer"
}
