%define major 2
%define libname %mklibname zrtpcpp %{major}
%define devname %mklibname zrtpcpp -d

Summary:	A ccrtp extension for zrtp/Zfone support
Name:		libzrtpcpp
Version:	2.3.4
Release:	3
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnu.org/software/commoncpp/commoncpp.html
Source0:	ftp://ftp.gnu.org/gnu/ccrtp/libzrtpcpp-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/ccrtp/libzrtpcpp-%{version}.tar.gz.sig
Patch0:		libzrtpcpp-2.3.4-compile.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	stdc++-devel
BuildRequires:	pkgconfig(libccext2)
BuildRequires:	pkgconfig(libccrtp)
BuildRequires:	pkgconfig(libgcrypt)

%description
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications.  The current
release is based on a beta draft of the zrtp spec.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Abstract asynchronous event notification library
Group:		System/Libraries

%description -n %{libname}
This library is a GPL licensed extension to the GNU RTP Stack, ccrtp, that
offers compatibility with Phil Zimmermann's zrtp/Zfone voice encryption, and
which can be directly embedded into telephony applications. The current
release is based on a beta draft of the zrtp spec.

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
%doc AUTHORS COPYING
%dir %{_includedir}/libzrtpcpp
%{_includedir}/libzrtpcpp/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake -G Ninja
%ninja

%install
%ninja_install -C build

