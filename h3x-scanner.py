import socket
import time
import threading
from queue import Queue
from colorama import Fore,Back
import os 
import platform


# check os type
data0 = platform.uname()[0]

if data0 == "Linux":
    os.system("clear")
elif data0 == "Windows":
    os.system("cls")

# --------------------- banner --------------------------
print(Fore.RED+ f"""

 ██      ██  ████  ██     ██        ████████   ██████      ██     ████     ██
░██     ░██ █░░░ █░░██   ██        ██░░░░░░   ██░░░░██    ████   ░██░██   ░██
░██     ░██░    ░█ ░░██ ██        ░██        ██    ░░    ██░░██  ░██░░██  ░██
░██████████   ███   ░░███    █████░█████████░██         ██  ░░██ ░██ ░░██ ░██
░██░░░░░░██  ░░░ █   ██░██  ░░░░░ ░░░░░░░░██░██        ██████████░██  ░░██░██
░██     ░██ █   ░█  ██ ░░██              ░██░░██    ██░██░░░░░░██░██   ░░████
░██     ░██░ ████  ██   ░░██       ████████  ░░██████ ░██     ░██░██    ░░███
░░      ░░  ░░░░  ░░     ░░       ░░░░░░░░    ░░░░░░  ░░      ░░ ░░      ░░░ 

                                       {Fore.RED}----------------------------
                                        {Fore.CYAN}DEVELOPER: H3X
                                            insta : h3x_code
""")

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

ip_address = input(Fore.RED+'TARGET IP => '+Fore.RESET)
host = socket.gethostbyname(ip_address)
print (Fore.BLUE+'Scanning on IP Address: ', host + Fore.RESET)

def scan(port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = sock.connect((host, port))
      with lock:
         print(Fore.CYAN + f'{port} is open')
      con.close()
   except:
      pass

def execute():
   while True:
      worker = queue.get()
      scan(worker)
      queue.task_done()

queue = Queue()
start_time = time.time()
   
for x in range(100):
   thread = threading.Thread(target = execute)
   thread.daemon = True
   thread.start()
   
for worker in range(1, 500):
   queue.put(worker)
   
queue.join()
print(Fore.RESET)
print("------------------------")
print(Fore.YELLOW+'Time taken:', time.time() - start_time)