%define upstream_name    DateTime-Format-Pg
%define upstream_version 0.16009

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse and format PostgreSQL dates and times
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Pg-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Builder)
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create 'DateTime' or 'DateTime::Duration' objects, and it can
take a 'DateTime' or 'DateTime::Duration' object and produce a string
representing it in a format accepted by PostgreSQL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.yml 
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.160.50-2mdv2011.0
+ Revision: 654303
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.160.50-1mdv2011.0
+ Revision: 607837
- import perl-DateTime-Format-Pg



