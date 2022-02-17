#!/usr/bin/env python3 
#run as root part 4

import os 
#MAKE GVM LIBS
os.chdir("/tmp/gvm-source/gvm-libs")
os.system("export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")

#MAKE OPENVAS-SMB
os.chdir("/tmp/gvm-source/openvas-smb")
os.system("export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make install")



#MAKE OPENVAS 
os.chdir("/tmp/gvm-source/")
os.system("mv openvas-scanner/ openvas")
os.chdir("openvas")
os.system("export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH")
os.system("mkdir build")
os.chdir("build")
os.system("sed -i 's/set (CMAKE_C_FLAGS_DEBUG\s.*\"\${​​​CMAKE_C_FLAGS_DEBUG}​​​​​​​​​​ \${​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​COVERAGE_FLAGS}​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​\")/set (CMAKE_C_FLAGS_DEBUG \"\${​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​CMAKE_C_FLAGS_DEBUG}​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ -Werror -Wno-error=deprecated-declarations\")/g' ../../openvas/CMakeLists.txt")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")


#Configuration of Openvas and redis server
os.system("cp /tmp/gvm-source/openvas-scanner/config/redis-openvas.conf /etc/redis")
os.system("chown redis:redis /etc/redis/redis-openvas.conf")