# TODO:
# - package examples
# - does not build (at least) on th/x86_64:
#   In file included from nautilus.override:26:
#   /usr/include/gnome-python-2.0/pygnomevfs.h:7:40: error: libgnomevfs/gnome-vfs-init.h: No such file or directory
#   /usr/include/gnome-python-2.0/pygnomevfs.h:8:39: error: libgnomevfs/gnome-vfs-uri.h: No such file or directory
#   /usr/include/gnome-python-2.0/pygnomevfs.h:9:45: error: libgnomevfs/gnome-vfs-file-info.h: No such file or directory
#   
Summary:	Python bindings for GNOME 2's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 2
Name:		nautilus-python
Version:	0.5.1
Release:	2.1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	83136937cdb790a2ee5823e96de20acf
Patch0:		%{name}-libpython-soname.patch
URL:		http://www.gnome.org/
BuildRequires:	eel-devel >= 2.6.0
BuildRequires:	nautilus-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	sed >= 4.0
Requires:	python-gnome-gconf
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are unstable bindings for the nautilus extension library
introduced in GNOME 2.6.

%description -l pl.UTF-8
Ten pakiet zawiera niestabilne wiązania dla biblioteki rozszerzeń
nautilusa wprowadzonej w GNOME 2.6.

%prep
%setup -q
%patch0 -p1

sed -i 's/codegen.py/codegen.pyc/' configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/python

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus{-python,/extensions-2.0}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/nautilus-python
%attr(755,root,root) %{_libdir}/nautilus-python/nautilus.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-python.so
%dir %{_libdir}/nautilus/extensions-2.0/python
%{_pkgconfigdir}/nautilus-python.pc
