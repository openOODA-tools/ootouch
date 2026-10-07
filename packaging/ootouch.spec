Name:           ootouch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-safe file creation and access/modification timestamp updater.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootouch
Source0:        ootouch-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootouch is a sovereign, capability-bounded TIMESTAMP SETTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootouch
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootouch-uninstall

%files
/usr/bin/ootouch
/usr/bin/ootouch-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
