#!/usr/bin/env python3 
#RUN AS REGULAR USER    
import os 
os.system("sudo -Hiu postgres createuser gvm")
os.system("sudo -Hiu postgres createdb -O gvm gvmd")
os.system("sudo -Hiu postgres psql -c 'create role dba with superuser noinherit;' gvmd")
os.system("sudo -Hiu postgres psql -c 'grant dba to gvm;' gvmd")
os.system('''sudo -Hiu postgres psql -c 'create extension "uuid-ossp";' gvmd''')
os.system('''sudo -Hiu postgres psql -c 'create extension "pgcrypto";' gvmd''')
os.system("systemctl restart postgresql")
os.system("sudo systemctl restart postgresql")
os.system("systemctl enable postgresql")
os.system("sudo systemctl enable postgresql")
os.system("sudo cp -r run-as-gvm.py /opt/gvm")
