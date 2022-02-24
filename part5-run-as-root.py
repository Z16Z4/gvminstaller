#!/usr/bin/env python3 
#run as root part 4
import os
os.system("bash ./part4-set-export.sh")
#MAKE GVM LIBS
os.chdir("/tmp/gvm-source/gvm-libs")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")

#MAKE OPENVAS-SMB
os.chdir("/tmp/gvm-source/openvas-smb")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make install")



#MAKE OPENVAS 
os.chdir("/tmp/gvm-source/")
os.system("mv openvas-scanner/ openvas")
os.chdir("openvas")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")

#MAKE GVMD
os.chdir("/tmp/gvm-source/gvmd")
os.system("mkdir build")
os.system("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")
#look at default gsad.service /lib/systemd/system/gsad.service $£$$%$*%£$*£@($£($*£($*£$*(£*))))

#MAKE GSA
os.chdir("/tmp/gvm-source/gsa")
os.system("mkdir build")
os.chdir("build")
os.system("cmake .. -DCMAKE_INSTALL_PREFIX=/opt/gvm -DCMAKE_BUILD_TYPE=RELEASE")
os.system("make")
os.system("make doc")
os.system("make install")

#MAKE OSPD
os.chdir("/tmp/gvm-source/ospd")
os.system("pip3 install . --prefix=/opt/gvm")


#configuration
os.system("cp /tmp/gvm-source/openvas/config/redis-openvas.conf /etc/redis")
os.system("chown redis:redis /etc/redis/redis-openvas.conf")
 
os.system("sudo ldconfig")
os.system("echo 'db_address = /run/redis-openvas/redis.sock' > /etc/openvas/openvas.conf")
os.system("chown gvm:gvm /opt/gvm/etc/openvas/openvas.conf")
os.system("usermod -aG redis gvm")
#start redis
os.system("systemctl start redis-server@openvas")
os.system("systemctl enable redis-server@openvas")
os.system("echo 'net.core.somaxconn = 1024' >> /etc/sysctl.conf")
os.system("echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf")
os.system("sysctl -p")

