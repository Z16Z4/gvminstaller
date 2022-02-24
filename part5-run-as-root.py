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


#Configuration of Openvas and redis server
os.system("cp /tmp/gvm-source/openvas/config/redis-openvas.conf /etc/redis")
os.system("chown redis:redis /etc/redis/redis-openvas.conf")

#Ldconfig

os.system("sudo ldconfig; ")