Name:           stremio-linux-shell
Version:        1.1.2
Release:        3.main%{?dist}
Summary:        Native GTK4 client for Stremio on Linux

License:        GPL-3.0-only
URL:            https://github.com/Stremio/stremio-linux-shell

Source0:        https://github.com/Stremio/stremio-linux-shell/archive/refs/heads/main.tar.gz
Source1:        stremio.desktop
Source2:        stremio.sh
Source3:        com.stremio.Stremio.service

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  webkitgtk6.0-devel
BuildRequires:  mpv-devel
BuildRequires:  libepoxy-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2
BuildRequires:  appstream

Requires:       nodejs

%description
Native GTK4 + libadwaita + WebKitGTK + libmpv shell for Stremio on Linux.

%prep
%autosetup -n stremio-linux-shell-main

%build
cargo build --release

%install
# Main executable
install -Dm755 target/release/stremio-linux-shell \
    %{buildroot}%{_libexecdir}/stremio/stremio

# Node.js backend
install -Dm644 data/server.js \
    %{buildroot}%{_libexecdir}/stremio/server.js

# Desktop entry
install -Dm644 %{SOURCE1} \
    %{buildroot}%{_datadir}/applications/stremio.desktop

# Launcher wrapper
install -Dm755 %{SOURCE2} \
    %{buildroot}%{_bindir}/stremio

# Icons
install -Dm644 data/icons/com.stremio.Stremio.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.stremio.Stremio.svg

install -Dm644 data/icons/symbolic.png \
    %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/com.stremio.Stremio-symbolic.png

# GSettings schema
install -Dm644 data/com.stremio.Stremio.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/com.stremio.Stremio.gschema.xml

# D-Bus service
install -Dm644 %{SOURCE3} \
    %{buildroot}%{_datadir}/dbus-1/services/com.stremio.Stremio.service

# AppStream metadata
install -Dm644 data/com.stremio.Stremio.metainfo.xml \
    %{buildroot}%{_metainfodir}/com.stremio.Stremio.metainfo.xml

# Translations
install -Dm644 po/es/LC_MESSAGES/stremio.mo \
    %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/stremio.mo

install -Dm644 po/fr/LC_MESSAGES/stremio.mo \
    %{buildroot}%{_datadir}/locale/fr/LC_MESSAGES/stremio.mo

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/stremio.desktop

appstreamcli validate \
    %{buildroot}%{_metainfodir}/com.stremio.Stremio.metainfo.xml

%files
%license LICENSE

%{_bindir}/stremio

%dir %{_libexecdir}/stremio
%{_libexecdir}/stremio/stremio
%{_libexecdir}/stremio/server.js

%{_datadir}/applications/stremio.desktop

%{_datadir}/icons/hicolor/scalable/apps/com.stremio.Stremio.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.stremio.Stremio-symbolic.png

%{_datadir}/glib-2.0/schemas/com.stremio.Stremio.gschema.xml
%{_datadir}/dbus-1/services/com.stremio.Stremio.service
%{_metainfodir}/com.stremio.Stremio.metainfo.xml

%{_datadir}/locale/es/LC_MESSAGES/stremio.mo
%{_datadir}/locale/fr/LC_MESSAGES/stremio.mo

%changelog
* Wed, 08 July 2026 GlockTwentyFive <redninjaxbt@gmail.com> - 1.1.2-3.main
- Build from upstream main branch
- Rename installed executable to stremio
- Install GSettings schema
- Install D-Bus service
- Install AppStream metadata
- Install translations
- Validate desktop entry and AppStream metadata
