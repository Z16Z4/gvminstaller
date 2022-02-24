#!/usr/bin/env python3

import os


os.system("gvmd --get-scanners")
os.system('gvmd --create-scanner="ST1" --scanner-type="OpenVAS" --scanner-host=/opt/gvm/var/run/ospd.sock')
