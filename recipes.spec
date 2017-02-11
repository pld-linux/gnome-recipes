Summary:	A GNOME cookbook
Summary(pl.UTF-8):	Książka kucharska GNOME
Name:		recipes
Version:	0.10.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/recipes/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	4dfc5fe85d4a3d8d8df560878b2d0284
URL:		https://wiki.gnome.org/Apps/Recipes
BuildRequires:	appstream-glib
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
# C11 (-std=gnu11)
BuildRequires:	gcc >= 6:4.7
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gnome-autoar-devel
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gspell-devel
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	json-glib-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun): gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+3 >= 3.20.0
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

%build
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/recipes/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/recipes
%dir %{_libdir}/recipes
%attr(755,root,root) %{_libdir}/recipes/libgd.so
%{_datadir}/appdata/org.gnome.Recipes.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Recipes.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Recipes-search-provider.ini
%{_datadir}/recipes
%{_desktopdir}/org.gnome.Recipes.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Recipes*.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Recipes-symbolic.svg
