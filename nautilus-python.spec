Summary:	Python bindings for GNOME 2's nautilus
Name:		nautilus-python
Version:	0.4.3
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-python/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	d676ff598426fbcda3f103d41d60d520
URL:		http://www.gnome.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-gnome-vfs >= 2.12.0
BuildRequires:	python-pygtk-devel
Requires:	python-gnome-gconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are unstable bindings for the nautilus extension library
introduced in Gnome 2.6.

%prep
%setup -q
sed -i 's/codegen.py/codegen.pyc/' configure.in
mkdir local
cat << 'EOF' > local/acinclude.m4
AC_DEFUN([AM_CHECK_PYTHON_HEADERS],
[AC_REQUIRE([AM_PATH_PYTHON])
AC_MSG_CHECKING(for headers required to compile python extensions)
dnl deduce PYTHON_INCLUDES
py_prefix=`$PYTHON -c "import sys; print sys.prefix"`
py_exec_prefix=`$PYTHON -c "import sys; print sys.exec_prefix"`
PYTHON_INCLUDES="-I${py_prefix}/include/python${PYTHON_VERSION}"
if test "$py_prefix" != "$py_exec_prefix"; then
  PYTHON_INCLUDES="$PYTHON_INCLUDES -I${py_exec_prefix}/include/python${PYTHON_VERSION}"
fi
AC_SUBST(PYTHON_INCLUDES)
dnl check if the headers exist:
save_CPPFLAGS="$CPPFLAGS"
CPPFLAGS="$CPPFLAGS $PYTHON_INCLUDES"
AC_TRY_CPP([#include <Python.h>],dnl
[AC_MSG_RESULT(found)
$1],dnl
[AC_MSG_RESULT(not found)
$2])
CPPFLAGS="$save_CPPFLAGS"
])
EOF

%build
%{__libtoolize}
%{__aclocal} -I local
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/python
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	NAUTILUS_LIBDIR=%{_libdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/nautilus-python
%{_libdir}/nautilus/extensions-1.0/*.so
%dir %{_libdir}/nautilus/extensions-1.0/python
%{_pkgconfigdir}/nautilus-python.pc
