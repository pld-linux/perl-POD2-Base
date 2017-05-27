#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	POD2
%define		pnam	Base
%include	/usr/lib/rpm/macros.perl
Summary:	Base module for translations of Perl documentation
Summary(pl.UTF-8):	Bazowy moduł do tłumaczeń dokumentacji Perla
Name:		perl-POD2-Base
Version:	0.044_1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FE/FERREIRA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8dd5125ba5026427cafdddaa7f5946a9
URL:		http://search.cpan.org/dist/POD2-Base/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an abstraction of the code in POD2::IT and POD2::FR.
These modules belong to the Italian and the French translation
projects of core Perl pods.

%description -l pl.UTF-8
Ten moduł to abstrakcja dla kodu w pakietach POD2::IT oraz POD2::FR.
Moduły te należą do projektów tłumaczenia podstawowych plików pod z
Perla na język włoski i francuski.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/POD2/Base.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/POD2/PT/POD2/Base.pod
rmdir $RPM_BUILD_ROOT%{perl_vendorlib}/POD2/PT/POD2
rmdir $RPM_BUILD_ROOT%{perl_vendorlib}/POD2/PT

install -d $RPM_BUILD_ROOT%{_mandir}/pt/man3
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/POD2::PT::POD2::Base.3pm $RPM_BUILD_ROOT%{_mandir}/pt/man3/POD2::Base.3pm

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/POD2/Base.pm
%{_mandir}/man3/POD2::Base.3pm*
%lang(pt) %{_mandir}/pt/man3/POD2::Base.3pm*
%{_examplesdir}/%{name}-%{version}
