%global debug_package %{nil}

Name:		multibootusb
Version:	9.2.0
Release:	5
License:	GPLv2+
Group:		File tools
Summary:	Create multiboot live Linux on a USB disk
Url:		https://multibootusb.org
Source0:	https://github.com/mbusb/multibootusb/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
# Dirty but needed. Allow to run app from .desktop file as root. W/o we can't. Only CLI works. If anyone know better solution, pls fix it. (penguin)
Patch0:  	multibootusb-fix-desktop-start-as-root.patch

BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
Requires:	mtools
Requires:	util-linux
Requires:	parted
Requires:	python-qt5
Requires:	python-dbus
Requires:	python-six
Requires:	polkit
Requires:	p7zip
Suggests:	qemu
#BuildArch:	noarch

%description
MultiBootUSB is a cross platform* software/utility to create multi boot live 
Linux on a removable media i.e USB disk. 
It is similar to unetbootin but many distros can be installed, 
provided you have enough space on the disk. 
MultiBootUSB also provides an option to uninstall distro(s) at any time, 
if you wish.

%files
%doc CHANGELOG LICENSE.txt README.md
%{py_puresitedir}/scripts
%{py_puresitedir}/multibootusb-%{version}*
%{_bindir}/multibootusb
%{_bindir}/multibootusb-pkexec
%{_datadir}/applications/multibootusb.desktop
%{_datadir}/pixmaps/multibootusb.png
%{_datadir}/polkit-1/actions/org.debian.pkexec.run-multibootusb.policy
%dir %{_datadir}/multibootusb
%{_datadir}/multibootusb/*
#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build

%install
python setup.py install --root=%{buildroot}
