import json
import urllib.request

#The API key of Crypto Compare
API_KEY = 'b03db73eaa6a6957380ddf0707beb220a216eb767e059f214de61fcb2ad6b93e'

#Here I use a method to get the DATA from the API
def getData(URL):
    with urllib.request.urlopen(URL) as r:
        temp = r.read()
        temp = temp.decode()
        data = json.loads(temp)
        return data

#Here I open the file with read permissions and turn it into a JSON file so i can treat it like a dictionary
with open('Crypto.txt', 'r') as file:
    crypto_dic = json.load(file)

#Here i iterate the dictionary with the KEY (BTC,ETH etc)
#I transform the URL according to my KEY and then I use my func to get the DATA that I need
for key in crypto_dic:
    URL = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=EUR&api_key={}'.format(key, API_KEY)
    data = getData(URL)
    EURO = data[key]["EUR"]
    #I print the results to the user's console :)
    print("Your currenct ammount of: ", key, "is: ",EURO*crypto_dic[key],"EUR(€)")
