%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph-XY
Summary:	GD::Graph::XY Perl module - XY graphing modules for GD::Graph
Summary(pl):	Modu³ Perla GD::Graph::XY - modu³y do wykresów XY dla GD::Graph
Name:		perl-GD-Graph-XY
Version:	0.92
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-Graph >= 1.30
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some XY graphing modules for GD::Graph.

%description -l pl
Ten pakiet zawiera trochê modu³ów do wykresów XY dla GD::Graph.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme
%{perl_sitelib}/GD/Graph/*.pm
%{_mandir}/man3/*
