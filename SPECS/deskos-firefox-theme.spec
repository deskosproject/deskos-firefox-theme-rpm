%define debug_package %{nil}
%global arc_firefox_theme_tag 45.20160308

Name:           deskos-firefox-theme
Version:        0.1
Release:        3%{?dist}
Summary:        DeskOS Firefox Theme

Group:          User Interface/Desktops
License:        MPLv2.0
URL:            https://github.com/deskosproject/deskos-firefox-theme
Source0:        https://github.com/horst3180/arc-firefox-theme/archive/%{arc_firefox_theme_tag}.tar.gz
Patch0:         deskos-name.patch
Patch1:         deskos-hide-minimize-button.patch

BuildRequires:  autoconf
BuildRequires:  automake
Requires:       firefox

%description
DeskOS Firefox Theme, based on the Arc Firefox Theme.
This theme is meant to be used in conjunction with the DeskOS GNOME Theme.

%prep
%setup -q -n arc-firefox-theme-%{arc_firefox_theme_tag}
%patch0 -p1
%patch1 -p1

%build
./autogen.sh --prefix=/usr \
             --disable-darker \
             --disable-dark

make mkxpi

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/firefox/browser/extensions/
cp -p arc-firefox-theme-%{arc_firefox_theme_tag}.xpi $RPM_BUILD_ROOT/%{_libdir}/firefox/browser/extensions/\{52c2877e-44e1-11e5-8874-a62d1d5d46B0\}.xpi

%files
%defattr(-,root,root)
%{_libdir}/firefox/browser/extensions/*.xpi

%changelog
* Thu Dec 22 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-3
- Don't build debuginfo

* Thu Dec 22 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-2
- Removed BuildArch: noarch

* Mon Dec 19 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Initial release
