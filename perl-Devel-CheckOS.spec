%define upstream_name       Devel-CheckOS
%define upstream_version 1.72
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Check what OS we're running on

License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Compare)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Temp) >= 0.190.0
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A learned sage once wrote on IRC:

   $^O is stupid and ugly, it wears its pants as a hat

Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_bindir}/use-devel-assertos
%{_mandir}/man1/use-devel-assertos.1*
%{_mandir}/man3/*
%{perl_vendorlib}/Devel



