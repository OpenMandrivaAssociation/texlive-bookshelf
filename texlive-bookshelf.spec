Name:		texlive-bookshelf
Version:	55475
Release:	1
Summary:	Create a nice image from a BibTeX file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookshelf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookshelf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookshelf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookshelf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package turns a BibTeX bibliography file into a
randomly-coloured, randomly-sized shelf of books, with the
title and author in a randomly-chosen typeface.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bookshelf
%{_texmfdistdir}/tex/latex/bookshelf
%doc %{_texmfdistdir}/doc/latex/bookshelf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
