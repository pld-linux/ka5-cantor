%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		cantor
Summary:	Cantor
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b94d96c56c6e0622d8167e64ddf3902a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cantor is a KDE Application aimed to provide a nice Interface for
doing Mathematics and Scientific Computing. It doesn't implement its
own Computation Logic, but instead is built around different Backends.

Available Backends
- Julia Programming Language: http://julialang.org/
- KAlgebra for Calculation and Plotting: http://edu.kde.org/kalgebra/
- Lua Programming Language: http://lua.org/
- Maxima Computer Algebra System: http://maxima.sourceforge.net/
- Octave for Numerical Computation: https://gnu.org/software/octave/
- Python 2 Programming Language: http://python.org/
- Python 3 Programming Language: http://python.org/
- Qalculate Desktop Calculator: http://qalculate.sourceforge.net/
- R Project for Statistical Computing: http://r-project.org/
- Sage Mathematics Software: http://sagemath.org/
- Scilab for Numerical Computation: http://scilab.org/

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/cantor.knsrc
/etc/xdg/cantor_kalgebra.knsrc
/etc/xdg/cantor_maxima.knsrc
/etc/xdg/cantor_octave.knsrc
/etc/xdg/cantor_python2.knsrc
/etc/xdg/cantor_python3.knsrc
/etc/xdg/cantor_qalculate.knsrc
/etc/xdg/cantor_r.knsrc
/etc/xdg/cantor_sage.knsrc
/etc/xdg/cantor_scilab.knsrc
%attr(755,root,root) %{_bindir}/cantor
%attr(755,root,root) %{_bindir}/cantor_python3server
%attr(755,root,root) %{_bindir}/cantor_rserver
%attr(755,root,root) %{_libdir}/libcantor_config.so
%attr(755,root,root) %{_libdir}/libcantor_pythonbackend.so
%attr(755,root,root) %ghost %{_libdir}/libcantorlibs.so.17
%attr(755,root,root) %{_libdir}/libcantorlibs.so.*.*.*
%dir %{_libdir}/qt5/plugins/cantor
%dir %{_libdir}/qt5/plugins/cantor/assistants
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_advancedplotassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_creatematrixassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_differentiateassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_eigenvaluesassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_eigenvectorsassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_importpackageassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_integrateassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_invertmatrixassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_plot2dassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_plot3dassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_qalculateplotassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_runscriptassistant.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/assistants/cantor_solveassistant.so
%dir %{_libdir}/qt5/plugins/cantor/backends
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_kalgebrabackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_maximabackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_nullbackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_octavebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_python2backend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_python3backend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_qalculatebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_rbackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_sagebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_scilabbackend.so
%dir %{_libdir}/qt5/plugins/cantor/panels
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_helppanelplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_variablemanagerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/libcantorpart.so
%{_desktopdir}/org.kde.cantor.desktop
%{_datadir}/cantor
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/kalgebrabackend.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
%{_datadir}/config.kcfg/octavebackend.kcfg
%{_datadir}/config.kcfg/python2backend.kcfg
%{_datadir}/config.kcfg/python3backend.kcfg
%{_datadir}/config.kcfg/qalculatebackend.kcfg
%{_datadir}/config.kcfg/rserver.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config.kcfg/scilabbackend.kcfg
%{_iconsdir}/hicolor/128x128/apps/cantor.png
%{_iconsdir}/hicolor/16x16/apps/cantor.png
%{_iconsdir}/hicolor/22x22/apps/cantor.png
%{_iconsdir}/hicolor/32x32/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/juliabackend.png
%{_iconsdir}/hicolor/48x48/apps/kalgebrabackend.png
%{_iconsdir}/hicolor/48x48/apps/luabackend.png
%{_iconsdir}/hicolor/48x48/apps/maximabackend.png
%{_iconsdir}/hicolor/48x48/apps/octavebackend.png
%{_iconsdir}/hicolor/48x48/apps/pythonbackend.png
%{_iconsdir}/hicolor/48x48/apps/qalculatebackend.png
%{_iconsdir}/hicolor/48x48/apps/rbackend.png
%{_iconsdir}/hicolor/48x48/apps/sagebackend.png
%{_iconsdir}/hicolor/48x48/apps/scilabbackend.png
%{_iconsdir}/hicolor/64x64/apps/cantor.png
%dir %{_datadir}/kxmlgui5/cantor
%{_datadir}/kxmlgui5/cantor/cantor_part.rc
%{_datadir}/kxmlgui5/cantor/cantor_scripteditor.rc
%{_datadir}/kxmlgui5/cantor/cantor_shell.rc
%{_datadir}/metainfo/org.kde.cantor.appdata.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/cantor
%attr(755,root,root) %{_libdir}/libcantorlibs.so

