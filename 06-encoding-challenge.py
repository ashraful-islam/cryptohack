import telnetlib
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def decode_base64(hsh):
    return base64.b64decode(hsh).decode('utf-8')

def decode_hex(hsh):
    return bytes.fromhex(hsh).decode('utf-8')

def decode_rot13(hsh):
    return codecs.decode(hsh, 'rot13')

def decode_bigint(hsh):
    return decode_hex(hsh.lstrip('0x'))

def decode_utf8(hsh):
    return ''.join([ chr(n) for n in hsh ])

def decode_msg(enc, hsh):
    if enc == 'base64': return decode_base64(hsh)
    if enc == 'hex': return decode_hex(hsh)
    if enc == 'rot13': return decode_rot13(hsh)
    if enc == 'bigint': return decode_bigint(hsh)
    if enc == 'utf-8': return decode_utf8(hsh)
    return ''

while True:
    resp = json_recv()

    if 'flag' in resp:
        print(f"Flag Found: {resp['flag']}")
        break

    enc = resp['type']
    val = resp['encoded']
    #print(f"{enc} => {val}")
    to_send = {
        "decoded": decode_msg(enc, val)
    }
    json_send(to_send)

