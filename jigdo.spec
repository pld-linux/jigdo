Summary:	jigdo
Summary(pl):	jigdo
Name:		jigdo
Version:	0.6.9
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://home.in.tum.de/~atterer/${name}/%{name}-%{version}.tar.bz2
URL:		http://home.in.tum.de/~atterer/jigdo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS changelog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
