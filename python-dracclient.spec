%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        1.6.0
Release:        1%{?dist}
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
# All this is required to run unit tests in check phase
BuildRequires:  python-lxml
BuildRequires:  python2-mock
BuildRequires:  python2-requests
BuildRequires:  python-requests-mock

Requires: python-lxml
Requires: python2-requests

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
* Thu Nov 29 2018 Jon Schlueter <jschluet@redhat.com> 1.6.0-1
- Update to 1.6.0

* Mon Sep 24 2018 RDO <dev@lists.rdoproject.org> 1.5.0-1
- Update to 1.5.0

* Tue Feb 13 2018 RDO <dev@lists.rdoproject.org> 1.3.1-1
- Update to 1.3.1

