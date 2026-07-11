%global tl_name bookshelf
%global tl_revision 72521

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Create a nice image from a BibTeX file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/bookshelf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookshelf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookshelf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bookshelf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package turns a BibTeX bibliography file into a randomly-coloured,
randomly-sized shelf of books, with the title and author in a randomly-
chosen typeface.

