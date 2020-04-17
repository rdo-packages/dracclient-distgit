%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        XXX
Release:        XXX
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch

%description
Library for managing machines with Dell iDRAC cards.

%package -n     python3-dracclient
Summary:        Library for managing machines with Dell iDRAC cards.
%{?python_provide:%python_provide python3-dracclient}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# All this is required to run unit tests in check phase
BuildRequires:  python3-mock
BuildRequires:  python3-requests

BuildRequires:  python3-lxml
BuildRequires:  python3-requests-mock

Requires: python3-requests

Requires: python3-lxml

%description -n     python3-dracclient
Library for managing machines with Dell iDRAC cards.

%prep
%setup -q -n %{name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} -m unittest discover dracclient.tests

%files -n     python3-dracclient
%doc README.rst LICENSE
%{python3_sitelib}/dracclient*
%{python3_sitelib}/python_dracclient*

%changelog
