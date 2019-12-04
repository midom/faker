Name:       fb-faker
Version:	0.1
Release:	%{_release}
Summary:	MySQL replication prefetcher

Group:		Applications/Databases
License:	GPL	
URL:		http://facebook.com/mysqlatfacebook
Source0:	http://anywhere/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: glib2-devel
BuildRequires: mysql-devel

%description
faker is high performance InnoDB fake updates based replication prefetcher

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -D faker $RPM_BUILD_ROOT/usr/local/bin/faker


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/bin/faker
