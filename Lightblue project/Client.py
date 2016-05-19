## I am the client -- This is the client file you are looking at

import lightblue_1
import sys
import socket
from lightblue_1 import *

user_select = lightblue_1.selectdevice()
user_address = user_select[0]

s = socket()
s.connect((user_address, 5))
s.send("chutiya test 1")
s.close()