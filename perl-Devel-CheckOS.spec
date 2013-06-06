%define upstream_name       Devel-CheckOS
%define upstream_version 1.71
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.71
Release:	1
Summary:	Check what OS we're running on
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Devel/Devel-CheckOS-1.71.tar.gz

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


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.640.0-1mdv2011.0
+ Revision: 659911
- update to new version 1.64

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.630.0-1mdv2011.0
+ Revision: 553120
- update to 1.63

* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.610.0-2mdv2010.0
+ Revision: 399800
- use %%perl_version macro

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.61-1mdv2010.0
+ Revision: 369726
- add missing prereq
- forcing mdv pkg, since file::temp is a dual-lifed pelr pkg
- update to new version 1.61

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50-1mdv2009.1
+ Revision: 329061
- import perl-Devel-CheckOS


* Tue Jan 13 2009 cpan2dist 1.50-1mdv
- initial mdv release, generated with cpan2dist


