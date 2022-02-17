#!/usr/bin/env python3 
#RUN AS SUDO SU - GVM

import os 

url = 'https://github.com/greenbone/'
def get_package(url, filename, version):
    os.system("wget " + url + filename + "/archive/refs/tags/" + version + ".zip")
    os.system("unzip " + version + ".zip")
    os.system("rm *.zip")
    os.system("mv *21* " + filename)


os.chdir("/tmp/gvm-source")





get_package(url, "gvm-libs", "v21.4.2")
get_package(url, "openvas-scanner", "v21.4.2")
get_package(url, "ospd", "v21.4.3")
get_package(url, "ospd-openvas", "v21.4.2")
get_package(url, "gvmd", "v21.4.3")
get_package(url, "gsa", "v21.4.2")
get_package(url, "openvas-smb", "v21.4.0")





