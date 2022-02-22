#!/bin/bash 
sudo -Hiu postgres createuser gvm
sudo -Hiu postgres createdb -O gvm gvmd
sudo -Hiu postgres psql -c 'create role dba with superuser noinherit;' gvmd
sudo -Hiu postgres psql -c 'grant dba to gvm;' gvmd
sudo -Hiu postgres psql -c 'create extension "uuid-ossp";' gvmd
sudo -Hiu postgres psql -c 'create extension "pgcrypto";' gvmd
systemctl restart postgresql
sudo systemctl restart postgresql
systemctl enable postgresql
sudo systemctl enable postgresql
sudo cp -r part3-run-as-gvm.py /opt/gvm
sudo mkdir /opt/gvm/src
sudo mkdir /tmp/gvm-source
sudo mkdir /opt/gvm/src
sudo chown gvm:gvm /opt/gvm/src
sudo chown gvm:gvm /opt/gvm
sudo chown gvm:gvm /tmp/gvm-source
