print ('netcheck auto run')
import os
import socket
name=socket.gethostname()
print ('executing php server')
print ('$ php -S 0.0.0.0:8080')
print ('web in '+socket.gethostbyname(name)+':8080')
os.system('php -S 0.0.0.0:8080')
