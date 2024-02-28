%define oname kImageAnnotator
%define major %(echo %{version} |cut -d. -f1)
%define oldlibname %mklibname %{name} 0
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

Name:		kimageannotator
Version:	0.7.0
Release:	1
Summary:	Tool for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: cmake ninja
BuildRequires: qmake5
BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(x11)

BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)

%description
kImageAnnotator is a tool for annotating images.

#------------------------------------------------

%prep
%autosetup -p1 -n kImageAnnotator-%{version}
%cmake \
	-DBUILD_EXAMPLE=ON \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DBUILD_EXAMPLE=ON \
	-DBUILD_WITH_QT6=ON \
	-G Ninja

%build
%ninja_build -C build
%ninja_build -C build-qt6

%install
%ninja_install -C build
%ninja_install -C build-qt6
%find_lang %{name} --with-qt --all-name
%libpackages

for i in $(ls %{specpartsdir} |grep -v devel); do
	sed -i -e '/%%package/aRequires: %{name} = %{EVRD}' %{specpartsdir}/$i
done

%files -f %{name}.lang
