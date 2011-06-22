Summary:	Ruby binding to the EET library
Summary(pl.UTF-8):	Dowiązania języka Ruby do biblioteki EET
Name:		ruby-eet
Version:	0.1.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	ftp://code-monkey.de/pub/ruby-eet/%{name}-%{version}.tar.gz
# Source0-md5:	f5ecfd0bd35063e9219be4983fcbf6c8
Patch0:		%{name}-ruby1.9.patch
URL:		http://code-monkey.de/pages/ruby-eet
BuildRequires:	eet-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-rake >= 0.5.0
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ruby_hdrdir	%(%{__ruby} -r rbconfig -e 'print Config::CONFIG["rubyhdrdir"]')
%define		ruby_arch	%(%{__ruby} -r rbconfig -e 'print Config::CONFIG["arch"]')

%description
Ruby binding to the EET library.

%description -l pl.UTF-8
Dowiązania języka Ruby do biblioteki EET.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
CFLAGS="%{rpmcflags} -I%{ruby_hdrdir} -I%{ruby_hdrdir}/ruby -I%{ruby_hdrdir}/%{ruby_arch}" \
CC="%{__cc}" \
rake -I.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_sitearchdir}}

DESTDIR=$RPM_BUILD_ROOT \
rake -I. install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{ruby_sitelibdir}/eet.rb
%attr(755,root,root) %{ruby_sitearchdir}/eet_ext.so
