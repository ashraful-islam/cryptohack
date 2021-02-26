msg = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
msg = bytes.fromhex(msg).decode('utf-8')
msg = [ ord(x) for x in msg ]
dec = msg[:7] # should be 'crypto{'

s_key = None
for i in range(256):
    check = ''.join([ chr(x^i) for x in dec ])
    if check == 'crypto{':
        s_key = i
        break

flag = ''.join([ chr(x^s_key) for x in msg ])

print(flag)