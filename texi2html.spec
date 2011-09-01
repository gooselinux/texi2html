Name: texi2html
Version: 1.82
Release: 5.1%{?dist}
# GPLv2+ is for the code
# OFSFDL (Old FSF Documentation License) for the documentation
# CC-BY-SA or GPLv2 for the images
License: GPLv2+ and OFSFDL and (CC-BY-SA or GPLv2)
Group: Applications/Text
Summary: A highly customizable texinfo to HTML and other formats translator
Source0: http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/texi2html/
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: perl >= 5.004
Requires: latex2html
BuildRequires: perl(Text::Unidecode) latex2html tetex-tex4ht
# not detected automatically because it is required at runtime based on
# user configuration
Requires: perl(Text::Unidecode)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML, 
and other formats.  Configuration files written in perl provide fine degree 
of control over the final output, allowing most every aspect of the final 
output not specified in the Texinfo input file to be specified.  

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# directories shared by all the texinfo implementations for common
# config files, like htmlxref.cnf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/texinfo $RPM_BUILD_ROOT%{_sysconfdir}/texinfo

%check
#make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir > /dev/null 2>&1 || :

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO %{name}.init
%{_bindir}/%{name}
%{_datadir}/texinfo/html/%{name}.html
%{_mandir}/man*/%{name}*
%{_infodir}/%{name}.info*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.init
%{_datadir}/%{name}/*.texi
%dir %{_datadir}/%{name}/i18n/
%{_datadir}/%{name}/i18n/*
%dir %{_datadir}/%{name}/images/
%{_datadir}/%{name}/images/*
%dir %{_datadir}/texinfo
%dir %{_sysconfdir}/texinfo

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.82-5.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Jindrich Novy <jnovy@redhat.com> 1.82-5
- don't complain if installing with --excludedocs (#516010)
- disable tests for now

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  9 2009 Jindrich Novy <jnovy@redhat.com> 1.82-2
- run tests after build

* Fri Jan  9 2009 Jindrich Novy <jnovy@redhat.com> 1.82-1
- update to 1.82

* Tue Jan  6 2009 Jindrich Novy <jnovy@redhat.com> 1.80-1
- update to 1.80

* Tue Aug 28 2007 Patrice Dumas <pertusus@free.fr> 1.78-3
- use the right license tag for the documentation

* Tue Aug 28 2007 Patrice Dumas <pertusus@free.fr> 1.78-2
- Requires latex2html and perl(Text::Unidecode)
- add ownership for directories common for the texinfo implementations
- correct license

* Wed Jun  6 2007 Jindrich Novy <jnovy@redhat.com> 1.78-1
- update to 1.78

* Wed Feb 14 2007 Jindrich Novy <jnovy@redhat.com> 1.77-0.1.20070214cvs
- update to 1.77 release candidate (#226487)

* Fri Jan  5 2007 Jindrich Novy <jnovy@redhat.com> 1.76-6
- fix post/preun scriptlets so that they won't fail with docs disabled
  (thanks to Ville Skyttä)

* Wed Nov 29 2006 Jindrich Novy <jnovy@redhat.com> 1.76-5
- replace PreReq, fix BuildRoot

* Thu Aug 24 2006 Jindrich Novy <jnovy@redhat.com> 1.76-4.fc6
- correct URLs, name patch backups correctly

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.76-3.1
- rebuild

* Sat Feb 25 2006 Jindrich Novy <jnovy@redhat.com> 1.76-3
- PreReq info (#182888)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Mar 08 2005 Jindrich Novy <jnovy@redhat.com> 1.76-2
- replace %%configure with ./configure to prevent definition of
  target, build and host for noarch package

* Fri Feb 18 2005 Jindrich Novy <jnovy@redhat.com> 1.76-1
- we have separate texi2html package now (#121889)
- fix Source0
- BuildArchitectures -> BuildArch
- create backups for patches

* Thu Feb 10 2005 MATSUURA Takanori <t-matsuu@estyle.ne.jp> - 1.76-0
- updated to 1.76

* Mon Jan 10 2005 MATSUURA Takanori <t-matsuu@estyle.ne.jp> - 1.72-1.fc3
- initial build for Fedora Core 3 based on spec file in source tarball

* Mon Mar 23 2004 Patrice Dumas <pertusus@free.fr> 0:1.69-0.fdr.1
- Initial build.
