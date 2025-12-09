Summary: DRBD distributed resource management utility
Name:    linstor-client
Version: 1.27.0
Release: 1%{?dist}
License: GPL-3.0-or-later
URL:     https://linbit.com/linstor/

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python-linstor >= %{version}

Source0: https://pkg.linbit.com/downloads/linstor/linstor_client-%{version}.tar.gz

%description
This client program communicates to controller node which manages the resources

%prep
%autosetup -p1 -n linstor_client-%{version}

%build
PYTHON=%{__python3} %{__python3} ./setup.py build

%install
PYTHON=%{__python3} %{__python3} ./setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%license COPYING
%doc README.md

%changelog
* Tue Dec 09 2025 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.27.0-1
- Update to linstor-client-1.27.0

* Tue Sep 10 2024 Ronan Abhamon <ronan.abhamon@vates.tech> - 1.23.0-1
- Update to linstor-client-1.23.0

* Tue Nov 07 2023 Thierry Escande <thierry.escande@vates.tech> - 1.19.0-1
- Update to linstor-client-1.19.0
