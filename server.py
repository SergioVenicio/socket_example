import socket
import _thread
import pickle
from pathlib import Path

SERVER = ('127.0.0.1', 61100)


def connect(con, client):
    __write_mode__ = 'a'

    DB = 'database.HUE'

    if not Path(DB).exists():
        __write_mode__ = 'w'

    print(f'Connected with {client}')

    resp = b'OK'

    while True:
        msg = con.recv(2048)

        if not msg:
            break

        p = pickle.loads(msg)

        if not p.name or not p.age or not p.sex:
            resp = b'Err'
        else:
            with open('database.HUE', __write_mode__) as _file:
                new_line = f'{p.name} | {p.age} | {p.sex} \n'
                _file.write(new_line)
                if __write_mode__ == 'w':
                    __write_mode__ = 'a'

        con.send(resp)

        print(client, p)
    print(f'Close connection...')

    con.close()
    _thread.exit()


TCP_PROTO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_PROTO.bind(SERVER)
TCP_PROTO.listen(1)

while True:
    con, client = TCP_PROTO.accept()
    _thread.start_new_thread(connect, tuple([con, client]))
