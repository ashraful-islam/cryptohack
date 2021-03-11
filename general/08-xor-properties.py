
k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k1_xor_k2 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
k2_xor_k3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag_xor_k1_xor_k3_xor_k2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# solution
k2 = [ (x^y) for x,y in zip(k1, k1_xor_k2) ]
k3 = [ (x^y) for x,y in zip(k2, k2_xor_k3) ]
flag_xor_k2_xor_k3 = [ (x^y) for x,y in zip(k1, flag_xor_k1_xor_k3_xor_k2) ]
flag_xor_k3 = [ (x^y) for x,y in zip(k2, flag_xor_k2_xor_k3) ]
flag = [ chr(x^y) for x,y in zip(k3, flag_xor_k3) ]
print(''.join(flag))
