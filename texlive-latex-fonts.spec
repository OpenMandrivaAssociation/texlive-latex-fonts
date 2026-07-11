%global tl_name latex-fonts
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A collection of fonts used in LaTeX distributions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/latex
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a collection of fonts for use with standard LaTeX packages and
classes. It includes 'invisible' fonts (for use with the slides class),
line and circle fonts (for use in the picture environment) and 'LaTeX
symbol' fonts. For full support of a LaTeX installation, some Computer
Modern font variants cmbsy(6-9), cmcsc(8,9), cmex(7-9) and cmmib(5-9)
from the amsfonts distribution, are also necessary. The fonts are
available as Metafont source, and metric (tfm) files are also provided.
Most of the fonts are also available in Adobe Type 1 format, in the
amsfonts distribution.

