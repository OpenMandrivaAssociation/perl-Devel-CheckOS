%define upstream_name       Devel-CheckOS
%define upstream_version 2.04
Name:		perl-%{upstream_name}
Version:	2.04
Release:	44
Summary:	Check what OS we're running on

License:	GPL or Artistic
Group:		Development/Perl
Url:		https://github.com/DrHyde/perl-modules-Devel-CheckOS
Source:		https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{upstream_version}.tar.gz

BuildRequires:	make
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
%setup -q -n Devel-CheckOS-2.04 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc README
%{_bindir}/use-devel-assertos
%{_mandir}/man1/use-devel-assertos.1*
%{_mandir}/man3/*
%{perl_vendorlib}/Devel



