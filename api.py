import requests
import random
# replace all of the words in a text wit random synonyms
def word(word):
        bore = requests.get(f'https://api.jikan.moe/v4/')
        if bore.status_code != 200:
          print("Error fetching data")
          return None
        data = bore.json 
        return type(data)   
print(word('boat'))