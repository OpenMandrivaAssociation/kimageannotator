%define libname %mklibname kImageAnnotator
%define devname %mklibname -d kImageAnnotator

Name:		kimageannotator
Version:	0.7.1
Release:	4
Summary:	Library containing tools for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/kImageAnnotator-%{version}.tar.gz
#Patch0:		https://github.com/ksnip/kImageAnnotator/commit/52ed4a9415310ea941aae480cbd777acc37842ac.patch

BuildSystem:	cmake
BuildOption:	-DBUILD_EXAMPLE=ON -DBUILD_WITH_QT6=ON

BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)

%description
Library containing tools for annotating images

%package -n %{libname}
Summary: Library containing tools for annotating images
Group: System/Libraries
%rename %{_lib}kimageannotator
%rename %{mklibname kImageAnnotator-Qt6}

%description -n %{libname}
Library containing tools for annotating images

%package -n %{devname}
Summary:    Development package for %name
Requires:   %name = %{EVRD}
Group:	Development/Libraries/C++
%rename kimageannotator-devel
%rename %{_lib}kimageannotator-devel
%rename %{mklibname -d kImageAnnotator-Qt6}

%description -n %{devname}
%summary

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/libkImageAnnotator.so*
%{_datadir}/*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/libkImageAnnotator.so*
