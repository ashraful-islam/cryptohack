#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

if __name__ == '__main__':
    # read and discard welcome message
    for _ in range(4):
        readline()

    json_send({ "buy": "flag" })
    response = json_recv()
    print(response)
