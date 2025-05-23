#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v26
# autospec commit: 99a7985
#
Name     : Thunar
Version  : 4.20.3
Release  : 65
URL      : https://archive.xfce.org/src/xfce/thunar/4.20/thunar-4.20.3.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/thunar/4.20/thunar-4.20.3.tar.bz2
Summary  : A library to create Thunar extensions
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: Thunar-bin = %{version}-%{release}
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-lib = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}
Requires: Thunar-locales = %{version}-%{release}
Requires: Thunar-man = %{version}-%{release}
Requires: Thunar-services = %{version}-%{release}
Requires: gvfs
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : exiv2-dev
BuildRequires : file
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libexif-dev
BuildRequires : libnotify-dev
BuildRequires : libxfce4util-lib
BuildRequires : libxslt-bin
BuildRequires : pcre-dev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libwnck-1.0)
BuildRequires : pkgconfig(libxfce4kbd-private-3)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(pango)
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/thunar/COPYING)

%package bin
Summary: bin components for the Thunar package.
Group: Binaries
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}
Requires: Thunar-services = %{version}-%{release}

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
Requires: Thunar-lib = %{version}-%{release}
Requires: Thunar-bin = %{version}-%{release}
Requires: Thunar-data = %{version}-%{release}
Provides: Thunar-devel = %{version}-%{release}
Requires: Thunar = %{version}-%{release}

%description dev
dev components for the Thunar package.


%package doc
Summary: doc components for the Thunar package.
Group: Documentation
Requires: Thunar-man = %{version}-%{release}

%description doc
doc components for the Thunar package.


%package lib
Summary: lib components for the Thunar package.
Group: Libraries
Requires: Thunar-data = %{version}-%{release}
Requires: Thunar-license = %{version}-%{release}

%description lib
lib components for the Thunar package.


%package license
Summary: license components for the Thunar package.
Group: Default

%description license
license components for the Thunar package.


%package locales
Summary: locales components for the Thunar package.
Group: Default

%description locales
locales components for the Thunar package.


%package man
Summary: man components for the Thunar package.
Group: Default

%description man
man components for the Thunar package.


%package services
Summary: services components for the Thunar package.
Group: Systemd services
Requires: systemd

%description services
services components for the Thunar package.


%prep
%setup -q -n thunar-4.20.3
cd %{_builddir}/thunar-4.20.3
pushd ..
cp -a thunar-4.20.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747404251
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-introspection
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-introspection
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747404251
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Thunar
cp %{_builddir}/thunar-%{version}/COPYING %{buildroot}/usr/share/package-licenses/Thunar/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/thunar-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/Thunar/86207ea3fdd7e8ef5ea34ca9d12a511dc7272d31 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang thunar
## Remove excluded files
rm -f %{buildroot}*/usr/share/dbus-1/services/org.freedesktop.FileManager1.service
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}

## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/Thunar/thunar-sendto-email
/usr/lib64/Thunar/thunar-sendto-email

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/thunar
/usr/bin/Thunar
/usr/bin/thunar
/usr/bin/thunar-settings

%files data
%defattr(-,root,root,-)
/usr/share/Thunar/sendto/thunar-sendto-email.desktop
/usr/share/applications/thunar-bulk-rename.desktop
/usr/share/applications/thunar-settings.desktop
/usr/share/applications/thunar.desktop
/usr/share/dbus-1/services/org.xfce.FileManager.service
/usr/share/dbus-1/services/org.xfce.Thunar.FileManager1.service
/usr/share/dbus-1/services/org.xfce.Thunar.service
/usr/share/icons/hicolor/128x128/apps/org.xfce.thunar.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.thunar.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/16x16/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-copy.png
/usr/share/icons/hicolor/24x24/stock/navigation/stock_folder-move.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.thunar.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.thunar.svg
/usr/share/metainfo/org.xfce.thunar.appdata.xml
/usr/share/polkit-1/actions/org.xfce.thunar.policy
/usr/share/xdg/Thunar/uca.xml
/usr/share/xfce4/panel/plugins/thunar-tpa.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/thunarx-3/thunarx/thunarx-config.h
/usr/include/thunarx-3/thunarx/thunarx-file-info.h
/usr/include/thunarx-3/thunarx/thunarx-menu-item.h
/usr/include/thunarx-3/thunarx/thunarx-menu-provider.h
/usr/include/thunarx-3/thunarx/thunarx-menu.h
/usr/include/thunarx-3/thunarx/thunarx-preferences-provider.h
/usr/include/thunarx-3/thunarx/thunarx-property-page-provider.h
/usr/include/thunarx-3/thunarx/thunarx-property-page.h
/usr/include/thunarx-3/thunarx/thunarx-provider-factory.h
/usr/include/thunarx-3/thunarx/thunarx-provider-module.h
/usr/include/thunarx-3/thunarx/thunarx-provider-plugin.h
/usr/include/thunarx-3/thunarx/thunarx-renamer-provider.h
/usr/include/thunarx-3/thunarx/thunarx-renamer.h
/usr/include/thunarx-3/thunarx/thunarx.h
/usr/lib64/libthunarx-3.so
/usr/lib64/pkgconfig/thunarx-3.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/thunar/README.gtkrc
/usr/share/gtk-doc/html/thunar/ThunarAbstractDialog.html
/usr/share/gtk-doc/html/thunar/ThunarAbstractIconView.html
/usr/share/gtk-doc/html/thunar/ThunarActionManager.html
/usr/share/gtk-doc/html/thunar/ThunarApplication.html
/usr/share/gtk-doc/html/thunar/ThunarBrowser.html
/usr/share/gtk-doc/html/thunar/ThunarChooserButton.html
/usr/share/gtk-doc/html/thunar/ThunarChooserDialog.html
/usr/share/gtk-doc/html/thunar/ThunarChooserModel.html
/usr/share/gtk-doc/html/thunar/ThunarClipboardManager.html
/usr/share/gtk-doc/html/thunar/ThunarColumnEditor.html
/usr/share/gtk-doc/html/thunar/ThunarColumnModel.html
/usr/share/gtk-doc/html/thunar/ThunarCompactView.html
/usr/share/gtk-doc/html/thunar/ThunarComponent.html
/usr/share/gtk-doc/html/thunar/ThunarDBusService.html
/usr/share/gtk-doc/html/thunar/ThunarDeepCountJob.html
/usr/share/gtk-doc/html/thunar/ThunarDetailsView.html
/usr/share/gtk-doc/html/thunar/ThunarDevice.html
/usr/share/gtk-doc/html/thunar/ThunarDeviceMonitor.html
/usr/share/gtk-doc/html/thunar/ThunarEmblemChooser.html
/usr/share/gtk-doc/html/thunar/ThunarFile.html
/usr/share/gtk-doc/html/thunar/ThunarFolder.html
/usr/share/gtk-doc/html/thunar/ThunarHistory.html
/usr/share/gtk-doc/html/thunar/ThunarIconFactory.html
/usr/share/gtk-doc/html/thunar/ThunarIconRenderer.html
/usr/share/gtk-doc/html/thunar/ThunarIconView.html
/usr/share/gtk-doc/html/thunar/ThunarImage.html
/usr/share/gtk-doc/html/thunar/ThunarJob.html
/usr/share/gtk-doc/html/thunar/ThunarJobOperation.html
/usr/share/gtk-doc/html/thunar/ThunarJobOperationHistory.html
/usr/share/gtk-doc/html/thunar/ThunarListModel.html
/usr/share/gtk-doc/html/thunar/ThunarLocationBar.html
/usr/share/gtk-doc/html/thunar/ThunarLocationButton.html
/usr/share/gtk-doc/html/thunar/ThunarLocationButtons.html
/usr/share/gtk-doc/html/thunar/ThunarLocationEntry.html
/usr/share/gtk-doc/html/thunar/ThunarMenu.html
/usr/share/gtk-doc/html/thunar/ThunarNavigator.html
/usr/share/gtk-doc/html/thunar/ThunarPathEntry.html
/usr/share/gtk-doc/html/thunar/ThunarPermissionsChooser.html
/usr/share/gtk-doc/html/thunar/ThunarPreferences.html
/usr/share/gtk-doc/html/thunar/ThunarPreferencesDialog.html
/usr/share/gtk-doc/html/thunar/ThunarProgressDialog.html
/usr/share/gtk-doc/html/thunar/ThunarProgressView.html
/usr/share/gtk-doc/html/thunar/ThunarPropertiesDialog.html
/usr/share/gtk-doc/html/thunar/ThunarRenamerDialog.html
/usr/share/gtk-doc/html/thunar/ThunarRenamerModel.html
/usr/share/gtk-doc/html/thunar/ThunarRenamerProgress.html
/usr/share/gtk-doc/html/thunar/ThunarSendtoModel.html
/usr/share/gtk-doc/html/thunar/ThunarSessionClient.html
/usr/share/gtk-doc/html/thunar/ThunarShortcutsIconRenderer.html
/usr/share/gtk-doc/html/thunar/ThunarShortcutsModel.html
/usr/share/gtk-doc/html/thunar/ThunarShortcutsPane.html
/usr/share/gtk-doc/html/thunar/ThunarShortcutsView.html
/usr/share/gtk-doc/html/thunar/ThunarSidePane.html
/usr/share/gtk-doc/html/thunar/ThunarSimpleJob.html
/usr/share/gtk-doc/html/thunar/ThunarSizeLabel.html
/usr/share/gtk-doc/html/thunar/ThunarStandardView.html
/usr/share/gtk-doc/html/thunar/ThunarStatusbar.html
/usr/share/gtk-doc/html/thunar/ThunarTransferJob.html
/usr/share/gtk-doc/html/thunar/ThunarTreeModel.html
/usr/share/gtk-doc/html/thunar/ThunarTreePane.html
/usr/share/gtk-doc/html/thunar/ThunarTreeView.html
/usr/share/gtk-doc/html/thunar/ThunarUserManager.html
/usr/share/gtk-doc/html/thunar/ThunarView.html
/usr/share/gtk-doc/html/thunar/ThunarWindow.html
/usr/share/gtk-doc/html/thunar/annotation-glossary.html
/usr/share/gtk-doc/html/thunar/ch01.html
/usr/share/gtk-doc/html/thunar/ch02.html
/usr/share/gtk-doc/html/thunar/ch03.html
/usr/share/gtk-doc/html/thunar/ch04.html
/usr/share/gtk-doc/html/thunar/ch05.html
/usr/share/gtk-doc/html/thunar/ch06.html
/usr/share/gtk-doc/html/thunar/ch07.html
/usr/share/gtk-doc/html/thunar/ch08.html
/usr/share/gtk-doc/html/thunar/ch09.html
/usr/share/gtk-doc/html/thunar/ch10.html
/usr/share/gtk-doc/html/thunar/ch11.html
/usr/share/gtk-doc/html/thunar/ch12.html
/usr/share/gtk-doc/html/thunar/ch13.html
/usr/share/gtk-doc/html/thunar/ch14.html
/usr/share/gtk-doc/html/thunar/ch15.html
/usr/share/gtk-doc/html/thunar/ch16.html
/usr/share/gtk-doc/html/thunar/ch17.html
/usr/share/gtk-doc/html/thunar/ch18.html
/usr/share/gtk-doc/html/thunar/ch19.html
/usr/share/gtk-doc/html/thunar/glib-gtk-extensions.html
/usr/share/gtk-doc/html/thunar/home.png
/usr/share/gtk-doc/html/thunar/index.html
/usr/share/gtk-doc/html/thunar/left-insensitive.png
/usr/share/gtk-doc/html/thunar/left.png
/usr/share/gtk-doc/html/thunar/right-insensitive.png
/usr/share/gtk-doc/html/thunar/right.png
/usr/share/gtk-doc/html/thunar/style.css
/usr/share/gtk-doc/html/thunar/thunar-objects.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-dialogs.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-dnd.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-enum-types.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-gdk-extensions.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-gio-extensions.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-gobject-extensions.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-gtk-extensions.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-ice.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-io-jobs-util.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-io-jobs.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-io-scan-directory.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-notify.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-pango-extensions.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-renamer-pair.html
/usr/share/gtk-doc/html/thunar/thunar-thunar-util.html
/usr/share/gtk-doc/html/thunar/thunar-view.html
/usr/share/gtk-doc/html/thunar/thunar-widgets.html
/usr/share/gtk-doc/html/thunar/thunar.devhelp2
/usr/share/gtk-doc/html/thunar/up-insensitive.png
/usr/share/gtk-doc/html/thunar/up.png
/usr/share/gtk-doc/html/thunarx/ThunarxFileInfo.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenu.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenuItem.html
/usr/share/gtk-doc/html/thunarx/ThunarxMenuProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxPreferencesProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxPropertyPage.html
/usr/share/gtk-doc/html/thunarx/ThunarxPropertyPageProvider.html
/usr/share/gtk-doc/html/thunarx/ThunarxProviderFactory.html
/usr/share/gtk-doc/html/thunarx/ThunarxProviderPlugin.html
/usr/share/gtk-doc/html/thunarx/ThunarxRenamer.html
/usr/share/gtk-doc/html/thunarx/ThunarxRenamerProvider.html
/usr/share/gtk-doc/html/thunarx/abstraction.png
/usr/share/gtk-doc/html/thunarx/annotation-glossary.html
/usr/share/gtk-doc/html/thunarx/bulk-rename.png
/usr/share/gtk-doc/html/thunarx/home.png
/usr/share/gtk-doc/html/thunarx/index.html
/usr/share/gtk-doc/html/thunarx/ix01.html
/usr/share/gtk-doc/html/thunarx/left-insensitive.png
/usr/share/gtk-doc/html/thunarx/left.png
/usr/share/gtk-doc/html/thunarx/menu-provider.png
/usr/share/gtk-doc/html/thunarx/right-insensitive.png
/usr/share/gtk-doc/html/thunarx/right.png
/usr/share/gtk-doc/html/thunarx/say-hello.png
/usr/share/gtk-doc/html/thunarx/style.css
/usr/share/gtk-doc/html/thunarx/thunarx-Variables-and-functions-to-check-the-library-version.html
/usr/share/gtk-doc/html/thunarx/thunarx-abstraction-layer.html
/usr/share/gtk-doc/html/thunarx/thunarx-fundamentals.html
/usr/share/gtk-doc/html/thunarx/thunarx-overview.html
/usr/share/gtk-doc/html/thunarx/thunarx-providers.html
/usr/share/gtk-doc/html/thunarx/thunarx-using-extensions.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions-advanced-topics.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions-getting-started.html
/usr/share/gtk-doc/html/thunarx/thunarx-writing-extensions.html
/usr/share/gtk-doc/html/thunarx/thunarx.devhelp2
/usr/share/gtk-doc/html/thunarx/up-insensitive.png
/usr/share/gtk-doc/html/thunarx/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libthunarx-3.so.0.0.0
/V3/usr/lib64/thunarx-3/thunar-apr.so
/V3/usr/lib64/thunarx-3/thunar-sbr.so
/V3/usr/lib64/thunarx-3/thunar-uca.so
/V3/usr/lib64/thunarx-3/thunar-wallpaper-plugin.so
/V3/usr/lib64/xfce4/panel/plugins/libthunar-tpa.so
/usr/lib64/libthunarx-3.so.0
/usr/lib64/libthunarx-3.so.0.0.0
/usr/lib64/thunarx-3/thunar-apr.so
/usr/lib64/thunarx-3/thunar-sbr.so
/usr/lib64/thunarx-3/thunar-uca.so
/usr/lib64/thunarx-3/thunar-wallpaper-plugin.so
/usr/lib64/xfce4/panel/plugins/libthunar-tpa.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Thunar/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/Thunar/86207ea3fdd7e8ef5ea34ca9d12a511dc7272d31

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Thunar.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/thunar.service

%files locales -f thunar.lang
%defattr(-,root,root,-)

