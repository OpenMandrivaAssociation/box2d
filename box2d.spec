%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define		oname	Box2D

Summary:	A 2D physics engine for games
Name:		box2d
Version:	2.3.1
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.box2d.org
Source:		https://github.com/erincatto/box2d/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/Box2D/raw/master/f/Box2D-2.3.1-cmake.patch
BuildRequires:	cmake ninja
BuildRequires:	glfw-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(x11)

%description
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

#----------------------------------------------------------------------------

%package devel
Summary:	A 2D physics engine for games
Group:		Development/C++

%description devel
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

%files devel
%doc Box2D/License.txt Box2D/Readme.txt Box2D/Documentation
%{_libdir}/lib*.a
%{_libdir}/%{oname}
%{_includedir}/%{oname}
%{_libdir}/cmake/Box2D

#----------------------------------------------------------------------------

%prep
%autosetup -p1
cd Box2D
%cmake -G Ninja

%build
%ninja_build -C Box2D/build

%install
%ninja_install -C Box2D/build

