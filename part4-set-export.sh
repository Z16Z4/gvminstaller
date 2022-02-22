#!/bin/bash
cd /tmp/gvm-source/gvm-libs
exec bash
mkdir build
cd build
exec bash
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
cd /tmp/gvm-source/openvas-smb
exec bash 
mkdir build
cd build
exec bash
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
cd /tmp/gvm-source
exec bash
mv openvas-scanner openvas
cd openvas
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
exec bash
mkdir build
cd build 
exec bash