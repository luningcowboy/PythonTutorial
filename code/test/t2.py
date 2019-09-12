d1 = {"k1":0,"k2":1}
print(d1.get("k3"))
if not d1.get("k3",None):
    print("error")
