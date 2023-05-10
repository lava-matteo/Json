import json

f = open("datisalvati.txt", "r", encoding = "utf-8")
datijson = f.read()
f.close()
print(datijson)