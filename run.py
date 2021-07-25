import socket
import sys
import subprocess
import time
import os
import getpass

user=getpass.getuser()
path=os.getcwd()
name=socket.gethostname()

print ('<title>netcheck</title>')
banner='''
                   88b 88 888888 888888  dP""b8 88  88 888888  dP""b8 88  dP
                   88Yb88 88__     88   dP   `" 88  88 88__   dP   `" 88odP
                   88 Y88 88""     88   Yb      888888 88""   Yb      88"Yb
                   88  Y8 888888   88    YboodP 88  88 888888  YboodP 88  Yb (⌐■_■)


'''
print (banner)
iface='wlan0'
mode='scanning'
aaa = subprocess.Popen('iwconfig '+iface+' | grep level', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
inf = aaa.stderr.read()+aaa.stdout.read()
slu = (inf[:49])
signallvl = (slu[43:].decode())
time.sleep(1)
print (f'<h3><font color="red">                netcheck</font>          mode: <font color="yellow">{mode}</font>      power: <font color="green">-{signallvl}</font></h3>')
print ('<h3>                ═════════════════════════════════════════════════════</h3>')
print ('')
print ('<h3>pinging net (<font color="yellow">1.1.1.1</font>)... </h3>')
nowping = subprocess.Popen('ping -c 1 1.1.1.1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
ping = nowping.stderr.read()+nowping.stdout.read()
print ('<h3><font color="red">'+user+'@'+name+'<font color="black">:<font color="blue">'+path+'</font>$ <font color="green">',ping.decode()+'</font></h3>')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('')
print ('                                      netcheck made by 0xK1r4')
