Summary:	gvfs - userspace virtual filesystem
Name:		gvfs
Version:	0.1.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	6477f9f37de9310d43a3c89414832a9d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	libcdio-devel >= 0.78.2
BuildRequires:	libfuse-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2 >= 1:2.15.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via D-BUS. It contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It
also supports exposing the gvfs mounts to non-gio applications using
FUSE.

%package libs
Summary:	gvfs libraries
Summary(pl.UTF-8):	Biblioteki gvfs
Group:		Libraries

%description libs
gvfs libraries.

%description libs -l pl.UTF-8
Biblioteki gvfs.

%package devel
Summary:	Header files for gvfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gvfs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for gvfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gvfs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang gvfs

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f gvfs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO

%dir %{_sysconfdir}/gvfs
%dir %{_sysconfdir}/gvfs/mounts
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gvfs/mounts/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gvfsd*
%attr(755,root,root) %{_libexecdir}/gvfs-fuse-daemon
%attr(755,root,root) %{_libdir}/gio/modules/*.so
%{_datadir}/dbus-1/services/gvfs-daemon.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so.*.*.*
%{_libdir}/libgvfscommon.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so
%{_includedir}/gvfs-client
