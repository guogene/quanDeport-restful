import hashlib
a = "sdfds".encode("utf-8")
b = hashlib.md5(a).hexdigest()
print(b)
