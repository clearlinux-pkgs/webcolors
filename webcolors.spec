#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : webcolors
Version  : 1.8.1
Release  : 28
URL      : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz
Source0  : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz
Source99 : http://pypi.debian.net/webcolors/webcolors-1.8.1.tar.gz.asc
Summary  : A library for working with color names and color values formats defined by HTML and CSS.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webcolors-python3
Requires: webcolors-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://travis-ci.org/ubernostrum/webcolors.svg?branch=master
:target: https://travis-ci.org/ubernostrum/webcolors

%package legacypython
Summary: legacypython components for the webcolors package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the webcolors package.


%package python
Summary: python components for the webcolors package.
Group: Default
Requires: webcolors-python3

%description python
python components for the webcolors package.


%package python3
Summary: python3 components for the webcolors package.
Group: Default
Requires: python3-core

%description python3
python3 components for the webcolors package.


%prep
%setup -q -n webcolors-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519351146
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519351146
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
