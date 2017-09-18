# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        XXX
Release:        XXX
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  openstack-macros

%description
Library for managing machines with Dell iDRAC cards.

%package -n     python%{pyver}-dracclient
Summary:        Library for managing machines with Dell iDRAC cards.
%{?python_provide:%python_provide python%{pyver}-dracclient}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
# All this is required to run unit tests in check phase
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-requests

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-lxml
BuildRequires:  python-requests-mock
%else
BuildRequires:  python%{pyver}-lxml
BuildRequires:  python%{pyver}-requests-mock
%endif

Requires: python%{pyver}-requests

# Handle python2 exception
%if %{pyver} == 2
Requires: python-lxml
%else
Requires: python%{pyver}-lxml
%endif

%description -n     python%{pyver}-dracclient
Library for managing machines with Dell iDRAC cards.

%prep
%setup -q -n %{name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Let RPM handle the dependencies
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%check
%{pyver_bin} -m unittest discover dracclient.tests

%files -n     python%{pyver}-dracclient
%doc README.rst LICENSE
%{pyver_sitelib}/dracclient*
%{pyver_sitelib}/python_dracclient*

%changelog
