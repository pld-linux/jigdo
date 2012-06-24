Summary:	jigdo - Jigsaw Download - easy the distribution of very large files
Summary(pl):	jigdo - �atwa dystrybucja du�ych plik�w
Name:		jigdo
Version:	0.6.9
Release:	0.2
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
jigdo to narz�dzie do �atwej dystrybucji bardzo du�ych plik�w
w Internecie, na przyk�ad obraz�w CD lub DVD. Latwo�� �ci�gania
polega tylko na klikni�ciu linku w twojej przegl�darce, omijaj�c
problemy jakie niesie obs�uga du�ych plik�w biednym administratorom.

%prep
%setup -q

%build
#rm -f missing
#%{__libtoolize}
#%{__gettextize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS changelog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/
