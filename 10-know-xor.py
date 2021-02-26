msg = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
msg = [ x for x in msg ]
seek_term = b'crypto{}'
sample = msg[:7] + [msg[-1]]
secret_key = [ (x^y) for x,y in zip(sample, seek_term)]
key_str = ''.join([ chr(x) for x in secret_key ])
print(f'Secret Key: {key_str}')

steps, flag = len(secret_key), ''
for i in range(0, len(msg), steps):
    flag += ''.join( [ chr(x^y) for x,y in zip(secret_key, msg[ i: i + steps ]) ] )

print(flag)