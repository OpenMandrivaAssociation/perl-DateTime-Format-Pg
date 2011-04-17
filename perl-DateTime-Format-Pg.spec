%define upstream_name    DateTime-Format-Pg
%define upstream_version 0.16005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Parse and format PostgreSQL dates and times
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)
BuildRequires: perl(DateTime::TimeZone)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module understands the formats used by PostgreSQL for its DATE, TIME,
TIMESTAMP, and INTERVAL data types. It can be used to parse these formats
in order to create 'DateTime' or 'DateTime::Duration' objects, and it can
take a 'DateTime' or 'DateTime::Duration' object and produce a string
representing it in a format accepted by PostgreSQL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


