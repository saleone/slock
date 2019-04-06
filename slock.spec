%define debug_package %{nil}

Name: slock
Version: 1.4
Release: 1%{?dist}
Summary: Simple screen locker utility for X

License: MIT
URL: https://github.com/saleone/slock
Source0: https://github.com/saleone/slock/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel


%description
%{summary}


%prep
%autosetup


%build
%make_build


%install
%make_install

%files
/usr/local/bin/slock
/usr/local/share/man/man1/slock.1

%changelog
* Sat Apr 6 2019 Saša Savić <sasa@sasa-savic.com> 1.4-1
- Initial RPM release

