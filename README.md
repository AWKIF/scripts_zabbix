#DUPDATE.PY

####Permet de disable le monitoring d'un host zabbix.

####Allow to disable monitoring on a zabbix host

####You need:

yum install epel-release (necessary if you don't find the below packages)

yum install python

yum install python-pip

####Then install

pip install pyzabbix

####Usage:

./dupdate.py --url http://zabbix_url/ --user XXXX --password XXXXX --disable X --hostname XXXXXX

1 to disable - 0 to enable


#INTUPDATE.PY

####Permet de modifier l'ip du host dans zabbix

####Allow to change ip of an host in zabbix

####You need:

pyzabbix library like above

####Usage:

./intupdate.py --url http://zabbix_url/ --user XXXX --password XXXX --ip X.X.X.X --hostname XXXX
