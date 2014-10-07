#
# Conditional build:
%bcond_without	doc	# docs building and packaging
%bcond_without	afc	# AFC backend
%bcond_without	afp	# AFP support
%bcond_without	archive	# archive support
%bcond_without	avahi	# DNS-SD / Avahi support
%bcond_without	bluray	# bluray metadata support
%bcond_without	cdda	# CDDA backend
%bcond_without	fuse	# FUSE support
%bcond_without	goa	# GOA backend
%bcond_with	gdu	# GDU (Gnome Disk Utility) volume monitor (3.0.2 <= v < 3.4)
%bcond_without	gphoto2	# gphoto2 support
%bcond_without	gtk	# GTK+
%bcond_without	gudev	# gudev support (if disabled, HAL could be used)
%bcond_without	http	# HTTP/DAV backend
%bcond_without	keyring	# GNOME Keyring support in gvfs and udisks plugin
%bcond_without	mtp	# MTP support
%bcond_without	obexftp	# ObexFTP backend
%bcond_without	samba	# SMB support
%bcond_without	systemd	# libsystemd-login support
%bcond_without	udev	# udev support (needed also for gphoto2, mtp, udisks2)
%bcond_without	udisks2	# libudisks2 support

%if %{without gudev}
%undefine	with_gphoto2
%undefine	with_mtp
%undefine	with_udisks2
%endif

%ifarch s390 s390x
%undefine	with_afc
%endif

Summary:	gvfs - userspace virtual filesystem
Summary(pl.UTF-8):	gvfs - wirtualny system plików w przestrzeni użytkownika
Name:		gvfs
Version:	1.22.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/1.22/%{name}-%{version}.tar.xz
# Source0-md5:	065fc9a1e2169ec224fa2c752aeefa37
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
%{?with_doc:BuildRequires:	docbook-dtd42-xml}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_obexftp:BuildRequires:	expat-devel >= 1.95}
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.38.0
%{?with_gdu:BuildRequires:	gnome-disk-utility-devel < 3.4}
%{?with_gdu:BuildRequires:	gnome-disk-utility-devel >= 3.0.2}
%{?with_goa:BuildRequires:	gnome-online-accounts-devel >= 3.8.0}
%{?with_gtk:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	intltool >= 0.40.0
%{?with_archive:BuildRequires:	libarchive-devel >= 3.0.22}
%{?with_bluray:BuildRequires:	libbluray-devel}
%{?with_cdda:BuildRequires:	libcdio-paranoia-devel >= 0.78.2}
%{?with_fuse:BuildRequires:	libfuse-devel >= 2.8.0}
BuildRequires:	libgcrypt-devel >= 1.2.2
%{?with_gphoto2:BuildRequires:	libgphoto2-devel >= 2.5.0}
%{?with_afc:BuildRequires:	libimobiledevice-devel >= 1.1.5}
%{?with_mtp:BuildRequires:	libmtp-devel >= 1.1.6}
%{?with_afc:BuildRequires:	libplist-devel >= 0.15}
%{?with_keyring:BuildRequires:	libsecret-devel}
%{?with_samba:BuildRequires:	libsmbclient-devel >= 3.4}
%{?with_http:BuildRequires:	libsoup-devel >= 2.42.0}
BuildRequires:	libtool >= 2:2.2
%{?with_http:BuildRequires:	libxml2-devel >= 1:2.6.31}
%{?with_doc:BuildRequires:	libxslt-progs}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
%{?with_systemd:BuildRequires:	systemd-devel >= 44}
BuildRequires:	tar >= 1:1.22
%{?with_udev:BuildRequires:	udev-devel >= 1:138}
%{?with_gudev:BuildRequires:	udev-glib-devel >= 1:147}
%{?with_udisks2:BuildRequires:	udisks2-devel >= 1.97.0}
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
%{?with_avahi:Requires:	avahi-glib >= 0.6.22}
%{?with_cdda:Requires:	cdparanoia-III-libs >= 1:10}
%{?with_cdda:Requires:	libcdio-paranoia >= 0.78.2}
Requires:	libplist >= 0.15
Requires:	libsoup >= 2.42.0
Requires:	libxml2 >= 1:2.6.31
%{?with_gudev:Requires:	udev-glib >= 1:147}
%{?with_udev:Requires:	udev-libs >= 1:138}
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
Obsoletes:	gvfs-libs < 1.20.0
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
gfvs-a do wszystkich aplikacji używających API gio.

%package devel
Summary:	Header files for gvfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gvfs
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.38.0

%description devel
Header files for gvfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gvfs.

%package afc
Summary:	AFC support for gvfs
Summary(pl.UTF-8):	Obsługa AFC dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libimobiledevice >= 1.1.5
Requires:	usbmuxd

%description afc
This package provides support for reading files on mobile devices
including phones and music players to applications using gvfs.

%description afc -l pl.UTF-8
Ten pakiet zapewnia obsługę odczytu plików na urządzeniach
przenośnych, w tym telefonach i odtwarzaczach muzyki dla aplikacji
wykorzystujących gvfs.

%package afp
Summary:	AFP support for gvfs
Summary(pl.UTF-8):	Obsługa AFP dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description afp
This package provides support for reading and writing files on Mac OS
X and original Mac OS network shares via Apple Filing Protocol to
applications using gvfs.

%description afp -l pl.UTF-8
Ten pakiet zapewnia obsługę odczytu i zapisu plików na udziałach
sieciowych Mac OS X oraz oryginalnego Mac OS poprzez Apple Filing
Protocol dla aplikacji wykorzystujących gvfs.

%package archive
Summary:	Archiving support for gvfs
Summary(pl.UTF-8):	Obsługa archiwów dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libarchive >= 3.0.22

%description archive
This package provides support for accessing files inside Zip and Tar
archives, as well as ISO images, to applications using gvfs.

%description archive -l pl.UTF-8
Ten pakiet zapewnia dostęp do plików wewnątrz archiwów Zip i Tar oraz
obrazów ISO dla aplikacji wykorzystujących gvfs.

%package fuse
Summary:	FUSE support for gvfs
Summary(pl.UTF-8):	Obsługa FUSE dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libfuse

%description fuse
This package provides support for applications not using gio to access
the gvfs filesystems.

%description fuse -l pl.UTF-8
Ten pakiet zapewnia obsługę aplikacji nie używających gio do dostępu
do systemów plików gvfs.

%package goa
Summary:	GOA support for gvfs
Summary(pl.UTF-8):	Obsługa GOA dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-online-accounts-libs >= 3.8.0

%description goa
This package provides seamless integration with gnome-online-accounts
file services.

%description goa -l pl.UTF-8
Ten pakiet zapewnia przezroczystą integrację z usługami plikowymi
gnome-online-accounts.

%package gphoto2
Summary:	gphoto2 support for gvfs
Summary(pl.UTF-8):	Obsługa gphoto2 dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gphoto2
This package provides support for reading and writing files on PTP
based cameras (Picture Transfer Protocol) and MTP based media players
(Media Transfer Protocol) to applications using gvfs.

%description gphoto2 -l pl.UTF-8
Ten pakiet zapewnia obsługę odczytu i zapisu plików na aparatach
obsługujących protokół PTP (Picture Transfer Protocol) oraz
odtwarzaczach multimedialnych obsługujących protokół MTP (Media
Transfer Protocol) dla aplikacji wykorzystujących gvfs.

%package mtp
Summary:	MTP support for gvfs
Summary(pl.UTF-8):	Obsługa MTP dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmtp >= 1.1.6

%description mtp
This package provides support for reading and writing files on MTP
based devices (Media Transfer Protocol) to applications using gvfs.

%description mtp -l pl.UTF-8
Ten pakiet zapewnia obsługę odczytu i zapisu plików na urządzeniach
obsługujących protokół MTP (Media Transfer Protocol) dla aplikacji
wykorzystujących gvfs.

%package smb
Summary:	Windows fileshare support for gvfs
Summary(pl.UTF-8):	Obsługa udziałów sieciowych Windows dla gvfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description smb
This package provides support for reading and writing files on Windows
shares (SMB) to applications using gvfs.

%description smb -l pl.UTF-8
Ten pakiet zapewnia obsługę odczytu i zapisu plików na udziałach
sieciowych Windows (SMB) dla aplikacji wykorzystujących gvfs.

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
	%{__enable_disable doc documentation} \
	%{__enable_disable fuse} \
	%{__enable_disable gdu} \
	%{__enable_disable goa} \
	%{__enable_disable gphoto2} \
	%{__enable_disable gtk} \
	%{__enable_disable gudev} \
	%{__enable_disable http} \
	%{__enable_disable keyring} \
	%{__enable_disable mtp libmtp} \
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{gio/modules,gvfs}/*.la

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

# Reload .mount files when single subpackage is installed:
%post afc
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post archive
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post goa
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post gphoto2
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post mtp
killall -USR1 gvfsd >/dev/null 2>&1 || :

%post smb
%glib_compile_schemas
killall -USR1 gvfsd >/dev/null 2>&1 || :

%postun smb
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

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
%attr(755,root,root) %{_libexecdir}/gvfsd-computer
%attr(755,root,root) %{_libexecdir}/gvfsd-ftp
%attr(755,root,root) %{_libexecdir}/gvfsd-localtest
%attr(755,root,root) %{_libexecdir}/gvfsd-metadata
%attr(755,root,root) %{_libexecdir}/gvfsd-network
%attr(755,root,root) %{_libexecdir}/gvfsd-sftp
%attr(755,root,root) %{_libexecdir}/gvfsd-trash
%attr(755,root,root) %{_libexecdir}/libgvfscommon.so
%attr(755,root,root) %{_libexecdir}/libgvfsdaemon.so
%{_datadir}/dbus-1/services/gvfs-daemon.service
%{_datadir}/dbus-1/services/gvfs-metadata.service
%dir %{_datadir}/gvfs
%dir %{_datadir}/gvfs/mounts
%dir %{_datadir}/gvfs/remote-volume-monitors
%{_datadir}/gvfs/mounts/burn.mount
%{_datadir}/gvfs/mounts/computer.mount
%{_datadir}/gvfs/mounts/ftp.mount
%{_datadir}/gvfs/mounts/localtest.mount
%{_datadir}/gvfs/mounts/network.mount
%{_datadir}/gvfs/mounts/sftp.mount
%{_datadir}/gvfs/mounts/trash.mount
%{_datadir}/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml

# cdda
%if %{with cdda}
%attr(755,root,root) %{_libexecdir}/gvfsd-cdda
%{_datadir}/gvfs/mounts/cdda.mount
%endif

# http
%if %{with http}
%attr(755,root,root) %{_libexecdir}/gvfsd-dav
%attr(755,root,root) %{_libexecdir}/gvfsd-http
%{_datadir}/gvfs/mounts/http.mount
%{_datadir}/gvfs/mounts/dav.mount
%{?with_avahi:%{_datadir}/gvfs/mounts/dav+sd.mount}
%endif

# obexftp
%if %{with obexftp}
%attr(755,root,root) %{_libexecdir}/gvfsd-obexftp
%{_datadir}/gvfs/mounts/obexftp.mount
%endif

# gtk
%if %{with gtk}
%attr(755,root,root) %{_libexecdir}/gvfsd-recent
%{_datadir}/gvfs/mounts/recent.mount
%endif

# udisks2
%if %{with udisks2}
%attr(755,root,root) %{_libexecdir}/gvfs-udisks2-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.Private.UDisks2VolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/udisks2.monitor
%endif

# avahi
%if %{with avahi}
%attr(755,root,root) %{_libexecdir}/gvfsd-dnssd
%{_datadir}/gvfs/mounts/dns-sd.mount
%{_datadir}/GConf/gsettings/gvfs-dns-sd.convert
%{_datadir}/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
%endif

%if %{with doc}
%{_mandir}/man1/gvfs-*.1*
%{_mandir}/man1/gvfsd.1*
%{_mandir}/man1/gvfsd-metadata.1*
%{_mandir}/man7/gvfs.7*
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/gvfs-client

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

%if %{with archive}
%files archive
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-archive
%{_datadir}/gvfs/mounts/archive.mount
%endif

%if %{with fuse}
%files fuse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfsd-fuse
%if %{with doc}
%{_mandir}/man1/gvfsd-fuse.1*
%endif
%if %{with systemd}
# FIXME: reusing USE_LIBSYSTEMD_LOGIN as systemd has no universal header or pkg-config file
%{systemdtmpfilesdir}/gvfsd-fuse-tmpfiles.conf
%endif
%endif

%if %{with goa}
%files goa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-goa-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.Private.GoaVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/goa.monitor
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

%if %{with mtp}
%files mtp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gvfs-mtp-volume-monitor
%attr(755,root,root) %{_libexecdir}/gvfsd-mtp
%{_datadir}/dbus-1/services/org.gtk.Private.MTPVolumeMonitor.service
%{_datadir}/gvfs/mounts/mtp.mount
%{_datadir}/gvfs/remote-volume-monitors/mtp.monitor
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

%files -n bash-completion-gvfs
%defattr(644,root,root,755)
%{bash_compdir}/gvfs
