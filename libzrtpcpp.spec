%define api 1.4
%define	major 0
%define libname	%mklibname zrtpcpp %{api} %{major}
%define develname %mklibname zrtpcpp -d

Summary:	A ccrtp extension for zrtp/Zfone support
Name:		libzrtpcpp
Version:	1.4.1
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/commoncpp/commoncpp.html
Source0:	ftp://ftp.gnu.org/gnu/cccrtp/libzrtpcpp-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/cccrtp/libzrtpcpp-%{version}.tar.gz.sig
Requires:	ccrtp >= 1.7.0
BuildRequires:	ccrtp-devel >= 1.7.0
BuildRequires:	pkgconfig
BuildRequires:	libstdc++-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libCommonC++-devel
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
Provides:       %{name} = %{version}-%{release}
Obsoletes:	%{mklibname zrtpcpp 0} < %{version}-%{release}

%description -n	%{libname}
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

%package -n	%{develname}
Summary:	Static library and header files for the libzrtpcpp library
Group:		Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d zrtpcpp 0.9}

%description -n	%{develname}
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

This package provides the header files, link libraries, and documentation for
building applications that use libzrtpcpp.

%prep
%setup -q

%build
export LDFLAGS="-s"
%configure2_5x
%make LIBTOOL=%_bindir/libtool

%install
rm -rf %{buildroot}

%makeinstall_std
rm -rf %{buildroot}/%{_infodir}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*%{api}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/libzrtpcpp
%{_includedir}/libzrtpcpp/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc


