# revision 21721
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-science
# catalog-date 2011-03-13 14:25:22 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-biblatex-science
Version:	1.1
Release:	1
Summary:	Biblatex support for Science
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-science
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Science.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/biblatex-science/biblatex-science.bib
%{_texmfdistdir}/tex/latex/biblatex-science/science.bbx
%{_texmfdistdir}/tex/latex/biblatex-science/science.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-science/README
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
