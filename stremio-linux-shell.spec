Name:           stremio-linux-shell
Version:        1.1.2
Release:        1%{?dist}
Summary:        Native GTK4 client for Stremio on Linux

License:        GPL-3.0-only
URL:            https://github.com/Stremio/stremio-linux-shell
Source0:        https://github.com/Stremio/stremio-linux-shell/archive/refs/tags/v%{version}.tar.gz
Source1:        stremio.desktop
Source2:        stremio.sh

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  webkitgtk6.0-devel
BuildRequires:  mpv-devel
BuildRequires:  libepoxy-devel
BuildRequires:  desktop-file-utils

Requires:       nodejs24

%description
Native GTK4 + libadwaita + WebKitGTK + libmpv shell for Stremio on Linux.

%prep
%autosetup -n stremio-linux-shell-%{version}

%build
cargo build --release

%install
install -Dm755 target/release/stremio-linux-shell \
    %{buildroot}%{_libexecdir}/stremio/stremio-linux-shell
install -Dm644 data/server.js \
    %{buildroot}%{_libexecdir}/stremio/server.js

install -Dm644 data/icons/com.stremio.Stremio.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.stremio.Stremio.svg
install -Dm644 data/icons/symbolic.png \
    %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.stremio.Stremio-symbolic.png

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/stremio.desktop
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/stremio.sh

desktop-file-validate %{buildroot}%{_datadir}/applications/stremio.desktop

%files
%license LICENSE
%{_libexecdir}/stremio/
%{_datadir}/icons/hicolor/scalable/apps/com.stremio.Stremio.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.stremio.Stremio-symbolic.png
%{_datadir}/applications/stremio.desktop
%{_bindir}/stremio.sh

%changelog
* Wed Jul 08 2026 GlockTwentyFive <redninjaxbt@gmail.com> - 1.1.2-1
- Initial package
