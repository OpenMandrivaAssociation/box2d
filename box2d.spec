%define major 2

# Make sure we don't have non-PIC code in a static library...
%global optflags %{optflags} -fPIC

%define libname %mklibname box2d %{major}
%define devname %mklibname -d box2d

Summary:	A 2D physics engine for games
Name:		box2d
Version:	2.4.1
Release:	2
Group:		System/Libraries
License:	BSD
Url:		http://www.box2d.org
Source:		https://github.com/erincatto/box2d/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		https://src.fedoraproject.org/rpms/Box2D/raw/master/f/Box2D-2.3.1-cmake.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	glfw-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xi)

%description
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A 2D physics engine for games
Group:		System/Libraries

%description -n %{libname}
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	A 2D physics engine for games
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
%rename %{name}-devel

%description -n %{devname}
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

%files -n %{devname}
%{_includedir}/box2d
%{_libdir}/lib*.so
%{_libdir}/cmake/box2d

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DBOX2D_INSTALL:BOOL=ON \
	-DBOX2D_BUILD_SHARED:BOOL=ON \
	-DBOX2D_BUILD_UNIT_TESTS:BOOL=OFF \
	-DBOX2D_BUILD_TESTBED:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
