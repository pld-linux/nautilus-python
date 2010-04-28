Summary:	Python bindings for GNOME 2's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 2
Name:		nautilus-python
Version:	0.6.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	fa56dadfa98b7b3d29408d57f01756a5
URL:		http://www.gnome.org/
BuildRequires:	nautilus-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygobject-devel >= 2.16.0
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

%package examples
Summary:	Example scripts
Summary(pl.UTF-8):	Przykładowe skrypty
Group:		Libraries/Python

%description examples
Example scripts.

%description examples -l pl.UTF-8
Przykładowe skrypty.

%prep
%setup -q

sed -i 's/codegen.py/codegen.pyc/' configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/python
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install examples
cp examples/{README,*.py} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
