Summary:	SilverXP theme for IceWM
Summary(pl.UTF-8):   Motyw SilverXP dla IceWM-a
Name:		icewm-themes-xp-silver
Version:	1.2.17
%define	_verrel 1
Release:	1
License:	GPL (?)
Group:		Themes
Source0:	http://dl.sourceforge.net/icewmsilverxp/SilverXP-%{version}-double-%{_verrel}.tar.bz2
# Source0-md5:	b3dece94b234145093b766d7eaa38776
Requires:	icewm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/share/icewm/themes

%description
The IceWM SilverXP Theme was inspired by the Microsoft Windows XP
Silver Theme. The title bars and window borders have the look of
Windows XP. The colors of all elements are very similar to the colors
of the Windows XP interface.

%description -l pl.UTF-8
Motyw SilverXP dla IceWM-a został zainspirowany motywem XP Silver dla
systemu Microsoft Windows XP. Paski tytułowe, kolory i obramowania
okien wyglądają i zachowują się jak te w Windowsie XP.

%prep
%setup -q -n icewm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}/silverxp

cp -R themes/SilverXP-%{version}-double-%{_verrel}/*.xpm $RPM_BUILD_ROOT%{_themesdir}/silverxp
cp -R themes/SilverXP-%{version}-double-%{_verrel}/*.theme $RPM_BUILD_ROOT%{_themesdir}/silverxp
cp -R themes/SilverXP-%{version}-double-%{_verrel}/icons $RPM_BUILD_ROOT%{_themesdir}/silverxp
cp -R themes/SilverXP-%{version}-double-%{_verrel}/taskbar $RPM_BUILD_ROOT%{_themesdir}/silverxp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
