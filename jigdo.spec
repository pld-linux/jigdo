Summary:	jigdo - Jigsaw Download - easy the distribution of very large files
Summary(pl):	jigdo - ³atwa dystrybucja du¿ych plików
Name:		jigdo
Version:	0.7.3
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://atterer.net/jigdo/%{name}-%{version}.tar.bz2
# Source0-md5:	bbc1d9ac750bb34e0748f0b57157cc72
URL:		http://atterer.net/jigdo/
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.11
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jigsaw Download, or short jigdo, is a tool designed to ease the
distribution of very large files over the internet, for example CD or
DVD images. Its aim is to make downloading the images as easy for
users as a click on a direct download link in a browser, while
avoiding all the problems that server administrators have with hosting
such large files.

%description -l pl
jigdo to narzêdzie do ³atwej dystrybucji bardzo du¿ych plików
w Internecie, na przyk³ad obrazów CD lub DVD. £atwo¶æ ¶ci±gania
polega tylko na klikniêciu odno¶nika w przegl±darce, omijaj±c
problemy jakie niesie hostowanie du¿ych plików administratorom.

%package gtk
Summary:	GTK+2 based download manager
Summary(pl):	Zarz±dca pobierania oparty na GTK+2
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
Provides GTK+2 based download manager. 

%description gtk -l pl
Pakiet zawiera zarz±dcê pobierania, opartego na GTK+2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-gui
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README THANKS changelog
%attr(755,root,root) %{_bindir}/jigdo-*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/debian-mirrors.jigdo
%{_mandir}/man1/jigdo-*.1*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jigdo
%{_datadir}/%{name}/pixmaps
%{_mandir}/man1/jigdo.1*
