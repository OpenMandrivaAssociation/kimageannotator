%define oname kImageAnnotator
%define major %(echo %{version} |cut -d. -f1)
%define oldlibname %mklibname %{name} 0
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

Name:		kimageannotator
Version:	0.6.0
Release:	1
Summary:	Tool for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: cmake ninja
BuildRequires: qmake5
BuildRequires: cmake(kColorPicker)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(x11)

%description
kImageAnnotator is a tool for annotating images.

#------------------------------------------------

%package -n	%{libname}
Summary:	Tool for annotating images
Group:		System/Libraries
# Fix bogus naming scheme from earlier builds
%rename %mklibname %{name} 0.4.0
%rename %mklibname %{name} 0.4.2
%rename %{oldlibname}

%description -n	%{libname}
kImageAnnotator is a tool for annotating images.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	cmake(kColorPicker)

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}
%cmake \
	-DBUILD_EXAMPLE=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -n %{libname} -f %{name}.lang
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/lib%{oname}.so.%{major}*
%dir %{_datadir}/kImageAnnotator
%dir %{_datadir}/kImageAnnotator/translations

%files -n %{develname}
%doc CHANGELOG.md README.md
%{_includedir}/%{oname}/
%{_libdir}/lib%{oname}.so
%{_libdir}/cmake/%{oname}/
