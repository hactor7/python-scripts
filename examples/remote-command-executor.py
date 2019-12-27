#!/usr/bin/python
# pip install paramiko
# check for help with python paramiko_example.py --help
# python remote-command-executor.py  /home/delhivery/.ssh/done-key.pem  52.70.172.225 ubuntu 'sudo netstat -tunlp'
# Or crate a alias first
# alias runc='python /path/to/remote-command-executor.py'
# 


import paramiko
import optparse
import getpass
import time

parser = optparse.OptionParser()

parser.add_option('-i', '--identity-key', action="store", dest="key",help="SSH key for access", default='/home/' + getpass.getuser() + '/.ssh/id_rsa')
parser.add_option('-H', '--host', action="store", dest="host",help="Target hostname like localhost", default="localhost")
parser.add_option('-u', '--user', action="store", dest="user",help="Target username like ubuntu", default="ubuntu")
parser.add_option('-s', '--script', action="store", dest="script",help="Script to run on target server.", default="ls -al")

options, args = parser.parse_args()

keypath = options.key
hostname = options.host
username = options.user
scripttorun = options.script 



k = paramiko.RSAKey.from_private_key_file(keypath)
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting to " + hostname)
print(".........                          (33%)\r")
time.sleep(1)
print("......................             (66%)\r")
time.sleep(1)
print("...................................(100%)\r")
c.connect( hostname = hostname, username = username, pkey = k )
print("Connected :) ")
print("")
commands = [ scripttorun ]
for command in commands:
	print("Executing: {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	print(stdout.read().decode())
	print( "Errors")
	print(stderr.read().decode())
c.close()

