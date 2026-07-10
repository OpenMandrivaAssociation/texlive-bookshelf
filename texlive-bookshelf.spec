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
Requires(pre):	texlive-tlpkg
Requires:	texlive(bookshelf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package turns a BibTeX bibliography file into a randomly-coloured,
randomly-sized shelf of books, with the title and author in a randomly-
chosen typeface.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/bookshelf
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bookshelf
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/bookshelf
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/bookshelf/bookshelf.bst
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/LICENSE
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/Makefile
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/Makefile.doc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/Makefile.scripts
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/allfonts
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf-listallfonts.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf-mkfontsel.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf.dtx
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf.ins
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/bookshelf.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/excluded_patterns
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/features
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/sample.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/spines.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/spines.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/bookshelf/svgnam.sh
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bookshelf-listallfonts.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bookshelf-listallfonts.man1.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bookshelf-mkfontsel.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bookshelf-mkfontsel.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/scripts/bookshelf/bookshelf-listallfonts
%{_datadir}/texmf-dist/texmf-dist/scripts/bookshelf/bookshelf-mkfontsel
%{_datadir}/texmf-dist/texmf-dist/tex/latex/bookshelf/bookshelf-svgnam.tex
%{_datadir}/texmf-dist/texmf-dist/tex/latex/bookshelf/bookshelf.cls
