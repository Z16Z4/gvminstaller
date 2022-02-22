#!/bin/bash

wget https://github.com/greenbone/gvm-libs/archive/refs/tags/v21.4.2.zip
unzip v21.4.2.zip
rm *.zip
mv *21* gvm-libs

wget https://github.com/greenbone/openvas-scanner/archive/refs/tags/v21.4.2.zip
unzip v21.4.2.zip
rm *.zip
mv *21* openvas
wget https://github.com/greenbone/ospd/archive/refs/tags/v21.4.3.zip
unzip v21.4.3.zip
rm *.zip
mv *21* ospd
wget https://github.com/greenbone/ospd-openvas/archive/refs/tags/v21.4.2.zip
unzip v21.4.2.zip
rm *.zip
mv *21* ospd-openvas
wget https://github.com/greenbone/gvmd/archive/refs/tags/v21.4.3.zip
unzip v21.4.3.zip
rm *.zip
mv *21* gvmd
wget https://github.com/greenbone/gsa/archive/refs/tags/v21.4.2.zip
unzip v21.4.2.zip
rm *.zip
mv *21* gsa
wget https://github.com/greenbone/openvas-smb/archive/refs/tags/v21.4.0.zip
unzip v21.4.0.zip
rm *.zip
mv *21* openvas-smb

sudo mv -r gvm-libs /tmp/gvm-source
sudo mv -r openvas /tmp/gvm-source
sudo mv -r ospd /tmp/gvm-source
sudo mv -r ospd-openvas /tmp/gvm-source
sudo mv -r gvmd /tmp/gvm-source
sudo mv -r gsa /tmp/gvm-source
sudo mv -r openvas-smb /tmp/gvm-source

