%define	_exec_prefix	/

Summary:	The GNU line editor
Name:		ed
Version:	1.0
Release:	%mkrel 1
License:	GPLv3+
Group:		Text tools
URL:		http://www.gnu.org/software/ed/ed.html
Source0:	ftp://ftp.gnu.org/pub/gnu/ed/ed-%{version}.tar.bz2
Patch0:		ed-1.0-install.patch
Requires(post): info-install
Requires(preun):info-install
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ed is a line-oriented text editor, used to create, display, and modify text
files (both interactively and via shell scripts).  For most purposes, ed has
been replaced in normal usage by full-screen editors (emacs and vi, for
example).

Ed was the original UNIX editor, and may be used by some programs.  In general,
however, you probably don't need to install it and you probably won't use it
much.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%configure2_5x --bindir=/bin

%make CFLAGS="%{optflags}"

# all tests must pass
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc NEWS README AUTHORS TODO ChangeLog
/bin/ed
/bin/red
%{_infodir}/ed.info*
%{_mandir}/*/*
