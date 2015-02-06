%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define		oname	Box2D

Summary:	A 2D physics engine for games
Name:		box2d
Version:	2.2.1
Release:	4
Group:		System/Libraries
License:	BSD
Url:		http://www.box2d.org
Source:		http://box2d.googlecode.com/files/%{oname}_v%{version}.zip
Patch1:		box2d-2.2.1-cmake.patch
BuildRequires:	cmake
BuildRequires:	%{_lib}glui2-devel
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
%doc License.txt Readme.txt Documentation
%{_libdir}/lib*.a
%{_libdir}/%{oname}
%{_includedir}/%{oname}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}_v%{version}
%patch1 -p1
# XXX incorrect dates in zipfile
find . -type f -exec touch {} \;

%build
%cmake
%make

%install
%makeinstall_std -C build

