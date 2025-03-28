#
# Conditional build:
%bcond_without	luajit		# build without luajit
%bcond_with	tests		# build with tests
#
%ifarch x32
%undefine	with_luajit
%endif

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		cantor
Summary:	Cantor
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	6
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b2579f3ac8b0618ebd14b21d3c1342a1
Patch0:		luajit-5.2.patch
URL:		https://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Help-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	R
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-analitza-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kpty-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	libmarkdown-devel
BuildRequires:	libqalculate-devel >= 2.8.2
%{?with_luajit:BuildRequires:	luajit-devel}
BuildRequires:	ninja
BuildRequires:	poppler-qt5-devel
BuildRequires:	qt5-assistant
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cantor is a KDE Application aimed to provide a nice Interface for
doing Mathematics and Scientific Computing. It doesn't implement its
own Computation Logic, but instead is built around different Backends.

Available Backends
- Julia Programming Language: http://julialang.org/
- KAlgebra for Calculation and Plotting: http://edu.kde.org/kalgebra/
  %{?with_luajit:- Lua Programming Language: http://lua.org/}
- Maxima Computer Algebra System: http://maxima.sourceforge.net/
- Octave for Numerical Computation: https://gnu.org/software/octave/
- Python 2 Programming Language: http://python.org/
- Python 3 Programming Language: http://python.org/
- Qalculate Desktop Calculator: http://qalculate.sourceforge.net/
- R Project for Statistical Computing: http://r-project.org/
- Sage Mathematics Software: http://sagemath.org/
- Scilab for Numerical Computation: http://scilab.org/

%description -l pl.UTF-8
Cantor jest programem KDE, którego celem jest dostarczenie miłego
interfejsu do obliczeń naukowych. Cantor nie implementuje własnej
logiki obliczeń, zamiast tego jest zbudowany wokół różnych backendów.

Dostępne backendy:
- język programowania Julia: http://julialang.org/
- KAlgebra do obliczeń i rysowania: http://edu.kde.org/kalgebra/
  %{?with_luajit:- język Lua: http://lua.org/}
- system komputerowej algebry Maxima: http://maxima.sourceforge.net/
- Octave do obliczeń numerycznych: https://gnu.org/software/octave/
- język Python 3: http://python.org/
- kalkulator biurkowy Qalculate: http://qalculate.sourceforge.net/
- projekt R do obliczeń statystycznych: http://r-project.org/
- oprogramowanie matematyczne Sage: http://sagemath.org/
- Scilab do obliczeń numerycznych: http://scilab.org/

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
%patch -P 0 -p1

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%{?with_luajit:%{_datadir}/knsrcfiles/cantor_lua.knsrc}
%attr(755,root,root) %{_bindir}/cantor_pythonserver
%attr(755,root,root) %{_libdir}/cantor_pythonbackend.so
%ghost %{_libdir}/libcantorlibs.so.28
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_pythonbackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_filebrowserpanelplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_tocpanelplugin.so
%{_datadir}/cantor/octave/graphic_packages.xml
%{_datadir}/cantor/python/graphic_packages.xml
%{_datadir}/config.kcfg/pythonbackend.kcfg
%{_datadir}/knsrcfiles/cantor.knsrc
%{_datadir}/knsrcfiles/cantor_kalgebra.knsrc
%{_datadir}/knsrcfiles/cantor_maxima.knsrc
%{_datadir}/knsrcfiles/cantor_octave.knsrc
%{_datadir}/knsrcfiles/cantor_python.knsrc
%{_datadir}/knsrcfiles/cantor_qalculate.knsrc
%{_datadir}/knsrcfiles/cantor_r.knsrc
%{_datadir}/knsrcfiles/cantor_sage.knsrc
%{_datadir}/knsrcfiles/cantor_scilab.knsrc
%attr(755,root,root) %{_bindir}/cantor
%attr(755,root,root) %{_bindir}/cantor_rserver
%attr(755,root,root) %{_bindir}/cantor_scripteditor
%attr(755,root,root) %{_libdir}/libcantor_config.so
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
%{?with_luajit:%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_luabackend.so}
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_maximabackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_octavebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_qalculatebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_rbackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_sagebackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/backends/cantor_scilabbackend.so
%dir %{_libdir}/qt5/plugins/cantor/panels
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_helppanelplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cantor/panels/cantor_variablemanagerplugin.so
%{_desktopdir}/org.kde.cantor.desktop
%dir %{_datadir}/cantor
%{_datadir}/cantor/latex
%{_datadir}/cantor/maximabackend
%{_datadir}/cantor/octavebackend
%dir %{_datadir}/cantor/octave
%dir %{_datadir}/cantor/python
%{_datadir}/cantor/xslt
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/kalgebrabackend.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
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
%{?with_luajit:%{_iconsdir}/hicolor/48x48/apps/luabackend.png}
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
%{_datadir}/kxmlgui5/cantor/cantor_advancedplot_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_create_matrix_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_differentiate_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_eigenvalues_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_eigenvectors_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_import_package_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_integrate_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_invert_matrix_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_plot2d_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_plot3d_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_qalculateplotassistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_runscript_assistant.rc
%{_datadir}/kxmlgui5/cantor/cantor_solve_assistant.rc
%{_datadir}/metainfo/org.kde.cantor.appdata.xml
%{?with_luajit:%{_datadir}/config.kcfg/luabackend.kcfg}
%{_datadir}/mime/packages/cantor.xml
%{_libdir}/qt5/plugins/cantor/panels/cantor_documentationpanelplugin.so
%{_libdir}/qt5/plugins/kf5/parts/cantorpart.so
%{_datadir}/config.kcfg/octavebackend.kcfg.in
%{_datadir}/knsrcfiles/cantor-documentation.knsrc

%files devel
%defattr(644,root,root,755)
%{_includedir}/cantor
%{_libdir}/libcantorlibs.so
%{_libdir}/cmake/Cantor
