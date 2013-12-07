# revision 28970
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-science
# catalog-date 2013-01-28 09:21:48 +0100
# catalog-license lppl
# catalog-version 1.1d
Name:		texlive-biblatex-science
Version:	1.1d
Release:	5
Summary:	Biblatex implementation of the Science bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-science
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-science.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Science.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-science/science.bbx
%{_texmfdistdir}/tex/latex/biblatex-science/science.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-science/README
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
