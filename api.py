import requests
import random
# replace all of the words in a text wit random synonyms
def word(word):
        bore = requests.get(f'https://wordsapiv1.p.rapidapi.com/words/{word.lower()}/synonyms')
        if bore.status_code != 200:
          print("Error fetching data")
          return None
        data = bore.json
        word = random.data
        
    
print(word('boat'))