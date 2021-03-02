import urllib.request
import json
def fetch_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    b=json.loads(html)
    return b[coin]["EUR"]
with open('mycoins.txt') as f: 
    data = f.read() 
    d = json.loads(data)
for key in d:
	k=key
	amount= d[k]
	bit= fetch_coin_data(k)
	euros = amount*bit
	print ("My", k, "s :", euros, "€") 
f.close()
 
