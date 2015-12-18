Name:          nodejs
Version:       4.2.3
Release:       1
Summary:       Evented I/O for V8 JavaScript
Group:         System/Service
URL:           http://nodejs.org/
Source:        %{name}-%{version}.tar.gz
Source1:       %{name}.pc.in
Source2:       %{name}.manifest
License:       MIT
BuildRequires: python
BuildRequires: fdupes
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(openssl)

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
Development libraries for Node.js

%package npm
Summary:       npm tools for %{name}
Group:         Development/Libraries
Requires:      %{name}

%description npm
npm tools for Node.js

%prep
%setup -q

cp %{SOURCE2} .

%build

./configure --prefix=%{_prefix} \
	--without-dtrace \
	--shared-zlib \
	--shared-openssl

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}/%{_libdir}/pkgconfig
sed -e "s#@prefix@#%{_prefix}#g" \
    -e "s#@exec_prefix@#%{_exec_prefix}#g" \
    -e "s#@libdir@#%{_libdir}#g" \
    -e "s#@includedir@#%{_includedir}/node#g" \
    -e "s#@version@#%{version}#g" \
    %SOURCE1 > %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc

# copy common.gypi for node-gyp
cp common.gypi %{buildroot}/%{_includedir}/node/common.gypi

# cleanup leftover cruft
rm -f %{buildroot}/usr/share/systemtap/tapset/node.stp
rm -fr %{buildroot}/usr/share/doc
rm -fr %{buildroot}/usr/share/man

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/node

%files devel
%{_includedir}/node/
%{_libdir}/pkgconfig/*.pc

%files npm
%{_bindir}/npm
/usr/lib/node_modules/npm/

