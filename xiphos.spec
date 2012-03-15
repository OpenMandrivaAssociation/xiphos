%define name	xiphos
%define version 3.1.5
%define release 1

Summary:	Bible Study Software for Linux and the Gnome Desktop
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://dfn.dl.sourceforge.net/sourceforge/gnomesword/%{name}-%{version}.tar.gz
Patch0:		xiphos-3.1.3-gtkhtml.patch
URL:		http://xiphos.org/
License:	GPLv2+
Group:		Text tools
BuildRequires:  gtkhtml-3.14-devel
BuildRequires:	pkgconfig(libgnomeui-2.0) libgnomeprintui-devel
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	aspell-devel sword-devel >= 1.5.11 pkgconfig(ImageMagick)
BuildRequires:  perl-XML-Parser
BuildRequires:  scrollkeeper
BuildRequires:  pkgconfig(webkitgtk-3.0)
BuildRequires:  gnome-doc-utils desktop-file-utils
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	libgsf-1-devel
Requires: 	sword >= 1.5.11
Obsoletes:	gnomesword < 2.4.1-2
Provides:	gnomesword

%description
GnomeSword is a GNOME interface to the Sword Project 
(http://www.croswire.org/sword)

The SWORD Bible Framework allows easy manipulation of Bible texts, 
commentaries, lexicons, dictionaries, etc.

%prep
%setup -q

%build
./waf configure --prefix=%{buildroot}/usr --gtk=auto --debug-level=optimized
#%  configure2_5x --without-gecko
./waf build

%install
./waf install

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications/ \
	--remove-key='Encoding' \
	--remove-key='MultipleArgs' \
	--remove-category='Application' \
	--remove-category='Utility' \
	--remove-category='X-Red-Hat-Extra' \
	--add-category='GNOME;GTK;Literature;Education' \
	%buildroot%_datadir/applications/*.desktop

mkdir -p $RPM_BUILD_ROOT/{%{_liconsdir},%{_miconsdir}}
install pixmaps/gs2-48x48.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -size 16x16 -resize 16x16 pixmaps/gs2-48x48.png %{buildroot}/%{_miconsdir}/%{name}.png
convert -size 32x32 -resize 32x32 pixmaps/gs2-48x48.png %{buildroot}/%{_iconsdir}/%{name}.png

rm -rf %{buildroot}/%{_docdir}/%{name}

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING INSTALL  NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/xiphos.svg
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/icon-theme.cache
%{_miconsdir}/%{name}.png
