%include	/usr/lib/rpm/macros.python

Summary:	Tool for finding bugs in Python source code
Summary(pl):	Narz�dzie do wyszukiwania b��d�w w programach napisanych w Pythonie
Name:		pychecker
Version:	0.8.10
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://prdownloads.sourceforge.net/pychecker/%{name}-%{version}.tar.gz
Patch0:		%{name}-checker.patch
URL:		http://pychecker.sourceforge.net
BuildRequires:	rpm-pythonprov >= 4.0.2-50
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
%setup  -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG MAINTAINERS KNOWN_BUGS TODO pycheckrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/pychecker/*.py[co]
