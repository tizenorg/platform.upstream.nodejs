Name:          node
Version:       0.10.13
Release:       1
Summary:       Node.js is a server-side JavaScript environment that uses an asynchronous event-driven model.
Packager:      Naruto TAKAHASHI <tnaruto@gmail.com>
Group:         Development/Libraries
License:       MIT License
URL:           http://nodejs.org
Source0:       %{url}/dist/v%{version}/%{name}-v%{version}.tar.gz
Provides:      npm
BuildRequires: which
BUildRequires: gcc-c++
BUildRequires: python
BuildRequires: openssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel
ExclusiveArch:  %{ix86} x86_64 %arm

%ifarch i586 i686 
%global target ia32
%endif
%ifarch x86_64
%global target x64
%endif
%ifarch armv7l armv7hl
%global target arm
%endif

%description
Node.js is a server-side JavaScript environment that uses an asynchronous event-driven model.
This allows Node.js to get excellent performance based on the architectures of many Internet applications.

%prep
%setup -q -n %{name}-v%{version}

%build
./configure --prefix=%{_prefix} \
	--dest-cpu=%{target} \
	--shared-openssl \
	--shared-zlib

make 

%install
rm -rf %{buildroot}
./tools/install.py install %{buildroot}
chmod 0755 %{buildroot}/%{_bindir}/node

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/lib/node_modules/npm
%{_prefix}/share/man/man1/node.1.gz
%{_prefix}/lib/dtrace/node.d
%defattr(755,root,root)
%{_bindir}/node
%{_bindir}/npm

%doc
/usr/share/man/man1/node.1.gz


%changelog
