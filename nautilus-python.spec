#
# Conditional build:
%bcond_without	apidocs	# gtk-doc based API documentation

Summary:	Python bindings for GNOME nautilus 4
Summary(pl.UTF-8):	Wiązania Pythona dla nautilusa 4 z GNOME
Name:		nautilus-python
Version:	4.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/nautilus-python/4.0/%{name}-%{version}.tar.xz
# Source0-md5:	ae577de94059968003c723d7f039c45f
URL:		https://wiki.gnome.org/Projects/NautilusPython
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	nautilus-devel >= 43
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	nautilus >= 43
Requires:	python-pygobject3 >= 3.0.0
Obsoletes:	nautilus3-python < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-python is a set of Python bindings for the Nautilus Extension
Framework. With these bindings, you can write extensions for the
Nautilus File Manager in Python.

%description -l pl.UTF-8
Nautilus-python to zestaw wiązań Pythona do szkieletu rozszerzeń
Nautilusa. Przy ich użyciu można tworzyć rozszerzenia zarządcy plików
Nautilus w Pythonie.

%package devel
Summary:	Development files for Python Nautilus extensions
Summary(pl.UTF-8):	Pliki programistyczne dla pythonowych rozszerzeń Nautilusa
Group:		Development/Libraries
# doesn't require base; the only file is pkg-config specific, so let's require it
Requires:	pkgconfig
Obsoletes:	nautilus3-python-devel < 4
BuildArch:	noarch

%description devel
Development files for Nautilus 4 extensions written in Python.

%description devel -l pl.UTF-8
Pliki programistyczne dla rozszerzeń zarządcy plików Nautilus 4
pisanych w Pythonie.

%package apidocs
Summary:	Python Nautilus 4 API documentation
Summary(pl.UTF-8):	Dokumentacja API Pythona dla rozszerzeń Nautilusa 4
Group:		Documentation
Obsoletes:	nautilus3-python-apidocs < 4
BuildArch:	noarch

%description apidocs
Python Nautilus 4 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Pythona dla rozszerzeń zarządcy plików Nautilus 4.

%package examples
Summary:	Example Python extensions for Nautilus 4 file manager
Summary(pl.UTF-8):	Przykładowe pythonowe rozszerzenia dla zarządcy plików Nautilus 4
Group:		Libraries/Python
Obsoletes:	nautilus3-python-examples < 4

%description examples
Example Python extensions for Nautilus 4 file manager.

%description examples -l pl.UTF-8
Przykładowe rozszerzenia dla zarządcy plików Nautilus 4 napisane w
Pythonie.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Ddocs=enabled}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions \
	$RPM_BUILD_ROOT%{_examplesdir}

%ninja_install -C build

# move examples
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/nautilus-python/README $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS.md README.md
%attr(755,root,root) %{_libdir}/nautilus/extensions-4/libnautilus-python.so
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/nautilus-python.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/nautilus-python
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
