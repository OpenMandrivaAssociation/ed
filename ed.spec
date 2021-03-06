Summary:	The GNU line editor
Name:		ed
Version:	1.17
Release:	1
License:	GPLv3+
Group:		Text tools
Url:		http://www.gnu.org/software/ed/ed.html
Source0:	ftp://ftp.gnu.org/pub/gnu/ed/ed-%{version}.tar.lz
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
%setup -q

%build
%configure \
	--bindir=/bin \
	--exec-prefix=/ \
	CFLAGS="%{optflags}" CC="%{__cc}" \
	CXXFLAGS="%{optflags}" \
	LDFLAGS="%{?ldflags}"

%make_build

%check
# all tests must pass
make check

%install
%make_install

%files
%doc NEWS README AUTHORS TODO ChangeLog
/bin/ed
/bin/red
%{_infodir}/ed.info*
%{_mandir}/*/*
