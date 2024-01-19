%global pypi_name wsproto

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1
Summary:        WebSockets state-machine based protocol implementation
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/wsproto/
Source0:        https://files.pythonhosted.org/packages/source/w/wsproto/wsproto-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(h11)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)

Requires:       python3dist(h11)

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

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
