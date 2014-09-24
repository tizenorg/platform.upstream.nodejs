Name:          nodejs
Version:       0.12.0
Release:       1
Summary:       Evented I/O for V8 JavaScript
Group:         System/Service
URL:           http://nodejs.org/
Source:        %{name}-%{version}.tar.gz
License:       MIT
BuildRequires: glibc-devel
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
BuildRequires: python
BuildRequires: fdupes

%description
Node.js is a platform built on Chromes JavaScript runtime for easily building fast,
scalable network applications. Node.js uses an event-driven, non-blocking I/O model
that makes it lightweight and efficient, perfect for data-intensive real-time
applications that run across distributed devices.

%package devel
Summary:       Header files for %{name}
Group:         Development/Libraries
Requires:      %{name}

%description devel
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. This allows Node.js to get excellent performance based on
the architectures of many Internet applications.

%prep
%setup -q

%build

./configure --prefix=%{_prefix} --without-dtrace --shared-openssl --shared-zlib
make %{?_smp_mflags}

%install
%make_install

# cleanup leftover cruft
rm -fR %{buildroot}/usr/lib/dtrace
find %{buildroot}/usr/lib/node_modules -name '\.*' -delete
rm -f %{buildroot}/usr/share/systemtap/tapset/node.stp

%fdupes %{buildroot}/usr/lib/node_modules

%docs_package

%files
%defattr(-,root,root)
%{_bindir}/node
%{_bindir}/npm
%dir /usr/lib/node_modules
%dir /usr/lib/node_modules/npm
/usr/lib/node_modules/npm/*

%files devel
%{_includedir}/node/
