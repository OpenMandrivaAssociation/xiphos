%define name	xiphos
%define version 3.1.3
%define release %mkrel 1

Summary:	Bible Study Software for Linux and the Gnome Desktop
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		http://dfn.dl.sourceforge.net/sourceforge/gnomesword/%{name}-%{version}.tar.gz
URL:		http://xiphos.org/
License:	GPLv2+
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gtkhtml-3.14-devel
BuildRequires:	gnomeui2-devel libgnomeprintui-devel
BuildRequires:	libglade2-devel 
BuildRequires:	aspell-devel sword-devel >= 1.5.11 imagemagick
BuildRequires:  perl-XML-Parser
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils desktop-file-utils
BuildRequires:	libmagick-devel
BuildRequires:	intltool
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
%configure2_5x --without-gecko
%make

%install
rm -fr %buildroot
%makeinstall_std

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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL  NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/xiphos.svg
%{_datadir}/omf/xiphos/xiphos-C.omf
%{_datadir}/omf/xiphos/xiphos-fa.omf
%{_datadir}/omf/xiphos/xiphos-fr.omf
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%exclude %{_defaultdocdir}/%{name}
