%global pypi_name wsproto

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        2
Summary:        WebSockets state-machine based protocol implementation
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/wsproto/
Source0:        https://files.pythonhosted.org/packages/source/w/wsproto/wsproto-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(h11)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)

Requires:       python%{pyver}dist(h11)

%description
WebSockets state-machine based protocol implementation

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/wsproto-%{version}.dist-info/
%{python_sitelib}/wsproto/
