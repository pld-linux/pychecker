%include	/usr/lib/rpm/macros.python

Summary:	Tool for finding bugs in Python source code
Summary(pl):	Narzêdzie do wyszukiwania b³êdów w programach napisanych w Pythonie
Name:		pychecker
Version:	0.8.12
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	aedbfe99ed1f540cc27243ec22b913c7
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
PyChecker jest narzêdziem do wyszukiwania b³êdów w programach
napisanych w Pythonie. Znajduje problemy, które s± zazwyczaj
wy³apywane przez kompilator w mniej dynamicznych jêzykach takich jak C
czy C++.

%prep
%setup  -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG MAINTAINERS KNOWN_BUGS TODO pycheckrc
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/pychecker/
%{py_sitedir}/pychecker/*.py[co]
