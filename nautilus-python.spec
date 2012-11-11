Summary:	Python bindings for GNOME 3's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 3
Name:		nautilus-python
Version:	1.0
Release:	6
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	64ceb67b6b167c2d17ac46f23ec70828
URL:		http://www.gnome.org/
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygobject-devel >= 2.28.2
Requires:	nautilus >= 3.0.0
Requires:	python-pygobject >= 2.28.2
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install examples
cp examples/{README,*.py} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-python.so
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions
%{_pkgconfigdir}/nautilus-python.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
