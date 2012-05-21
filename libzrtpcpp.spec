%define	major 2
%define libname	%mklibname zrtpcpp %{major}
%define develname %mklibname zrtpcpp -d

Summary:	A ccrtp extension for zrtp/Zfone support
Name:		libzrtpcpp
Version:	2.0.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnu.org/software/commoncpp/commoncpp.html
Source0:	ftp://ftp.gnu.org/gnu/ccrtp/libzrtpcpp-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/ccrtp/libzrtpcpp-%{version}.tar.gz.sig
#Requires:	ccrtp >= 1.7.0
BuildRequires:	ccrtp-devel >= 1.7.0
BuildRequires:	libstdc++-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libCommonC++-devel
BuildRequires:	cmake

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
%cmake
%make
#LIBTOOL=%_bindir/libtool

%install
pushd build
%makeinstall_std
popd
#rm -rf %{buildroot}/%{_infodir}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/libzrtpcpp
%{_includedir}/libzrtpcpp/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
