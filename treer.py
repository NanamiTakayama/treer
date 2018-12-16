import datetime
import time
import subprocess
from time import sleep

cmd1 = "pwd"
cmd2 = "tree"

file = open('new.txt','a')
file.write('new file\n')

while True:
    print(datetime.datetime.now())
    subprocess.call(cmd1)
    subprocess.call(cmd2)
    sleep(15)
