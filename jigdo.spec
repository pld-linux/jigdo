Summary:	jigdo - Jigsaw Download - easy the distribution of very large files
Summary(pl):	jigdo - ³atwa dystrybucja du¿ych plików
Name:		jigdo
Version:	0.6.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://home.in.tum.de/~atterer/${name}/%{name}-%{version}.tar.bz2
URL:		http://home.in.tum.de/~atterer/jigdo/
BuildRequires:	db3-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	w3c-libwww-devel
BuildRequires:	openssl-devel
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
w Internecie, na przyk³ad obrazów CD lub DVD. Latwo¶æ ¶ci±gania
polega tylko na klikniêciu linku w twojej przegl±darce, omijaj±c
problemy jakie niesie hostowanie du¿ych plików administratorom.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure --with-gui
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README THANKS changelog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/
