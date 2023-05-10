import json

f = open("datisalvati.txt", "r", encoding = "utf-8")
datijson = f.read()
f.close()
print(datijson, type(datijson))

dati = json.loads(datijson)
print(dati, type(dati))