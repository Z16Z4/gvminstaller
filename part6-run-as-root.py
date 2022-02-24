#!/usr/bin/env python3


import os 

os.system("gvm-manage-certs -a")
os.system("greenbone-nvt-sync")
os.system("greenbone-feed-sync --type SCAP")
os.system("gvmd --create-user=admin --password=letmein")
os.system("gvmd --get-users --verbose")
os.system("gvmd --modify-setting 78eceaec-3385-11ea-b237-28d24461215b --value 27790287-41de-49d3-be6e-daaec30348eb")



#Feed sync

os.system("greenbone-feed-sync --type GVMD_DATA")
os.system("greenbone-feed-sync --type SCAP")
os.system("greenbone-feed-sync --type CERT")

