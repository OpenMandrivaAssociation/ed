Summary:	The GNU line editor
Name:		ed
Version:	1.9
Release:	3
License:	GPLv3+
Group:		Text tools
Url:		http://www.gnu.org/software/ed/ed.html
Source0:	ftp://ftp.gnu.org/pub/gnu/ed/ed-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/ed/ed-%{version}.tar.gz.sig

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
%configure2_5x \
	--bindir=/bin \
	--exec-prefix=/ \
	CFLAGS="%{optflags}" CC="%__cc" \
	CXXFLAGS="%{optflags}" \
	LDFLAGS="%{?ldflags}"

%make

%check
# all tests must pass
make check

%install
%makeinstall_std

%files
%doc NEWS README AUTHORS TODO ChangeLog
/bin/ed
/bin/red
%{_infodir}/ed.info*
%{_mandir}/*/*

