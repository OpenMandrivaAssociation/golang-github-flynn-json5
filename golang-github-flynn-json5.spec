# Run tests in check section
%bcond_without check

%global goipath         github.com/flynn/json5
%global commit          7620272ed63390e979cf5882d2fa0506fe2a8db5

%global common_description %{expand:
Go JSON5 decoder package based on encoding/json.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Go JSON5 decoder package based on encoding/json
License: BSD and MIT
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(github.com/kylelemons/godebug/pretty)
BuildRequires: golang(github.com/robertkrimen/otto)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git7620272
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git7620272
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160717git7620272
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20160717git7620272
- First package for Fedora

