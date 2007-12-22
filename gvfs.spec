Summary:	gvfs
Name:		gvfs
Version:	0.1.0
Release:	1
License:	LGPL v2
Group:		System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	6477f9f37de9310d43a3c89414832a9d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 2.15.0
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	libcdio-devel
BuildRequires:	libfuse-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtool
Requires:	glib2 >= 2.15.0
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fixme

%package libs
Summary:	gvfs libs
Group:		Libraries

%description libs
fixme

%package devel
Summary:	Header files for gvfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gvfs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for gvfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gvfs

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
%find_lang gvfs

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f gvfs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO

%dir %{_sysconfdir}/gvfs
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gvfs/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libexecdir}/gvfsd*
%attr(755,root,root) %{_libexecdir}/gvfs-fuse-daemon
%attr(755,root,root) %{_libdir}/gio/modules/*.so
%{_datadir}/dbus-1/services/gvfs-daemon.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/lib*.la

%files devel
%defattr(644,root,root,755)
%{_includedir}/gvfs-client
%{_libdir}/lib*.so
