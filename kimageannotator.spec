%define major		%{version}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		kimageannotator
Version:	0.2.1
Release:	%mkrel 1
Summary:	Tool for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	cmake(kColorPicker) >= 0.1.1
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(x11)

%description
kImageAnnotator is a tool for annotating images.

#------------------------------------------------

%package -n	%{libname}
Summary:	Tool for annotating images
Group:		System/Libraries

%description -n	%{libname}
kImageAnnotator is a tool for annotating images.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1 -n kImageAnnotator-%{version}

%build
%cmake_qt5 \
	-DBUILD_EXAMPLE=ON
%cmake_build

%install
%cmake_install

%files -n %{libname}
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libkImageAnnotator.so.%{major}

%files -n %{develname}
%doc CHANGELOG.md README.md
%{_includedir}/kImageAnnotator/
%{_libdir}/libkImageAnnotator.so
%{_libdir}/cmake/kImageAnnotator/
