# revision 28888
# category Package
# catalog-ctan /fonts/latex
# catalog-date 2012-07-07 15:54:01 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-latex-fonts
Version:	20120707
Release:	1
Summary:	A collection of fonts used in LaTeX distributions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/latex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a collection of fonts for use with standard latex
packages and classes. It includes 'invisible' fonts (for use
with the slides class), line and circle fonts (for use in the
picture environment) and 'latex symbol' fonts. For full support
of a latex installation, some Computer Modern font variants
cmbsy(6-9), cmcsc(8,9), cmex(7-9) and cmmib(5-9) from the
amsfonts distribution, are also necessary. The fonts are
available as Metafont source, and metric (tfm) files are also
provided. Most of the fonts are also available in Adobe Type 1
format, in the amsfonts distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/latex-fonts/circle.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/icmcsc10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/icmex10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/icmmi8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/icmsy8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/icmtt8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/ilasy8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/ilcmss8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/ilcmssb8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/ilcmssi8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy5.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy6.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy7.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasy9.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lasyb10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lcircle10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lcirclew10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lcmss8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lcmssb8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/lcmssi8.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/line.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/line10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/linew10.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/sroman.mf
%{_texmfdistdir}/fonts/source/public/latex-fonts/sromanu.mf
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/icmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/icmex10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/icmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/icmsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/icmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/ilasy8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/ilcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/ilcmssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/ilcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy5.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy6.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy7.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasy9.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lasyb10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lcircle10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lcirclew10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lcmssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/lcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/line10.tfm
%{_texmfdistdir}/fonts/tfm/public/latex-fonts/linew10.tfm
%doc %{_texmfdistdir}/doc/fonts/latex-fonts/README
%doc %{_texmfdistdir}/doc/fonts/latex-fonts/legal.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
