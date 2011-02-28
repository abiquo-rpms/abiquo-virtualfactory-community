%define abiquo_basedir /opt/abiquo

Name:     abiquo-virtualfactory-community
Version:  1.7
Release:  4%{?dist}%{?buildstamp}
Summary:  Abiquo Virtual Factory
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  virtualfactory.war
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-core
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package contains the community virtualfactory component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/virtualfactory/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tomcat/webapps/virtualfactory

%changelog
* Mon Feb 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- updated release string

* Fri Feb 11 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3.20110211_114901
- Upstream update

* Wed Feb 09 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3.20110209_145339
- Upstream update

* Wed Feb 09 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3.20110209_142924
- Upstream update

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- set buildarch to noarch

* Wed Feb 01 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial Release
