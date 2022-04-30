# Maintainer: Henrik Mundt Milo <henrik265@outlook.dk>
pkgname="prio"
pkgver=1
pkgrel=1
pkgdesc="Easily configurable daemon to adjust niceness and ionice values"
arch=("x86_64")
url="https://github.com/HenrikDK2/prio"
license=('MIT')
depends=("python>=3.10.0", "python<4.0.0")
makedepends=('git')
source=('prio::git://github.com/HenrikDK2/prio.git')
md5sums=('SKIP')

pkgver() {
	cd "$"

}

build() {
	cd "$srcdir/${pkgname%-VCS}"
	./autogen.sh
	./configure --prefix=/usr
	make
}

check() {
	cd "$srcdir/${pkgname%-VCS}"
	make -k check
}

package() {
	cd "$srcdir/${pkgname%-VCS}"
	make DESTDIR="$pkgdir/" install
}
