Summary:	Python bindings for GNOME 3's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 3
Name:		nautilus-python
Version:	1.0
Release:	9
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	64ceb67b6b167c2d17ac46f23ec70828
URL:		http://www.gnome.org/
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libxslt-progs
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygobject-devel >= 2.28.2
BuildRequires:	python-pygobject-apidocs >= 2.28.2
Requires:	nautilus >= 3.0.0
Requires:	python-pygobject >= 2.28.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are unstable bindings for the nautilus extension library
introduced in GNOME 2.6.

%description -l pl.UTF-8
Ten pakiet zawiera niestabilne wiązania dla biblioteki rozszerzeń
nautilusa wprowadzonej w GNOME 2.6.

%package devel
Summary:	Development files for Python Nautilus extensions
Summary(pl.UTF-8):	Pliki programistyczne dla pythonowych rozszerzeń Nautilusa
Group:		Development/Libraries
# doesn't require base; the only file is pkg-config specific, so let's require it
Requires:	pkgconfig

%description devel
Development files for Nautilus extensions written in Python.

%description devel -l pl.UTF-8
Pliki programistyczne dla rozszerzeń zarządcy plików Nautilus pisanych
w Pythonie.

%package apidocs
Summary:	Python Nautilus API documentation
Summary(pl.UTF-8):	Dokumentacja API Pythona dla rozszerzeń Nautilusa
Group:		Documentation

%description apidocs
Python Nautilus API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Pythona dla rozszerzeń zarządcy plików Nautilus.

%package examples
Summary:	Example Python extensions for Nautilus file manager
Summary(pl.UTF-8):	Przykładowe pythonowe rozszerzenia dla zarządcy plików Nautilus
Group:		Libraries/Python

%description examples
Example Python extensions for Nautilus file manager.

%description examples -l pl.UTF-8
Przykładowe rozszerzenia dla zarządcy plików Nautilus napisane w
Pythonie.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/python

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/nautilus-python

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

# not installed because of incomplete docs/Makefile
cp -p docs/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/nautilus-python

# move examples
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/README $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-python.so
%dir %{_libdir}/nautilus/extensions-3.0/python
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/nautilus-python.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/nautilus-python

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
