import hashlib
msg=input("Enter the message::")
result = hashlib.sha1(msg.encode()).hexdigest()
print("SHA hash for", msg, ":", result)