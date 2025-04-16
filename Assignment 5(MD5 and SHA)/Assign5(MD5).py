import hashlib
msg=input("Enter the message::")
result = hashlib.md5(msg.encode()).hexdigest()
print("MD5 hash for", msg, ":", result)