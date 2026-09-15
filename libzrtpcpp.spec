%define major 4
%define libname %mklibname zrtpcpp %{major}
%define devname %mklibname zrtpcpp -d

Summary:	A ccrtp extension for zrtp/Zfone support
Name:		libzrtpcpp
Version:	4.6.6
Release:	1
License:	GPLv3+
Group:		System/Libraries
Url:		https://github.com/wernerd/ZRTPCPP
Source0:	https://github.com/wernerd/ZRTPCPP/archive/V%{version}/%{name}-%{version}.tar.gz
Patch0:		libzrtpcpp-4.4.0-no-warning.patch
Patch1:		libzrtpcpp-gcc15.patch
Patch2:		libzrtpcpp_cmakever.patch
Patch3:		libzrtpcpp_cmakesyntax.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libccrtp)
BuildRequires:	pkgconfig(libgcrypt)

BuildSystem:	cmake
BuildOption:	-DCCRTP:BOOL=ON
BuildOption:	-DCRYPTO_STANDALONE:BOOL=ON

%description
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	ZRTP support library for GNU ccRTP
Group:		System/Libraries

%description -n %{libname}
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.

%files -n %{libname}
%{_libdir}/libzrtpcpp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development library and header files for the libzrtpcpp library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides the header files, link libraries, and documentation for
building applications that use libzrtpcpp.

%files -n %{devname}
%doc AUTHORS COPYING NEWS.md README.md
%{_includedir}/libzrtpcpp
%{_libdir}/libzrtpcpp.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n ZRTPCPP-%{version}
chmod 644 NEWS.md
