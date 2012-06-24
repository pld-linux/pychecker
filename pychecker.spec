Summary:	Tool for finding bugs in Python source code
Summary(pl):	Narz�dzie do wyszukiwania b��d�w w programach napisanych w Pythonie
Name:		pychecker
Version:	0.8.16
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/pychecker/%{name}-%{version}.tar.gz
# Source0-md5:	531214b2c922462eb57dde5d37f004ac
URL:		http://pychecker.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyChecker is a tool for finding bugs in Python source code. It finds
problems that are typically caught by a compiler for less dynamic
languages, like C and C++.

%description -l pl
PyChecker jest narz�dziem do wyszukiwania b��d�w w programach
napisanych w Pythonie. Znajduje problemy, kt�re s� zazwyczaj
wy�apywane przez kompilator w mniej dynamicznych j�zykach takich jak C
czy C++.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

echo -e '#!/bin/sh
python %{py_sitescriptdir}/pychecker/checker.pyc "$@"
' > $RPM_BUILD_ROOT%{_bindir}/pychecker

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG MAINTAINERS KNOWN_BUGS TODO pycheckrc
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/pychecker
%{py_sitescriptdir}/pychecker/*.py[co]
