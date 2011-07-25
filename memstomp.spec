Summary:	specialized memcpy checker with low overhead
Name:		memstomp
Version:	0.1.5
Release:	0.1
License:	LGPL v3+ with exception (backtrace-symbols.c is GPL v2+)
Group:		Development/Debug
Source0:	%{name}.tar.bz2
# Source0-md5:	d0c7c703f0e4a9a0409509f7fa8b1744
Patch0:		%{name}-version.patch
URL:		http://fedorapeople.org/gitweb?p=wcohen/public_git/memstomp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memstomp checks the operation of memcpy. In particular memstomp warns
when memcpy is used to copy overlapping regions of memory (such as the
problem encountered in
https://bugzilla.redhat.com/show_bug.cgi?id=638477)

Just use it as prefix for your usual command line and it will check
memcpy used in all child processes. Note that valgrind can perform
this type of check also. Memstomp merely lowers the overhead for this
type of check.

%prep
%setup -qn %{name}.git
%patch0 -p1
sh bootstrap.sh

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/memstomp
%attr(755,root,root) %{_libdir}/libmemstomp-backtrace-symbols.so
%attr(755,root,root) %{_libdir}/libmemstomp.so
