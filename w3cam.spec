# TODO: webapps or so
Summary:	CGI application to show image retrieved from a webcam
Summary(pl.UTF-8):   Aplikacja CGI do pokazywania obrazu ściągniętego z kamery
Name:		w3cam
Version:	0.7.2
Release:	4
License:	GPL
Group:		Networking/Daemons
Source0:	http://mpx.freeshell.net/%{name}-%{version}.tar.gz
# Source0-md5:	eec0b301b32bc8e9f65a4e54248c9868
Patch0:		%{name}-includes.patch
URL:		http://mpx.freeshell.net/
BuildRequires:	autoconf
BuildRequires:	freetype1-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/home/services/httpd

%description
w3cam is a simple CGI to retrieve images from a so called video4linux
device. In other words this program will only run on Linux machines
which support a video4linux-device.

This CGI works only with Mozilla/Netscape browsers.

%description -l pl.UTF-8
w3cam to proste CGI do ściągania obrazów z tzw. urządzeń video4linux.
Innymi słowy ten program zadziała tylko na Linuksie z obsługą takich
urządzeń.

To CGI działa tylko z przeglądarkami Mozilla/Netscape.

%package -n vidcat
Summary:	Application to grab images from a video4linux device
Summary(pl.UTF-8):   Aplikacja do zrzucania obrazu z urządzeń video4linux
Group:		Applications/Graphics

%description -n vidcat
vidcat is a simple tool to retrieve images from a video4linux device.

%description -n vidcat -l pl.UTF-8
vidcat jest prostym narzędziem do ściągania obrazów z urządzeń
video4linux.

%package -n w3camd
Summary:	Application to show image retrieved from a webcam
Summary(pl.UTF-8):   Aplikacja do pokazywania obrazu ściągniętego z kamery
Group:		Networking/Daemons

%description -n w3camd
w3camd is a standalone daemon which serves images grabbed from a
webcam, just like any HTTP server would do.

It only with Mozilla/Netscape browsers.

%description -n w3camd -l pl.UTF-8
w3camd to samodzielny demon który serwuje obrazy wzięte z kamery
internetowej, tak jak by to robił serwer HTTP.

Działa tylko z przeglądarkami Mozilla/Netscape.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/freetype"
%configure \
	--with-syslog
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/cgi-bin,%{_bindir},%{_sbindir}}

install w3cam.cgi* $RPM_BUILD_ROOT%{_datadir}/cgi-bin
install vidcat $RPM_BUILD_ROOT%{_bindir}
install w3camd/w3camd $RPM_BUILD_ROOT%{_sbindir}
install w3camd/index.html w3camd.html
install w3camd/test.html w3camd-test.html
install index.html w3cam.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt FAQ.txt TODO.txt w3cam.html
%attr(755,root,root) %{_datadir}/cgi-bin/w3cam.cgi
%{_datadir}/cgi-bin/w3cam.cgi.scf

%files -n vidcat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vidcat

%files -n w3camd
%defattr(644,root,root,755)
%doc w3camd*.html
%attr(755,root,root) %{_sbindir}/w3camd
