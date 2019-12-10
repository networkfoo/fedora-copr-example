# Spec file Preamble
Name:    fedora-copr-example
Version: 1.0.0
Release: 1%{?dist}
Summary: RPM to test Fedora Copr Build System with Patch

License: GPLv2+
URL:     https://github.com/networkfoo/fedora-copr-example
Source0: https://www.deathorglory.cc/fedora-copr-example-1.0.0.tar.gz
Patch0:  fedora-copr-example-1.0.0.patch

BuildRequires:  gcc

# What this package does.
%description
Simple program to demonstrate Fedora Copr build system. This build demonstrates how to patch the src code.


# These are instructions to prepare sources for the build.
%prep
%setup -q
%patch0 -p1

# These are instructions to build the package.
%build
make %{?_smp_mflags}


# This installs package into system after it has been been built.
# Invoked e.g. by `dnf install example`.
%install
install -d %{buildroot}%{_bindir}
cp -a fedora-copr-example %{buildroot}%{_bindir}/fedora-copr-example


# Here you should list all the files the package provides.
%files
%doc
%{_bindir}/fedora-copr-example

# What has changed since the last version. High level overview
# over the last commits.
%changelog
* Sun Oct 13 2019 philip <philip@pbdigital.org> 1.0.0-1
- Initial version
