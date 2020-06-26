%define	oname		kImageAnnotator
%define	major		%{version}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		kimageannotator
Version:	0.3.1
Release:	1
Summary:	Tool for annotating images
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kImageAnnotator
Source:		https://github.com/ksnip/kImageAnnotator/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(kColorPicker)
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
%autosetup -p1 -n %{oname}-%{version}

%build
%cmake \
	-DBUILD_EXAMPLE=ON
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/lib%{oname}.so.%{major}

%files -n %{develname}
%doc CHANGELOG.md README.md
%{_includedir}/%{oname}/
%{_libdir}/lib%{oname}.so
%{_libdir}/cmake/%{oname}/
