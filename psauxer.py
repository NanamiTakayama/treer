import datetime
import time
import subprocess
from time import sleep

cmd = ["ps", "aux"]

while True:
    dt_now = datetime.datetime.now()
    returncode = subprocess.call(cmd)
    print(dt_now)
    sleep(15)
