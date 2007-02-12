Summary:	Ruby binding to the eet library
Summary(pl.UTF-8):	Dowiązania języka Ruby do biblioteki eet
Name:		ruby-eet
Version:	0.1.3
Release:	0.1
License:	Ruby's
Group:		Development/Languages
Source0:	ftp://code-monkey.de/pub/ruby-eet/%{name}-%{version}.tar.gz
# Source0-md5:	480d8c44af28099ce7c671b8a58db55a
URL:		http://code-monkey.de/projects/ruby-eet.html
BuildRequires:	eet-devel
BuildRequires:	rake >= 0.5.0
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the eet library.

%description -l pl.UTF-8
Dowiązania języka Ruby do biblioteki eet.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" CC="%{__cc}" rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_sitearchdir}}

DESTDIR=$RPM_BUILD_ROOT rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_sitelibdir}/eet.rb
%attr(755,root,root) %{ruby_sitearchdir}/eet_ext.so
