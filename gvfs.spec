Summary:	gvfs - userspace virtual filesystem
Summary(pl.UTF-8):	gvfs - wirtualny system plików w przestrzeni użytkownika
Name:		gvfs
Version:	0.1.2
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	732f3d49177cd4ec404e64870c3b3ecb
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel >= 1:10
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.2
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	libcdio-devel >= 0.78.2
BuildRequires:	libfuse-devel
BuildRequires:	libsmbclient-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via D-BUS. It contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It
also supports exposing the gvfs mounts to non-gio applications using
FUSE.

%description -l pl.UTF-8
gvfs to wirtualny system plik w przestrzeni użytkownika. Montowanie w
nim działa jako oddzielny proces, z którym komunikacja odbywa się
przez D-BUS. Zawiera moduł gio dodający w sposób przezroczysty obsługę
gfvs-a do wszystkich aplikacji używających API gio. Obsługuje także
montowania gvfs przy użyciu FUSE z myślą o aplikacjach nie
korzystających z gio.

%package libs
Summary:	gvfs libraries
Summary(pl.UTF-8):	Biblioteki gvfs
Group:		Libraries
Requires:	glib2 >= 1:2.15.1

%description libs
gvfs libraries.

%description libs -l pl.UTF-8
Biblioteki gvfs.

%package devel
Summary:	Header files for gvfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gvfs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.15.1

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
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gvfsd*
%attr(755,root,root) %{_libexecdir}/gvfs-fuse-daemon
%attr(755,root,root) %{_libdir}/gio/modules/*.so
%{_datadir}/dbus-1/services/gvfs-daemon.service
%dir %{_datadir}/gvfs
%dir %{_datadir}/gvfs/mounts
%{_datadir}/gvfs/mounts/*.mount

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvfscommon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so
%{_libdir}/libgvfscommon.la
%{_includedir}/gvfs-client
