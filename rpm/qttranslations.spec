Name:       qt5-qttranslations
Summary:    Qt translations module
Version:    5.1.0
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the translations module


#### Build section

%prep
%setup -q -n %{name}-%{version}/qttranslations

%build
export QTDIR=/usr/share/qt5
touch .git
qmake -qt=5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install




#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_qt5_translationdir}/*


#### No changelog section, separate $pkg.changes contains the history
