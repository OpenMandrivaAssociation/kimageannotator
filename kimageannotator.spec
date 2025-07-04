Name:		%{_lib}kImageAnnotator
Version:	0.7.1
Release:	1
Summary:	Tool for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/kImageAnnotator-%{version}.tar.gz
#Patch0:		https://github.com/ksnip/kImageAnnotator/commit/52ed4a9415310ea941aae480cbd777acc37842ac.patch

BuildSystem:	 cmake
BuildOption:   -DBUILD_EXAMPLE=ON -DBUILD_WITH_QT6=ON

BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)

%rename kimageannotator

%description
kImageAnnotator is a tool for annotating images.

%package devel

Summary:    Development package for %name
Requires:   %name = %version

%description devel
%summary

%files
%doc README.md
%license LICENSE
%{_libdir}/libkImageAnnotator.so*
%{_datadir}/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/libkImageAnnotator.so*
