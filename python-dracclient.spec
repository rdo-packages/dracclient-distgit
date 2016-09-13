%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        0.1.0
Release:        1%{?dist}
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-lxml
BuildRequires:  python-requests

Provides: python-dracclient = %{upstream_version}

%description
Library for managing machines with Dell iDRAC cards.

%prep
%setup -q -n %{name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python2_sitelib}/dracclient*
%{python2_sitelib}/python_dracclient*

%changelog
* Tue Sep 13 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.1.0-1
- Update to 0.1.0

