import socket
import pickle
from person import Person


SERVER = ('127.0.0.1', 61100)
TCP_PROTO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_PROTO.connect(SERVER)

while True:
    name = input('Name: ')
    age = input('Age: ')
    sex = input('Sex: ')
    msg = pickle.dumps(
        Person(name, age, sex), protocol=pickle.HIGHEST_PROTOCOL
    )
    TCP_PROTO.send(msg)
    resp = TCP_PROTO.recv(1024)
    print(resp.decode('utf-8'))

    if input('Press 0 to exit or Enter to continue') == '0':
        break
