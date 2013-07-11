Name:          nodejs
Version:       0.10.13
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

%description
Node.js is a platform built on Chromes JavaScript runtime for easily building fast,
scalable network applications. Node.js uses an event-driven, non-blocking I/O model
that makes it lightweight and efficient, perfect for data-intensive real-time
applications that run across distributed devices.

%prep
%setup -q

%build

./configure --prefix=%{_prefix} --without-dtrace --without-npm
make %{?_smp_mflags}

%install
%make_install

# cleanup leftover cruft
rm -fR %{buildroot}/usr/lib/dtrace

%docs_package

%files
%defattr(-,root,root)
%{_bindir}/node
