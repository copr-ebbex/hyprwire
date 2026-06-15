Name:           hyprwire
Version:        0.3.1
Release:        %autorelease
Summary:        A fast and consistent wire protocol for IPC

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwire
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(hyprutils) >= 0.9.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(pugixml)

%description
Hyprwire is a fast and consistent wire protocol for IPC used by Hyprland
and related components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%package -n     hyprwire-scanner
Summary:        Protocol code generator for hyprwire
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n hyprwire-scanner
A protocol code generator for hyprwire, used to generate C++ bindings
from hyprwire protocol XML definitions.

%prep
%autosetup -p1
sed -i 's/-Wpedantic//' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libhyprwire.so.3
%{_libdir}/libhyprwire.so.%{version}

%files devel
%{_includedir}/hyprwire/
%{_libdir}/libhyprwire.so
%{_libdir}/pkgconfig/hyprwire.pc

%files -n hyprwire-scanner
%{_bindir}/hyprwire-scanner
%{_libdir}/cmake/hyprwire-scanner/
%{_libdir}/pkgconfig/hyprwire-scanner.pc

%changelog
%autochangelog
