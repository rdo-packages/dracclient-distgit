%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        1.1.1
Release:        1%{?dist}
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
# All this is required to run unit tests in check phase
BuildRequires:  python-lxml
BuildRequires:  python-mock
BuildRequires:  python-requests
BuildRequires:  python-requests-mock

Requires: python-lxml
Requires: python-requests

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

%check
%{__python2} -m unittest discover dracclient.tests

%files
%doc README.rst LICENSE
%{python2_sitelib}/dracclient*
%{python2_sitelib}/python_dracclient*

%changelog
* Wed Mar 03 2017 Dmitry Tantsur <divius.inside@gmail.com> 1.1.1-1
- Update to 1.1.1

* Fri Nov 11 2016 Dmitry Tantsur <divius.inside@gmail.com> 1.0.0-1
- Update to 1.0.0

* Tue Sep 13 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.1.0-1
- Update to 0.1.0

