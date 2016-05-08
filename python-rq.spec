#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	rq
Summary:	RQ is a simple, lightweight, library for creating background jobs, and processing them
Name:		python-%{module}
Version:	0.5.6
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/c4/7f/a26b981b99ecc56b28f3de27e9f7dc2d5f16dd2f833e80c01b24bdeb9a5c/%{module}-%{version}.tar.gz
# Source0-md5:	8c72aae6e95379a07fd000752b1acfbf
URL:		https://github.com/nvie/rq/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rq is a simple, lightweight, library for creating background jobs, and
processing them.

%package -n python3-%{module}
Summary:	RQ is a simple, lightweight, library for creating background jobs, and processing them
Group:		Libraries/Python

%description -n python3-%{module}
rq is a simple, lightweight, library for creating background jobs, and
processing them.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
