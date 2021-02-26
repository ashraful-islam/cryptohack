msg = b'label'
flag = ''.join([ chr(n ^ 13) for n in msg ])
print(f"Flag: {flag}")
