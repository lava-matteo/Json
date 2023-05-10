import json

dati = {"meteo": "pioggia",
        "temperatura": 19,
        "citta": "Dalmine"
        }

datijson = json.dumps(dati)

print(dati)
print(datijson)

f = open("datisalvati.txt", "w", encoding = "utf-8")
f.write(datijson)
f.close()