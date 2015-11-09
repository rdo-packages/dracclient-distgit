%{?!_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        0.0.4
Release:        1
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

#patches_base=+1

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr

BuildRequires: python-lxml
BuildRequires: python-requests

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
* Mon Nov 09 2015 Mike Burns <mburns@redhat.com> 0.0.4-1
- Initial Spec
