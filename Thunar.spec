#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Thunar
Version  : 1.6.12
Release  : 22
URL      : http://archive.xfce.org/src/xfce/thunar/1.6/Thunar-1.6.12.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/thunar/1.6/Thunar-1.6.12.tar.bz2
Summary  : A library to create Thunar extensions
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: Thunar-bin
Requires: Thunar-lib
Requires: Thunar-data
Requires: Thunar-doc
Requires: Thunar-locales
BuildRequires : intltool
BuildRequires : libxfce4util-lib
BuildRequires : pcre-dev
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(exo-1)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwnck-1.0)
BuildRequires : pkgconfig(libxfce4panel-1.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(sm)
BuildRequires : sed
Patch1: 0001-Do-not-display-condescending-root-warning.patch

%description
What is it?
===========
Thunar is a modern file manager for the Unix/Linux desktop, aiming to be
easy-to-use and fast.

%package bin
Summary: bin components for the Thunar package.
Group: Binaries
Requires: Thunar-data

%description bin
bin components for the Thunar package.


%package data
Summary: data components for the Thunar package.
Group: Data

%description data
data components for the Thunar package.


%package dev
Summary: dev components for the Thunar package.
Group: Development
Requires: Thunar-lib
Requires: Thunar-bin
Requires: Thunar-data
Provides: Thunar-devel

%description dev
dev components for the Thunar package.


%package doc
Summary: doc components for the Thunar package.
Group: Documentation

%description doc
doc components for the Thunar package.


%package lib
Summary: lib components for the Thunar package.
Group: Libraries
Requires: Thunar-data

%description lib
lib components for the Thunar package.


%package locales
Summary: locales components for the Thunar package.
Group: Default

%description locales
locales components for the Thunar package.


%prep
%setup -q -n Thunar-1.6.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1498890265
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1498890265
rm -rf %{buildroot}
%make_install
%find_lang Thunar
## make_install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/Thunar/ThunarBulkRename
/usr/lib64/Thunar/thunar-sendto-email

%files bin
%defattr(-,root,root,-)
/usr/bin/Thunar
/usr/bin/thunar
/usr/bin/thunar-settings

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/thunar-sendto-email.desktop
/usr/share/appdata/thunar.appdata.xml
/usr/share/applications/Thunar-bulk-rename.desktop
/usr/share/applications/Thunar-folder-handler.desktop
/usr/share/applications/Thunar.desktop
/usr/share/applications/thunar-settings.desktop
/usr/share/dbus-1/services/org.xfce.FileManager.service
/usr/share/dbus-1/services/org.xfce.Thunar.service
/usr/share/icons/hicolor/128x128/apps/Thunar.png
/usr/share/icons/hicolor/16x16/apps/Thunar.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_thunar-shortcuts.png
/usr/share/icons/hicolor/24x24/apps/Thunar.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/48x48/apps/Thunar.png
/usr/share/icons/hicolor/64x64/apps/Thunar.png
/usr/share/icons/hicolor/scalable/apps/Thunar.svg
/usr/share/pixmaps/Thunar/Thunar-about-logo.png
/usr/share/polkit-1/actions/org.xfce.thunar.policy
/usr/share/xdg/Thunar/uca.xml
/usr/share/xfce4/panel/plugins/thunar-tpa.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/thunarx-2/thunarx/thunarx-config.h
/usr/include/thunarx-2/thunarx/thunarx-file-info.h
/usr/include/thunarx-2/thunarx/thunarx-menu-provider.h
/usr/include/thunarx-2/thunarx/thunarx-preferences-provider.h
/usr/include/thunarx-2/thunarx/thunarx-property-page-provider.h
/usr/include/thunarx-2/thunarx/thunarx-property-page.h
/usr/include/thunarx-2/thunarx/thunarx-provider-factory.h
/usr/include/thunarx-2/thunarx/thunarx-provider-plugin.h
/usr/include/thunarx-2/thunarx/thunarx-renamer-provider.h
/usr/include/thunarx-2/thunarx/thunarx-renamer.h
/usr/include/thunarx-2/thunarx/thunarx.h
/usr/lib64/libthunarx-2.so
/usr/lib64/pkgconfig/thunarx-2.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/Thunar/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libthunarx-2.so.0
/usr/lib64/libthunarx-2.so.0.0.0
/usr/lib64/thunarx-2/thunar-apr.so
/usr/lib64/thunarx-2/thunar-sbr.so
/usr/lib64/thunarx-2/thunar-uca.so
/usr/lib64/thunarx-2/thunar-wallpaper-plugin.so
/usr/lib64/xfce4/panel/plugins/libthunar-tpa.so

%files locales -f Thunar.lang
%defattr(-,root,root,-)

