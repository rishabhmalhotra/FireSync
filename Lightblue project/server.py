import socket
## Aditya is the server -- This is the

'''s = socket.socket()
host = socket.gethostname()

# Reserve a port for your service.
port = 0
# Bind to the port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", port))

# Now wait for client connection.
s.listen(10)
conn, addr = s.accept()
    while True:
        # connection, address
        content = conn.recv(1024)
        if content in ('status', 'stop', 'start', 'reload', 'restart'):
            conn.send ('%s received' % content)
        else:
            conn.send ('Invalid command')'''

'''from lightblue_1 import *

s = socket()
s.bind(("", 0))
s.listen(1)
advertise("My RFCOMM File", s, RFCOMM)
conn, addr = s.accept()
print "Connected by", addr
conn.recv(1024)
conn.close()
s.close()

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)'''

# speak out text:

import os
os.system("echo 'hello world'")
os.system("say 'hello world'")