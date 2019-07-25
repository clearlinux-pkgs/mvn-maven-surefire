#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-surefire
Version  : 2.22.0
Release  : 7
URL      : https://repo1.maven.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.jar
Source8  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.jar
Source10  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.jar
Source13  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.jar
Source15  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.jar
Source17  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.pom
Source18  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.jar
Source19  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.pom
Source20  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire-providers/2.22.0/surefire-providers-2.22.0.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire/2.19.1/surefire-2.19.1.pom
Source22  : https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire/2.22.0/surefire-2.22.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-surefire-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-surefire package.
Group: Data

%description data
data components for the mvn-maven-surefire package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-providers/2.22.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-providers/2.22.0/surefire-providers-2.22.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.19.1
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.19.1/surefire-2.19.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.22.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.22.0/surefire-2.22.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-failsafe-plugin/2.19.1/maven-failsafe-plugin-2.19.1.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.12.4/maven-surefire-plugin-2.12.4.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.21.0/maven-surefire-plugin-2.21.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-plugin/2.22.0/maven-surefire-plugin-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-surefire-report-plugin/2.19.1/maven-surefire-report-plugin-2.19.1.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/surefire/maven-surefire-common/2.22.0/maven-surefire-common-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-api/2.22.0/surefire-api-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-booter/2.22.0/surefire-booter-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-junit4/2.22.0/surefire-junit4-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.jar
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-logger-api/2.22.0/surefire-logger-api-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire-providers/2.22.0/surefire-providers-2.22.0.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.19.1/surefire-2.19.1.pom
/usr/share/java/.m2/repository/org/apache/maven/surefire/surefire/2.22.0/surefire-2.22.0.pom
