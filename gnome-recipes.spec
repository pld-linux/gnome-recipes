Summary:	A GNOME cookbook
Summary(pl.UTF-8):	Książka kucharska GNOME
Name:		gnome-recipes
Version:	1.2.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-recipes/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	a91a4213f6a99e3ef120be4b5770ad85
#
# Taken from GIT repository:
# $ git clone --recursive git://git.gnome.org/recipes
# $ cd recipes
# $ git checkout tags/1.2.0
# $ tar -cJf gnome-recipes-libgd-1.2.0.tar.xz subprojects/
Source1:	%{name}-libgd-%{version}.tar.xz
# Source1-md5:	91a14eca84ef2f09575237f21e7e6959
URL:		https://wiki.gnome.org/Apps/Recipes
BuildRequires:	appstream-glib
# C11 (-std=gnu11)
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	git-core
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gnome-autoar-devel
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gspell-devel
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	json-glib-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	meson >= 0.36.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.42.0
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Provides:	recipes = %{version}
Obsoletes:	recipes < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Recipes is an easy-to-use application that will help you to
discover what to cook today, tomorrow, rest of the week and for your
special occasions.

Recipes comes with a collection of recipes that have been collected by
GNOME contributors from all over the world. It also lets you store
your own recipes, and share them with your friends.

%description -l pl.UTF-8
Przepisy GNOME to łatwy w obsłudze program pomagający odkrywać
przepisy na dzisiaj, jutro i resztę tygodnia, a także na specjalne
okazje.

Program zawiera kolekcję przepisów zebranych przez współtwórców GNOME
z całego świata. Umożliwia także dodawanie własnych przepisów
i udostępnianie ich znajomym.

%prep
%setup -q -a 1

%build
meson --prefix=%{_prefix} build
ninja -C build

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
ninja -C build install

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md
%attr(755,root,root) %{_bindir}/gnome-recipes
%{_datadir}/appdata/org.gnome.Recipes.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Recipes.service
%{_datadir}/glib-2.0/schemas/org.gnome.Recipes.gschema.xml
%{_datadir}/mime/packages/org.gnome.Recipes-mime.xml
%{_datadir}/gnome-recipes
%{_desktopdir}/org.gnome.Recipes.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Recipes*.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Recipes-symbolic.svg
