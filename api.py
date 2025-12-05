import requests
import random
import tkinter as tk
#anime wordle 
#https://api.jikan.moe/v4/ <- the url base 
def anicheck(x):
     thething = requests.get("https://api.jikan.moe/v4/anime?q={x}")
     gah = thething.json()
     compare = gah['data']
     return compare
def randoman():
     popular = requests.get("https://api.jikan.moe/v4/top/anime")
     if popular.status_code != 200:
          print("Error fetching data")
          return None
     data = popular.json()
     anime = random.choice(data['data'])
     return anime
def analyze(anime):
     name = [anime['title'], anime['title_english']] + anime['title_synonyms']
     names = [n.lower() for n in name if n is not None]
     qualities = {'type': anime['type'], 'genre' :[g['name'] for g in anime['genres']], 'source': anime['source'], 'episodes' : anime['episodes'], 'rating' : anime['rating'], 'score' : anime['score'], 'popularity' : anime['popularity']}
     return names, qualities
def game():
     x = randoman()
     names, qualities = analyze(x)
     print(qualities)
     print(names) # take this out at end
     correct = False
     inputamt = 0
     while correct == False and inputamt < 5:
          guess = input('guess? :').strip().lower()
          inputamt += 1
          if guess in names:
               correct = True
               print(f'correct! got it in {inputamt}')
          if inputamt == 5 and correct == False:
               print(f'You lose, it was {names}')
#game()
window = tk.Tk()
window.title = ('Wordle')
window.geometry("960x540")
prompt = tk.Label(window, text="Guess the anime:",
font=("Arial", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
window.mainloop()