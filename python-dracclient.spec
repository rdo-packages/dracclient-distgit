%{?!_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Summary:        Library for managing machines with Dell iDRAC cards
Version:        0.0.4
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://github.com/openstack/python-dracclient

Source0:        https://pypi.python.org/packages/source/d/dracclient/dracclient-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-requests >= 2.5.2
Requires: python-lxml >= 2.3

#patches_base=+1

%prep
%autosetup -v -p 1 -n dracclient-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%description
Library for managing machines with Dell iDRAC cards

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/*dracclient*

%changelog
* Sat Nov 07 2015 Mike Burns <mburns@redhat.com> 0.0.3-1
- Initial Spec
