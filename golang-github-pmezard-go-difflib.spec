# http://github.com/pmezard/go-difflib

%global goipath         github.com/pmezard/go-difflib
%global commit          792786c7400a136282c1664665ae0a8db921c6c2


%gometa -i

Name:           golang-github-pmezard-go-difflib
Version:        0
Release:        0.11%{?dist}
Summary:        Partial port of Python difflib package to Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Jun 21 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git792786c
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git792786c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git792786c
- Bump to upstream 792786c7400a136282c1664665ae0a8db921c6c2
  resolves: #1490448

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitd8ed262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitd8ed262
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.gitd8ed262
- Bump to upstream d8ed2627bdf02c080bf22230dbb337003b7aba2d
  resolves: #1432934

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitf78a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf78a839
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitf78a839
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf78a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf78a839
- First package for Fedora
  resolves: #1272174
