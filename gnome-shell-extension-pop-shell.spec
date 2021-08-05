%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      ab87042d2579c9ad9bb3271584b0281d97da7baa
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gnome-shell-extension-%{extension}
Version:        1.2.0^3.%{shortcommit}
Release:        %autorelease
Summary:        GNOME Shell extension for advanced tiling window management
# main license - GPLv3
# src/plugins/calc/math.js - ASL 2.0
# src/levenshtein.ts - MIT
License:        GPLv3 and ASL 2.0 and MIT
URL:            https://github.com/pop-os/shell
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only patch
Patch0:         0001-Remove-schema-handling-from-transpile.sh.patch

BuildRequires:  npm(typescript) >= 3.8
BuildRequires:  make

Requires:       gnome-shell-extension-common

Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}

Provides:       %{extension}
Provides:       bundled(npm(mathjs)) = 8.1.0
Provides:       bundled(npm(js-levenshtein))


%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly-sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n shell-%{commit}

# remove launcher plugin developer guide
rm src/plugins/README.md


%build
%make_build compile


%install
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_prefix}/lib/pop-shell


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
%autochangelog
