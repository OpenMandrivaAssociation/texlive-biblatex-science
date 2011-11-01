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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/biblatex-science/biblatex-science.bib
%{_texmfdistdir}/tex/latex/biblatex-science/science.bbx
%{_texmfdistdir}/tex/latex/biblatex-science/science.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-science/README
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
