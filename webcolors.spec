#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : webcolors
Version  : 1.7
Release  : 12
URL      : http://pypi.debian.net/webcolors/webcolors-1.7.tar.gz
Source0  : http://pypi.debian.net/webcolors/webcolors-1.7.tar.gz
Source99 : http://pypi.debian.net/webcolors/webcolors-1.7.tar.gz.asc
Summary  : A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webcolors-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://travis-ci.org/ubernostrum/webcolors.svg?branch=master
:target: https://travis-ci.org/ubernostrum/webcolors

%package python
Summary: python components for the webcolors package.
Group: Default

%description python
python components for the webcolors package.


%prep
%setup -q -n webcolors-1.7

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488473600
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488473600
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
