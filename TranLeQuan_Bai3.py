import base64

base64_message = 'Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)