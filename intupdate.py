#!/usr/bin/python
import sys
import argparse
import logging
from pyzabbix import ZabbixAPI


#Uncomment for Debugging JSON w json request
#stream = logging.StreamHandler(sys.stdout)
#stream.setLevel(logging.DEBUG)
#log = logging.getLogger('pyzabbix')
#log.addHandler(stream)
#log.setLevel(logging.DEBUG)


parser = argparse.ArgumentParser(description='This is a simple tool to update monitored status of an host')
parser.add_argument('--url', help='URL to the zabbix server',required = True)
parser.add_argument('--user', help='The zabbix api user',required = True)
parser.add_argument('--password', help='The zabbix api password',required = True)
parser.add_argument('--ip', help='Disable monitoring on host, 1 = disabled',required = True)
parser.add_argument('--hostname', help='The zabbix hostname you want to update',required = True)

args = parser.parse_args()


if None == args.url :
  print "Error: Missing --url\n\n"
  exit(2)

if None == args.user :
  print "Error: Missing --user\n\n"
  exit(3)

if None == args.password :
  print "Error: Missing --password\n\n"
  exit(4)

if None == args.ip :
  print "Error: Missing --enable\n\n"
  exit(4)

if None == args.hostname :
  print "Error: Missing --hostname\n\n"
  exit(4)

zapi = ZabbixAPI(args.url)
zapi.login(args.user, args.password)
print "Connected to Zabbix API Version %s" % zapi.api_version()



for h in zapi.host.get(output="extend", filter={"host":[args.hostname]}):

	myhostid=h['hostid']

for i in zapi.hostinterface.get(output="extend", hostids=myhostid):

	print "Updating hostname: " + h['name'] + " -HostId: " + h['hostid'] + " -InterfaceId: " + i['interfaceid'] + " -CurrentIp: " + i['ip']

	myinterfaceid=i['interfaceid']

try:
	zapi.hostinterface.update(interfaceid=myinterfaceid, ip=args.ip)
except ZabbixAPIException as e:
	print(e)

print "Success - new ip is " + args.ip
