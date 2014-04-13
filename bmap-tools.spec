Summary:	Tools to generate block map (AKA bmap) and flash images using bmap
Summary(pl.UTF-8):	Narzędzia do generowania mapy bloków (bmap) i obrazów flash przy użyciu bmap
Name:		bmap-tools
Version:	3.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	ftp://ftp.infradead.org/pub/bmap-tools/%{name}-%{version}.tgz
# Source0-md5:	92cdad1cb4dfa0cca7176c8e22752616
URL:		https://source.tizen.org/documentation/reference/bmaptool
BuildRequires:	python-distribute
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.7
Requires:	python-pygpgme
Suggests:	gzip
Suggests:	lzop
Suggests:	pbzip2
Suggests:	pigz
Suggests:	tar
Suggests:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bmap-tools - tools to generate block map (AKA bmap) and flash images
using bmap. Bmaptool is a generic tool for creating the block map
(bmap) for a file, and copying files using the block map. The idea is
that large file containing unused blocks, like raw system image files,
can be copied or flashed a lot faster with bmaptool than with
traditional tools like "dd" or "cp".

%description -l pl.UTF-8
Bmap-tools to narzędzia do generowania map bloków (bmap) oraz obrazów
flash przy użyciu bmap. Bmaptool to ogólne narzędzie do tworzenia map
bloków (bmap) dla pliku oraz kopiowania plików przy użyciu tych map.
Idea jest taka, że duże pliki zawierające nie używane bloki, jak np.
pliki surowych obrazów systemu, można kopiować lub nagrywać na pamięć
flash dużo szybciej przy użyciu bmaptool niż za pomocą tradycyjnych
narzędzi, takich jak "dd" lub "cp".

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

install -D docs/man1/bmaptool.1 $RPM_BUILD_ROOT%{_mandir}/man1/bmaptool.1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{README,RELEASE_NOTES} TODO
%attr(755,root,root) %{_bindir}/bmaptool
%{_mandir}/man1/bmaptool.1*
%dir %{py_sitescriptdir}/bmaptools
%{py_sitescriptdir}/bmaptools/*.py[co]
%{py_sitescriptdir}/bmap_tools-%{version}-py*.egg-info
