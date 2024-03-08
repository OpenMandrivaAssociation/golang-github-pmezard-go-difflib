# Run tests in check section
%bcond_without check

# https://github.com/pmezard/go-difflib
%global goipath		github.com/pmezard/go-difflib
%global forgeurl	https://github.com/pmezard/go-difflib
Version:		1.0.0

%gometa

Summary:	Partial port of Python difflib package to Go
Name:		golang-github-pmezard-go-difflib

Release:	1
Source0:	https://github.com/pmezard/go-difflib/archive/v%{version}/go-difflib-%{version}.tar.gz
URL:		https://github.com/pmezard/go-difflib
License:	BSD
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
Go-difflib is a partial port of python 3 difflib package.
Its main goal was to make unified and context diff available
in pure Go, mostly for testing purposes.

The following class and functions (and related tests) have be ported:

 *  SequenceMatcher
 *  unified_diff()
 *  context_diff()

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-difflib-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

