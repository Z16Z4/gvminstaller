#!/usr/bin/env python3 
#run as root part 4

import os 

os.system("sudo ldconfig")
os.system("cp /tmp/gvm-source/openvas-scanner/redis-openvas.conf /etc/redis")
os.system("sudo chown redis:redis /etc/redis/redis-oepnvas.conf")

os.chdir("/tmp/gvm-source/gvm-libs")
os.system("export PKG_CONFIG_PATH=/opt/gvm/lib/pkgconfig:$PKG_CONFIG_PATH")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make install")
