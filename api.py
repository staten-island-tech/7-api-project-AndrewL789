import requests
import random
import tkinter as tk
from tkinter import ttk 
import threading
#anime wordle 
#https://api.jikan.moe/v4/ <- the url base
def anicheck(x):
     thething = requests.get(f"https://api.jikan.moe/v4/anime?q={x}")
     gah = thething.json()
     senor = gah['data'][0]
     compare = [t['title_english'] if t['title_english'] is not None else t['title'] for t in gah['data']]
     return compare, senor
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
def gamescreen():
     x = randoman()
     names, qualities = analyze(x)
     window = tk.Tk()
     window.title = ('Wordle')
     window.geometry("960x540")
     def update(event=None):
          text = drop.get()
          compare, _ = anicheck(text)
          drop['values'] = compare
     def on_enter(event=None):
          if drop.get() in drop['values']:
               value = drop.get()
               _, senor = anicheck(value)
               _ , qualities = analyze(senor)
               text = f"Guess: {value}\n" \
               f"Type: {qualities['type']}\n" \
               f"Genres: {', '.join(qualities['genre'])}\n" \
               f"Source: {qualities['source']}\n" \
               f"Episodes: {qualities['episodes']}\n" \
               f"Rating: {qualities['rating']}\n" \
               f"Score: {qualities['score']}\n" \
               f"Popularity: {qualities['popularity']}"
               new_label = tk.Label(window, text=text, font=("Arial", 10))
               new_label.pack(pady=9)
               label.append(new_label)
               drop.delete(0, tk.END)
     drop = ttk.Combobox(window)
     drop['values'] = []
     drop.set("")
     drop.pack()
     drop.bind("<KeyRelease>", update)
     drop.bind("<Return>", on_enter)
     label = [] 

     window.mainloop()
gamescreen()