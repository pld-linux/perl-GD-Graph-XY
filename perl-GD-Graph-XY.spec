%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Graph-XY
Summary:	GD::Graph::XY Perl module - XY graphing modules for GD::Graph
Summary(pl):	Modu³ Perla GD::Graph::XY - modu³y do wykresów XY dla GD::Graph
Name:		perl-GD-Graph-XY
Version:	0.92
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	58534781f38657f1cb30d2739b9cb1bf
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-GD >= 1.18
BuildRequires:	perl-GD-Graph >= 1.30
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some XY graphing modules for GD::Graph.

%description -l pl
Ten pakiet zawiera trochê modu³ów do wykresów XY dla GD::Graph.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/GD/Graph/*.pm
%{_mandir}/man3/*
