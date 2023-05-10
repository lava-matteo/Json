import requests
import json


for i in range(10):
    x = requests.get('https://api.breakingbadquotes.xyz/v1/quotes')
    if x.status_code !=200:
        pass
    else:
        quote = json.loads(x.text)
        print(quote[0]['quote'], "-", quote[0]['author'])