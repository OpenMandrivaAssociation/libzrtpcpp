%define	major 0.9
%define libname	%mklibname zrtpcpp %{major}

Summary:	A ccrtp extension for zrtp/Zfone support
Name:		libzrtpcpp
Version:	0.9.0
Release:	%mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.gnu.org/software/commoncpp/commoncpp.html
Source0:	ftp://ftp.gnu.org/gnu/cccrtp/libzrtpcpp-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/cccrtp/libzrtpcpp-%{version}.tar.gz.sig
Requires:	ccrtp >= 1.5.0
BuildRequires:	ccrtp-devel >= 1.5.0
BuildRequires:	pkgconfig
BuildRequires:	libstdc++-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

%package -n	%{libname}
Summary:	Abstract asynchronous event notification library
Group:          System/Libraries

%description -n	%{libname}
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

%package -n	%{libname}-devel
Summary:	Static library and header files for the libzrtpcpp library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

This package provides the header files, link libraries, and documentation for
building applications that use libzrtpcpp.

%prep

%setup -q

%build
%configure2_5x

%make LDFLAGS="-s" CXXFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

%makeinstall
rm -rf %{buildroot}/%{_infodir}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%dir %{_includedir}/libzrtpcpp
%{_includedir}/libzrtpcpp/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


