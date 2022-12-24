#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xstatic_objectpath
Version  : 1.2.1.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/23/6c/56de25d9d3be430e7de2fcf4baac10279dad78d7b16cbda339cf014c2fe5/XStatic-objectpath-1.2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/6c/56de25d9d3be430e7de2fcf4baac10279dad78d7b16cbda339cf014c2fe5/XStatic-objectpath-1.2.1.0.tar.gz
Summary  : objectpath 1.2.1 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: pypi-xstatic_objectpath-python = %{version}-%{release}
Requires: pypi-xstatic_objectpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
---------------
        
        Angular JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the pypi-xstatic_objectpath package.
Group: Default
Requires: pypi-xstatic_objectpath-python3 = %{version}-%{release}

%description python
python components for the pypi-xstatic_objectpath package.


%package python3
Summary: python3 components for the pypi-xstatic_objectpath package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_objectpath)

%description python3
python3 components for the pypi-xstatic_objectpath package.


%prep
%setup -q -n XStatic-objectpath-1.2.1.0
cd %{_builddir}/XStatic-objectpath-1.2.1.0
pushd ..
cp -a XStatic-objectpath-1.2.1.0 buildavx2
cp -a XStatic-objectpath-1.2.1.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671855299
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
