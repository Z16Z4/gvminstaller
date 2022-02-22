#!/bin/bash
#run as root part 4
cd /tmp/gvm-source
exec bash
#MAKE GVM LIBS
cd /tmp/gvm-source/gvm-libs
exec bash
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
mkdir build
cd build
exec bash
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE
make
make doc
make install


#MAKE OPENVAS SMB
cd /tmp/gvm-source/openvas-smb
exec bash
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
mkdir build
cd build
exec bash
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE
make
make install



#MAKE OPENVAS 
cd /tmp/gvm-source/openvas
exec bash
export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH
mkdir build
cd build
exec bash
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE
make
make doc
make install


#Configuration of Openvas and redis server
cp /tmp/gvm-source/openvas/config/redis-openvas.conf /etc/redis
chown redis:redis /etc/redis/redis-openvas.conf
