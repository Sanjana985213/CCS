from Crypto.Cipher import AES
from secrets import token_bytes
key=token_bytes(16)  
cipher = AES.new(key, AES.MODE_EAX)
msg=input("Enter the message:").encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(msg)
print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)