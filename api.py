import requests
# replace all of the words in a text wit random synonyms
def word(word):
        bore = requests.get(f'https://wordsapiv1.p.mashape.com/words/{word.lower()}')
        data = bore.json()
        
    
print(word('fart'))