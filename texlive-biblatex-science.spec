%global tl_name biblatex-science
%global tl_revision 48945

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	BibLaTeX implementation of the Science bibliography style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-science
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers styles that allow authors to use BibLaTeX when
preparing papers for submission to the journal Science.

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
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-science
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-science
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-science/LICENSE.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-science/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-science/biblatex-science.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-science/biblatex-science.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-science/biblatex-science.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-science/science.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-science/science.cbx
