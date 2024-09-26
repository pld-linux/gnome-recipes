Summary:	A GNOME cookbook
Summary(pl.UTF-8):	Książka kucharska GNOME
Name:		gnome-recipes
Version:	2.0.4
Release:	2
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-recipes/2.0/%{name}-%{version}.tar.xz
# Source0-md5:	2e854234e88c6320cb167db9bd8270e0
Patch0:		%{name}-warnings.patch
URL:		https://wiki.gnome.org/Apps/Recipes
BuildRequires:	appstream-glib
# C11 (-std=gnu11)
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	git-core
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gnome-autoar-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gspell-devel >= 1
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	json-glib-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	meson >= 0.43.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rest-devel >= 0.7
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.42.0
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Provides:	recipes = %{version}
Obsoletes:	recipes < 0.14
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
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# gnome-recipes, gnome-recipes-data gettext domains
# org.gnome.Recipes help
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
%{_datadir}/dbus-1/services/org.gnome.Recipes.service
%{_datadir}/glib-2.0/schemas/org.gnome.Recipes.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Recipes-search-provider.ini
%{_datadir}/metainfo/org.gnome.Recipes.appdata.xml
%{_datadir}/mime/packages/org.gnome.Recipes-mime.xml
%{_datadir}/gnome-recipes
%{_desktopdir}/org.gnome.Recipes.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Recipes*.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Recipes-symbolic.svg
