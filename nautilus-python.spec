Summary:	Python bindings for GNOME 3's nautilus
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa z GNOME 3
Name:		nautilus-python
Version:	1.2.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/nautilus-python/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	adb0886ef62df810ba31c9dbd7e821c0
URL:		https://wiki.gnome.org/Projects/NautilusPython
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libxslt-progs
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	nautilus >= 3.0.0
Requires:	python-pygobject3 >= 3.0.0
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
BuildArch:	noarch

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

# move examples
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/README $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# reference docs source
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/nautilus-python/reference

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
