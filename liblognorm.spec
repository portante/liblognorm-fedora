%define htmldir %{_docdir}/liblognorm/html

Name:		liblognorm
Version:	1.1.1
Release:	2%{?dist}
Summary:	Fast samples-based log normalization library
License:	LGPLv2+
URL:		http://www.liblognorm.com
Source0:	http://www.liblognorm.com/files/download/%{name}-%{version}.tar.gz

BuildRequires:	chrpath
BuildRequires:	json-c-devel
BuildRequires:	libestr-devel
BuildRequires:	pcre-devel

%description
Briefly described, liblognorm is a tool to normalize log data.

People who need to take a look at logs often have a common problem. Logs from
different machines (from different vendors) usually have different formats for
their logs. Even if it is the same type of log (e.g. from firewalls), the log
entries are so different, that it is pretty hard to read these. This is where
liblognorm comes into the game. With this tool you can normalize all your logs.
All you need is liblognorm and its dependencies and a sample database that fits
the logs you want to normalize.

%package devel
Summary:	Development tools for programs using liblognorm library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	json-c-devel%{?_isa}
Requires:	libestr-devel%{?_isa}

%description devel
The liblognorm-devel package includes header files, libraries necessary for
developing programs which use liblognorm library.

%package doc
Summary: HTML documentation for liblognorm
Group: Documentation
BuildRequires: python-sphinx

%description doc
This sub-package contains documentation for liblognorm in a HTML form.

%package utils
Summary:	Lognormalizer utility for normalizing log files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description utils
The lognormalizer is the core of liblognorm, it is a utility for normalizing
log files.

%prep
%setup -q

%build
%configure \
	--docdir=%{htmldir} \
	--enable-docs \
	--enable-regexp \

V=1 make

%install
make V=1 install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.{a,la}
chrpath -d %{buildroot}%{_bindir}/lognormalizer
chrpath -d %{buildroot}%{_libdir}/liblognorm.so
rm %{buildroot}%{htmldir}/{objects.inv,.buildinfo}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog README
%exclude %{htmldir}

%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{htmldir}

%files utils
%{_bindir}/lognormalizer


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Tomas Heinrich <theinric@redhat.com> - 1.1.1-1
- rebase to 1.1.1 (soname bump)
  - drop liblognorm-0.3.4-pc-file.patch, not needed anymore
  - update dependencies for the new version
  - add a new subpackage for documentation
  - enable support for reqular expressions
- make build more verbose

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Tomas Heinrich <theinric@redhat.com> - 0.3.7-1
- rebase to 0.3.7

* Wed Dec 12 2012 Mahaveer Darade <mah.darade@gmail.com> - 0.3.5-1
- upgrade to upstream version 0.3.5
- drop patch0, merged upstream
  liblognorm-0.3.4-rename-to-lognormalizer.patch
- remove trailing whitespace

* Fri Oct 05 2012 mdarade <mdarade@redhat.com> - 0.3.4-4
- Modified description of main & util package

* Thu Sep 20 2012 Mahaveer Darade <mdarade@redhat.com> - 0.3.4-3
- Renamed normalizer binary to lognormalizer
- Updated pc file to exclude lee and lestr

* Mon Aug 27 2012 mdarade <mdarade@redhat.com> - 0.3.4-2
- Updated BuildRequires to contain libestr-devel

* Wed Aug  1 2012 Milan Bartos <mbartos@redhat.com> - 0.3.4-1
- initial port
