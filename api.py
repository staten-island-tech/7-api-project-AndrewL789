import requests
import random
#anime wordle 
#https://api.jikan.moe/v4/ <- the url base 
def randoman():
     popular = requests.get("https://api.jikan.moe/v4/top/anime")
     if popular.status_code != 200:
          print("Error fetching data")
          return None
     data = popular.json()
     anime = random.choice(data['data'])
     name = [anime['title'], anime['title_english']] + anime['title_synonyms']
     names = [n.lower() for n in name if n is not None]
     hints = {'type': anime['type'], 'genre' :[g['name'] for g in anime['genres']], 'source': anime['source'], 'episodes' : anime['episodes'], 'rating' : anime['rating'], 'score' : anime['score'], 'popularity' : anime['popularity']}
     return names, hints
def game():
     names, hints = randoman()
     print(hints)
     print(names) # take this out at end
     correct = False
     inputamt = 0
     while correct == False and inputamt < 5:
          guess = input('guess? :').strip().lower()
          inputamt += 1
          if guess in names:
               correct = True
               print(f'correct! got it in {inputamt}')
game()