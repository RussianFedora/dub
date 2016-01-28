Summary:        The D package manager
Name:           dub
Version:        0.9.24
Release:        1%{?dist}

License:        MIT
URL:            https://github.com/D-Programming-Language/dub
# https://github.com/D-Programming-Language/%%{name}/releases/tag/v%%{version}
Source0:        https://github.com/rejectedsoftware/%{name}/archive/v%{version}.tar.gz

BuildRequires:  ldc-phobos-devel
BuildRequires:  pkgconfig(libcurl)

# https://github.com/ldc-developers/ldc/issues/613
ExcludeArch:    %{arm}

%description
The project's philosophy is to keep things as simple as possible. All that is
needed to make a project a dub package is to write a short dub.json file and
put the source code into a source subfolder. It can then be registered on the
public package registry to be made available for everyone. Any dependencies
specified in dub.json are automatically downloaded and made available to the
project during the build process.

%prep
%setup -q

%build
ldmd2 -L-lcurl -ofbin/dub -w -version=DubUseCurl -Isource $* $LIBS @build-files.txt

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/dub %{buildroot}%{_bindir}

%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_bindir}/dub

%changelog
* Thu Jan 28 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 0.9.24-1.R
- clean up spec

* Sun Sep 20 2015 Jonathan MERCIER <bioinfornatics@gmail.com> - 0.9.24-1
- Release 0.9.24

