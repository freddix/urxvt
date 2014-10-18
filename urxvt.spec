%include	/usr/lib/rpm/macros.perl

Summary:	Rxvt terminal with unicode support and some improvements
Name:		urxvt
Version:	9.20
Release:	2
Group:		X11/Applications
License:	GPL v2+
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	4a5b823f08d21036f94a6c51e94d025b
Source1:	%{name}.desktop
URL:		http://software.schmorp.de/
BuildRequires:	autoconf
BuildRequires:	fontconfig-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel
BuildRequires:	sed
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	zlib-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URxvt is a Rxvt modification which includes:
- unicode support
- xft font support (antialiasing)
- background pixmaps
- background tinting
- real transparency

%prep
%setup -qn rxvt-unicode-%{version}

%build
%configure \
	--disable-frills	    \
	--disable-pixbuf	    \
	--disable-smart-resize	    \
	--enable-256-color	    \
	--enable-combining	    \
	--enable-fading		    \
	--enable-font-styles	    \
	--enable-iso14755	    \
	--enable-keepscrolling	    \
	--enable-lastlog	    \
	--enable-mousewheel	    \
	--enable-next-scroll	    \
	--enable-perl		    \
	--enable-pointer-blank	    \
	--enable-rxvt-scroll	    \
	--enable-selectionscrolling \
	--enable-slipwheeling	    \
	--enable-startup-notification	\
	--enable-transparency	    \
	--enable-unicode3	    \
	--enable-utmp		    \
	--enable-wtmp		    \
	--enable-xft		    \
	--enable-xim		    \
	--enable-xterm-scroll	    \
	--with-terminfo=%{_datadir}/terminfo
%{__make} \
	CXXFLAGS="%{rpmcxxflags}" \
	CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so urxvtc.1' >$RPM_BUILD_ROOT%{_mandir}/man1/urxvtd.1

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes doc/README.xvt
%attr(755,root,root) %{_bindir}/urxvt*
%{_desktopdir}/%{name}.desktop
%{_libdir}/%{name}
%{_mandir}/man1/urxvt*.1*
%{_mandir}/man3/urxvtperl.3*
%{_mandir}/man7/urxvt.7*

