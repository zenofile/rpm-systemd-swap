%define        pkgname     systemd-swap
%global        forgeurl    https://github.com/Nefelim4ag/%{pkgname}
Version:       4.3.0
%global        tag         %{version}

%forgemeta -i

Name: systemd-swap
Summary: Creating hybrid swap space from zram swaps, swap files and swap partitions
Release: 1%{?dist}
License: GPLv3+
URL:     %{forgeurl}
Source:  %{forgesource}

BuildArch: noarch

%if 0%{?fedora} >= 31
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd-units
%endif
%{?systemd_requires}

# support for zram
Requires: util-linux
Requires: kmod

# need Linux kernel version 2.6.37.1 or better to use zram
#Requires: kernel >= 2.6.37.1
Requires: kmod(zram.ko)

%description
Systemd-swap manages the configuration of zram and zswap and allows for automatically setting up swap files through swapfc and automatically enables availible swapfiles and swap partitions.

%prep
%forgeautosetup -p1

%build

%install
%make_install

%post
%systemd_post systemd-swap.service

%preun
%systemd_preun systemd-swap.service

%postun
%systemd_postun_with_restart systemd-swap.service

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/systemd/swap.conf
%{_unitdir}/%{pkgname}.service
%{_bindir}/%{pkgname}
%{_mandir}/man5/swap.conf.5*
%{_mandir}/man8/%{pkgname}.8*
%dir %{_datadir}/%{pkgname}/
%{_datadir}/%{pkgname}/swap-default.conf

%ghost %dir %{_sharedstatedir}/%{pkgname}
%ghost %dir %{_sharedstatedir}/%{pkgname}/swapfc
%ghost %{_sharedstatedir}/%{pkgname}/*


%changelog
* Sat Jun 13 2020 zeno <zeno@bafh.org> - 4.2.0
- bump to new stable release

* Sun Jun 07 2020 zeno <zeno@bafh.org> - 4.1.0
- bump to new stable release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-3
- fix some typos

* Wed Apr 10 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-2
- fix hints from package review
- simplify dependencies
- use macros
- note real version in changelog
- generate manpage

* Tue Jul 11 2017 Raphael Groner <projects.rg@smart.ms> - 3.3.0-1
- initial
