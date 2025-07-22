Summary:	The GNU line editor
Name:		ed
Version:	1.22
Release:	1
License:	GPLv3+
Group:		Text tools
Url:		https://www.gnu.org/software/ed/ed.html
Source0:	http://ftpmirror.gnu.org/gnu/ed/%{name}-%{version}.tar.lz
BuildRequires:	lzip

%description
Ed is a line-oriented text editor, used to create, display, and modify text
files (both interactively and via shell scripts). For most purposes, ed has
been replaced in normal usage by full-screen editors (emacs and vi, for
example).

Ed was the original UNIX editor, and may be used by some programs. In general,
however, you probably don't need to install it and you probably won't use it
much.

%prep
%autosetup -p1

%build
%configure \
	CFLAGS="%{optflags} -Oz" CC="%{__cc}" \
	CXXFLAGS="%{optflags}" \
	LDFLAGS="%{?build_ldflags}"

%make_build

%check
# all tests must pass
make check

%install
%make_install

%files
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/ed
%{_bindir}/red
%doc %{_infodir}/ed.info*
%doc %{_mandir}/*/*
