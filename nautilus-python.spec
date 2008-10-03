Summary:	Python bindings for GNOME 2's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 2
Name:		nautilus-python
Version:	0.5.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	f46cd826d74f62ef7bba5b258c1d415a
Patch0:		%{name}-dir.patch
Patch1:		%{name}-api.patch
URL:		http://www.gnome.org/
BuildRequires:	nautilus-devel >= 2.8
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-gnome-vfs >= 2.12.0
BuildRequires:	python-pygtk-devel
BuildRequires:	sed >= 4.0
Requires:	python-gnome-gconf
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
%patch1 -p1
sed -i 's/codegen.py/codegen.pyc/' configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/python

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	NAUTILUS_LIBDIR=%{_libdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/nautilus-python
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/*.so
%dir %{_libdir}/nautilus/extensions-2.0/python
%{_pkgconfigdir}/nautilus-python.pc
