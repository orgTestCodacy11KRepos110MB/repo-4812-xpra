# This file is part of Xpra.
# Copyright (C) 2015-2021 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

%{!?__python2: %global __python2 python2}
%{!?python2_sitelib: %define python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define _disable_source_fetch 0

#this is a pure python package so debug is meaningless here:
%define debug_package %{nil}

Name:           python2-pynvml
Version:        11.460.79
Release:        1
URL:            http://pythonhosted.org/nvidia-ml-py/
Summary:        Python wrapper for NVML
License:        BSD
Group:          Development/Libraries/Python
Source:        	https://files.pythonhosted.org/packages/3a/14/32e32856e62422655dfe115c8c421a304e87330dadbab72fc5534a9fd5c6/nvidia-ml-py-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       python-pynvml

%description
Python Bindings for the NVIDIA Management Library

%prep
sha256=`sha256sum %{SOURCE0} | awk '{print $1}'`
if [ "${sha256}" != "5b7c051cd55469848960bb9fde07dc8fd25d21853307eeba669bfe3c3ede11c5" ]; then
	echo "invalid checksum for %{SOURCE0}"
	exit 1
fi
%setup -q -n nvidia-ml-py-%{version}

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -f %{buildroot}/%{python2_sitelib}/__pycache__/example.*
rm -f %{buildroot}/%{python2_sitelib}/example.py*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python2_sitelib}/pynvml.py*
%{python2_sitelib}/nvidia_ml_py-%{version}-py*.egg-info

%changelog
* Sat Jul 24 2021 Antoine Martin <antoine@xpra.org> - 11.460.79-1
- new upstream release

* Tue May 25 2021 Antoine Martin <antoine@xpra.org> - 11.450.51-1
- new upstream release

* Fri Dec 06 2019 Antoine Martin <antoine@xpra.org> - 10.418.84-1
- new upstream release

* Wed Sep 25 2019 Antoine Martin <antoine@xpra.org> - 7.352.0-3
- build pynvml for python3 on centos8

* Tue Jul 18 2017 Antoine Martin <antoine@xpra.org> - 7.352.0-2
- build python3 variant too

* Mon Aug 29 2016 Antoine Martin <antoine@xpra.org> - 7.352.0-1
- build newer version

* Fri Aug 05 2016 Antoine Martin <antoine@xpra.org> - 4.304.04-1
- initial packaging