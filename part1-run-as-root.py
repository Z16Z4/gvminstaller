#!/usr/bin/env python3 


# RUN AS SUDO SU

import os 
os.system("sudo apt-get update;sudo apt-get upgrade; sudo apt update; sudo apt upgrade")
os.system("sudo apt install unzip")
#Update system
os.system("sudo curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -")
os.system('''echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list''')
os.system("sudo apt update")

#Install yarn as root
os.system("sudo apt install yarn -y; sudo yarn install; sudo yarn upgrade")

#Get postgresql
os.system("sudo apt-get -y install postgresql postgresql-contrib postgresql-server-dev-all")
os.system("sudo systemctl restart postgresql")

#Add gvm user 
os.system('''useradd -r -d /opt/gvm -c "GVM (OpenVAS) User" -s /bin/bash gvm''')
os.system("mkdir /opt/gvm")
os.system("chown gvm:gvm /opt/gvm")
os.system("apt-get -y install gcc g++ make bison flex libksba-dev curl redis libpcap-dev cmake git pkg-config libglib2.0-dev libgpgme-dev libgnutls28-dev uuid-dev libssh-gcrypt-dev libldap2-dev gnutls-bin libmicrohttpd-dev libhiredis-dev zlib1g-dev libxml2-dev libradcli-dev libldap2-dev doxygen nmap gcc-mingw-w64 xml-twig-tools libical-dev perl-base heimdal-dev libpopt-dev libsnmp-dev python3-setuptools python3-paramiko python3-lxml python3-defusedxml python3-dev gettext python3-polib xmltoman python3-pip texlive-fonts-recommended xsltproc texlive-latex-extra rsync ufw ntp libunistring-dev git libnet1-dev graphviz graphviz-dev --no-install-recommends")
os.system('''sed -i 's/\"$/\:\/opt\/gvm\/bin\:\/opt\/gvm\/sbin\:\/opt\/gvm\/\.local\/bin\"/g' /etc/environment''')
os.system('sudo echo "/opt/gvm/lib" > /etc/ld.so.conf.d/gvm.conf')
