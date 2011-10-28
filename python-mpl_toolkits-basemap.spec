%define tarname basemap
%define name	python-mpl_toolkits-%{tarname}
%define version 1.0
%define release 3

Summary:	Python package for plotting on map projections
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://matplotlib.sourceforge.net/basemap/doc/html/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-matplotlib >= 0.98
Requires:	python-numpy >= 1.1
Requires:	python-httplib2
Suggests:	python-imaging
BuildRequires:	python-devel
BuildRequires:	python-matplotlib >= 0.98
BuildRequires:	geos-devel >= 3.1.1
BuildRequires:	python-numpy-devel >= 1.1
BuildRequires:	python-httplib2

%description
The matplotlib basemap toolkit is a library for plotting 2D data on
maps in Python. It is similar in functionality to the matlab mapping
toolbox, the IDL mapping facilities, GrADS, or the Generic Mapping
Tools. PyNGL and CDAT are other libraries that provide similar
capabilities in Python.

Basemap does not do any plotting on it’s own, but provides the
facilities to transform coordinates to one of 23 different map
projections (using the PROJ.4 C library). Matplotlib is then used to
plot contours, images, vectors, lines or points in the transformed
coordinates. Shoreline, river and political boundary datasets (from
Generic Mapping Tools) are provided, along with methods for plotting
them. The GEOS library is used internally to clip the coastline and
polticial boundary features to the desired map projection region.

Basemap provides facilities for reading data in netCDF and Shapefile
formats, as well as directly over http using OPeNDAP. This
functionality is provided through the PyDAP client, and a python
interface to the Shapefile C library.

%prep
%setup -q -n %{tarname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%__rm -rf %{buildroot}%{py_platsitedir}/mpl_toolkits/__init__.*

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples/ Changelog FAQ LICENSE* README
%py_platsitedir/*
