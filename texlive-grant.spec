Name:		texlive-grant
Version:	56852
Release:	2
Summary:	Classes for formatting federal grant proposals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grant
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grant.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grant.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grant.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX classes for formatting federal grant proposals: grant:
Base class for formatting grant proposals grant-arl: Army
Research Laboratory grant-darpa: Defense Advanced Research
Projects Agency grant-doe: Department of Energy grant-nih:
National Institutes of Health grant-nrl: Naval Research
Laboratory grant-nsf: National Science Foundation grant-onr:
Office of Naval Research

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/grant
%{_texmfdistdir}/tex/latex/grant
%doc %{_texmfdistdir}/doc/latex/grant

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
