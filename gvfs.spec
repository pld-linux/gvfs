#
# Conditional build:
%bcond_without	doc		# do not build and package docs
%bcond_without	http	# do not build http/dav backend
%bcond_without	avahi	# do not build avahi support
%bcond_without	udev	# build without libudev
%bcond_without	fuse	# build without FUSE support
%bcond_with		gdu		# build with GDU (Gnome Disk Utility) volume monitor
%bcond_without	udisks2	# build without libudisks2
%bcond_without	systemd	# build without liblibsystemd-login
%bcond_without	gudev	# build without gudev support (use HAL)
%bcond_without	cdda	# build without CDDA backend
%bcond_without	afc		# build without AFC backend
%bcond_without	goa		# build without GOA backend
%bcond_without	obexftp	# build without ObexFTP backend
%bcond_without	gphoto2	# build without gphoto2 support
%bcond_with		keyring	# build without GNOME Keyring support
%bcond_without	bluray	# build without bluray metadata support
%bcond_without	mtp		# build without libmtp support
%bcond_without	samba	# build without samba support
%bcond_without	gtk		# build without GTK+
%bcond_without	archive	# build without archive support
%bcond_without	afp		# build without AFP support

%if %{without gudev}
%undefine	with_gphoto2
%undefine	with_mtp
%endif

%ifarch s390 s390x
%undefine	with_afc
%endif

Summary:	gvfs - userspace virtual filesystem
Summary(pl.UTF-8):	gvfs - wirtualny system plików w przestrzeni użytkownika
Name:		gvfs
Version:	1.18.3
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/1.18/%{name}-%{version}.tar.xz
# Source0-md5:	3620baa478f1748bd32d2f47bcbe30d0
Patch0:		set_attributes_from_info-v1.patch
URL:		https://live.gnome.org/gvfs
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
%{?with_avahi:BuildRequires:	avahi-devel >= 0.6.22}
%{?with_avahi:BuildRequires:	avahi-glib-devel >= 0.6.22}
%{?with_obexftp:BuildRequires:	bluez-libs-devel >= 4.0}
%{?with_cdda:BuildRequires:	cdparanoia-III-devel >= 1:10}
BuildRequires:	dbus-devel
%{?with_obexftp:BuildRequires:	dbus-glib-devel}
%{?with_obexftp:BuildRequires:	expat-devel >= 1.95}
BuildRequires:	glib2-devel >= 1:2.38.0
%{?with_gdu:BuildRequires:	gnome-disk-utility-devel >= 3.0.2}
%{?with_goa:BuildRequires:	gnome-online-accounts-devel >= 3.8.0}
%{?with_gtk:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
%{?with_archive:BuildRequires:	libarchive-devel >= 3.0.22}
%{?with_bluray:BuildRequires:	libbluray-devel}
%{?with_cdda:BuildRequires:	libcdio-paranoia-devel >= 0.78.2}
BuildRequires:	libexif-devel
%{?with_fuse:BuildRequires:	libfuse-devel >= 2.8.0}
%{?with_afp:BuildRequires:	libgcrypt-devel >= 1.2.2}
%{?with_gphoto2:BuildRequires:	libgphoto2-devel >= 2.5.0}
%{?with_afc:BuildRequires:	libimobiledevice-devel >= 1.1.5}
%{?with_mtp:BuildRequires:	libmtp-devel >= 1.1.6}
%{?with_afc:BuildRequires:	libplist-devel >= 0.15}
BuildRequires:	libsecret-devel
%{?with_keyring:BuildRequires:	libsecret-devel}
%{?with_samba:BuildRequires:	libsmbclient-devel >= 3.0}
%{?with_http:BuildRequires:	libsoup-gnome-devel >= 2.34.0}
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libusb-devel
%{?with_http:BuildRequires:	libxml2-devel >= 1:2.6.31}
%{?with_doc:BuildRequires:	libxslt-progs}
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
%{?with_systemd:BuildRequires:	systemd-devel >= 44}
BuildRequires:	tar >= 1:1.22
%{?with_udev:BuildRequires:	udev-devel >= 1:138}
%{?with_gudev:BuildRequires:	udev-glib-devel >= 001}
%{?with_udisks2:BuildRequires:	udisks2-devel >= 1.97.0}
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	%{name}-libs = %{version}-%{release}
%{?with_avahi:Requires:	avahi-glib >= 0.6.22}
%{?with_cdda:Requires:	cdparanoia-III-libs >= 1:10}
%{?with_cdda:Requires:	libcdio-paranoia >= 0.78.2}
Requires:	libplist >= 0.15
Requires:	libsoup-gnome >= 2.34.0
Requires:	libxml2 >= 1:2.6.31
Requires:	udev-libs >= 1:138
%{?with_udisks2:Requires:	udisks2 >= 1.97.0}
%{?with_afc:Suggests:	%{name}-afc}
%{?with_afp:Suggests:	%{name}-afp}
%{?with_archive:Suggests:	%{name}-archive}
%{?with_fuse:Suggests:	%{name}-fuse}
%{?with_goa:Suggests:	%{name}-goa}
%{?with_gphoto2:Suggests:	%{name}-gphoto2}
%{?with_mtp:Suggests:	%{name}-mtp}
%{?with_samba:Suggests:	%{name}-smb}
%{?with_obexftp:Suggests:	obex-data-server >= 0.4}
Obsoletes:	gnome-mount <= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via D-BUS. It contains a gio module that
seamlessly adds gvfs support to all applications using the gio API.

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
Requires:	glib2 >= 1:2.38.0

%description libs
gvfs libraries.

%description libs -l pl.UTF-8
Biblioteki gvfs.

%package devel
Summary:	Header files for gvfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gvfs
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.38.0

%description devel
Header files for gvfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gvfs.

%package -n bash-completion-gvfs
Summary:	bash-completion for gvfs
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla gvfs
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2

%description -n bash-completion-gvfs
This package provides bash-completion for gvfs.

%description -n bash-completion-gvfs -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla gvfs.

%package fuse
Summary:	FUSE support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fuse
Conflicts:	%{name} < 1.18.3-5

%description fuse
This package provides support for applications not using gio to access
the gvfs filesystems.

%package smb
Summary:	Windows fileshare support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	%{name} < 1.18.3-5

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using gvfs.

%package archive
Summary:	Archiving support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libarchive >= 3.0.22

%description archive
This package provides support for accessing files inside Zip and Tar
archives, as well as ISO images, to applications using gvfs.

%package gphoto2
Summary:	gphoto2 support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	%{name} < 1.18.3-5

%description gphoto2
This package provides support for reading and writing files on PTP
based cameras (Picture Transfer Protocol) and MTP based media players
(Media Transfer Protocol) to applications using gvfs.

%package afc
Summary:	AFC support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libimobiledevice >= 1.1.5
Requires:	usbmuxd
Conflicts:	%{name} < 1.18.3-5

%description afc
This package provides support for reading files on mobile devices
including phones and music players to applications using gvfs.

%package afp
Summary:	AFP support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	%{name} < 1.18.3-5

%description afp
This package provides support for reading and writing files on Mac OS
X and original Mac OS network shares via Apple Filing Protocol to
applications using gvfs.

%package mtp
Summary:	MTP support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmtp >= 1.1.6
Conflicts:	%{name} < 1.18.3-5

%description mtp
This package provides support for reading and writing files on MTP
based devices (Media Transfer Protocol) to applications using gvfs.

%package goa
Summary:	GOA support for gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-online-accounts-libs >= 3.8.0
Conflicts:	%{name} < 1.18.3-5

%description goa
This package provides seamless integration with gnome-online-accounts
file services.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SSH_PROGRAM=/usr/bin/ssh \
	%{__enable_disable afc} \
	%{__enable_disable afp} \
	%{__enable_disable archive} \
	%{__enable_disable avahi} \
	%{__enable_disable bluray} \
	%{__enable_disable cdda} \
	%{__enable_disable documentation doc} \
	%{__enable_disable fuse} \
	%{__enable_disable gdu} \
	%{__enable_disable goa} \
	%{__enable_disable gphoto2} \
	%{__enable_disable gtk} \
	%{__enable_disable gudev} \
	%{__enable_disable http} \
	%{__enable_disable keyring} \
	%{__enable_disable mtp} \
	%{__enable_disable obexftp} \
	%{__enable_disable samba} \
	%{__enable_disable systemd libsystemd-login} \
	%{__enable_disable udev} \
	%{__enable_disable udisks2} \
	--disable-hal \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang gvfs

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules
# Reload .mount files:
killall -USR1 gvfsd >/dev/null 2>&1 || :

%postun
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules
exit 0

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

# Reload .mount files when single subpackage is installed:
%post smb
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post gphoto2
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post mtp
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post goa
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post afc
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post archive
killall -USR1 gvfsd >/dev/null 2>&1 || :

%files -f gvfs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gvfs-cat
%attr(755,root,root) %{_bindir}/gvfs-copy
%attr(755,root,root) %{_bindir}/gvfs-info
%attr(755,root,root) %{_bindir}/gvfs-less
%attr(755,root,root) %{_bindir}/gvfs-ls
%attr(755,root,root) %{_bindir}/gvfs-mime
%attr(755,root,root) %{_bindir}/gvfs-mkdir
%attr(755,root,root) %{_bindir}/gvfs-monitor-dir
%attr(755,root,root) %{_bindir}/gvfs-monitor-file
%attr(755,root,root) %{_bindir}/gvfs-mount
%attr(755,root,root) %{_bindir}/gvfs-move
%attr(755,root,root) %{_bindir}/gvfs-open
%attr(755,root,root) %{_bindir}/gvfs-rename
%attr(755,root,root) %{_bindir}/gvfs-rm
%attr(755,root,root) %{_bindir}/gvfs-save
%attr(755,root,root) %{_bindir}/gvfs-set-attribute
%attr(755,root,root) %{_bindir}/gvfs-trash
%attr(755,root,root) %{_bindir}/gvfs-tree
%attr(755,root,root) %{_libdir}/gio/modules/libgioremote-volume-monitor.so
%attr(755,root,root) %{_libdir}/gio/modules/libgvfsdbus.so
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gvfsd
%attr(755,root,root) %{_libexecdir}/gvfsd-burn
%{?with_cdda:%attr(755,root,root) %{_libexecdir}/gvfsd-cdda}
%attr(755,root,root) %{_libexecdir}/gvfsd-computer
%{?with_http:%attr(755,root,root) %{_libexecdir}/gvfsd-dav}
%{?with_avahi:%attr(755,root,root) %{_libexecdir}/gvfsd-dnssd}
%attr(755,root,root) %{_libexecdir}/gvfsd-ftp
%{?with_http:%attr(755,root,root) %{_libexecdir}/gvfsd-http}
%attr(755,root,root) %{_libexecdir}/gvfsd-localtest
%attr(755,root,root) %{_libexecdir}/gvfsd-metadata
%attr(755,root,root) %{_libexecdir}/gvfsd-network
%{?with_obexftp:%attr(755,root,root) %{_libexecdir}/gvfsd-obexftp}
%{?with_gtk:%attr(755,root,root) %{_libexecdir}/gvfsd-recent}
%attr(755,root,root) %{_libexecdir}/gvfsd-sftp
%attr(755,root,root) %{_libexecdir}/gvfsd-trash
%{?with_udisks2:%attr(755,root,root) %{_libexecdir}/gvfs-udisks2-volume-monitor}
%{_datadir}/dbus-1/services/gvfs-daemon.service
%{_datadir}/dbus-1/services/gvfs-metadata.service
%{?with_udisks2:%{_datadir}/dbus-1/services/org.gtk.Private.UDisks2VolumeMonitor.service}
%dir %{_datadir}/gvfs
%dir %{_datadir}/gvfs/mounts
%dir %{_datadir}/gvfs/remote-volume-monitors
%{_datadir}/gvfs/mounts/burn.mount
%{?with_cdda:%{_datadir}/gvfs/mounts/cdda.mount}
%{_datadir}/gvfs/mounts/computer.mount
%{?with_http:%{_datadir}/gvfs/mounts/dav.mount}
%{?with_http:%{_datadir}/gvfs/mounts/dav+sd.mount}
%{?with_avahi:%{_datadir}/gvfs/mounts/dns-sd.mount}
%{_datadir}/gvfs/mounts/ftp.mount
%{?with_http:%{_datadir}/gvfs/mounts/http.mount}
%{_datadir}/gvfs/mounts/localtest.mount
%{_datadir}/gvfs/mounts/network.mount
%{?with_obexftp:%{_datadir}/gvfs/mounts/obexftp.mount}
%{?with_gtk:%{_datadir}/gvfs/mounts/recent.mount}
%{_datadir}/gvfs/mounts/sftp.mount
%{_datadir}/gvfs/mounts/trash.mount
%{?with_udisks2:%{_datadir}/gvfs/remote-volume-monitors/udisks2.monitor}
%{?with_avahi:%{_datadir}/GConf/gsettings/gvfs-dns-sd.convert}
%{?with_avahi:%{_datadir}/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml}
%{_datadir}/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
%{_mandir}/man1/gvfs-*.1*
%{_mandir}/man1/gvfsd.1*
%{_mandir}/man1/gvfsd-metadata.1*
%{_mandir}/man7/gvfs.7*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvfscommon.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvfscommon.so
%{_libdir}/libgvfscommon.la
%{_includedir}/gvfs-client

%files -n bash-completion-gvfs
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/gvfs

%if %{with fuse}
%files fuse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-fuse
%{_mandir}/man1/gvfsd-fuse.1*
%{systemdtmpfilesdir}/gvfsd-fuse-tmpfiles.conf
%endif

%if %{with samba}
%files smb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-smb
%attr(755,root,root) %{_libexecdir}/gvfsd-smb-browse
%{_datadir}/gvfs/mounts/smb-browse.mount
%{_datadir}/gvfs/mounts/smb.mount
%{_datadir}/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
%{_datadir}/GConf/gsettings/gvfs-smb.convert
%endif

%if %{with archive}
%files archive
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-archive
%{_datadir}/gvfs/mounts/archive.mount
%endif

%if %{with gphoto2}
%files gphoto2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-gphoto2-volume-monitor
%attr(755,root,root) %{_libexecdir}/gvfsd-gphoto2
%{_datadir}/dbus-1/services/org.gtk.Private.GPhoto2VolumeMonitor.service
%{_datadir}/gvfs/mounts/gphoto2.mount
%{_datadir}/gvfs/remote-volume-monitors/gphoto2.monitor
%endif

%if %{with afc}
%files afc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-afc-volume-monitor
%attr(755,root,root) %{_libexecdir}/gvfsd-afc
%{_datadir}/dbus-1/services/org.gtk.Private.AfcVolumeMonitor.service
%{_datadir}/gvfs/mounts/afc.mount
%{_datadir}/gvfs/remote-volume-monitors/afc.monitor
%endif

%if %{with afp}
%files afp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-afp
%attr(755,root,root) %{_libexecdir}/gvfsd-afp-browse
%{_datadir}/gvfs/mounts/afp-browse.mount
%{_datadir}/gvfs/mounts/afp.mount
%endif

%if %{with mtp}
%files mtp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-mtp-volume-monitor
%attr(755,root,root) %{_libexecdir}/gvfsd-mtp
%{_datadir}/dbus-1/services/org.gtk.Private.MTPVolumeMonitor.service
%{_datadir}/gvfs/mounts/mtp.mount
%{_datadir}/gvfs/remote-volume-monitors/mtp.monitor
%endif

%if %{with goa}
%files goa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-goa-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.Private.GoaVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/goa.monitor
%endif
