import requests
import random
import tkinter as tk
from tkinter import ttk 
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
def gamescreen():

     x = randoman()
     names, qualitie = analyze(x)
     window = tk.Tk()
     window.title = ('Wordle')
     window.geometry("960x540")
     window.configure(bg="#2C2F33")
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
               te(text)
               drop.delete(0, tk.END)
     def te(x):
          new_text= tk.Text(window, height = 10, width = 180,bg = "#23272A", font=("Arial", 10))
          new_text.insert("end", x)
          new_text.config(state="disabled")
          new_text.pack(pady=9)
          gah.append(new_text)
     drop = ttk.Combobox(window)
     drop['values'] = []
     drop.set("")
     drop.pack(pady = 10)
     drop.bind("<KeyRelease>", update)
     drop.bind("<Return>", on_enter)
     gah = [] 

     window.mainloop()
class game:
     def __init__(self):
          self.window = tk.Tk()
          self.window.title("The game")
          self.window.geometry("960x540")
          self.window.configure(bg="#2C2F33")
          self.x = randoman()
          self.names, self.qualitie = analyze(self.x)
          self.guess_count = 0
          self.gah=[]
          self.drop = ttk.Combobox(self.window)
          self.drop['values'] = []
          self.drop.set("")
          self.drop.pack(pady=10)
          self.label = tk.Label(self.window, text = self.names,bg="#2C2F33",fg="#FFFFFF")
          self.label.pack(side = 'left')
          self.drop.bind("<KeyRelease>", self.update)
          self.drop.bind("<Return>", self.on_enter)
          self.win = False
          self.lose = False
     def update(self, event=None):
          text = self.drop.get()
          compare, _ = anicheck(text)
          self.drop['values'] = compare
     def te(self, x):
          new_text= tk.Text(self.window, height=10, width=180, bg="#23272A", fg="#FFFFFF", font=("Arial", 10))
          new_text.insert("end", x)
          new_text.config(state="disabled")
          new_text.pack(pady=9)
          self.gah.append(new_text)
     def on_enter(self, event=None):
          if self.drop.get() in self.drop['values'] and self.guess_count < 5 and self.win == False and self.lose == False:
               value = self.drop.get()
               _, senor = anicheck(value)
               _ , qualities = analyze(senor)
               output = self.xi(qualities)
               self.guess_count += 1
               text = (
                    f"Guess: {value}\n"
                    f"Type: {output['type']}\n"
                    f"Genres: {', '.join(output['genre'])}\n"
                    f"Source: {output['source']}\n"
                    f"Episodes: {output['episodes']}\n"
                    f"Rating: {output['rating']}\n"
                    f"Score: {output['score']}\n"
                    f"Popularity: {output['popularity']}\n"
                    f"guess number: {self.guess_count}"
               )
               self.te(text)
               self.drop.delete(0, tk.END)
          for t in self.names:
               if value == t:
                         self.win = True
          if self.guess_count == 5 and self.win == False:
               self.lose = True
          if self.win == True:
               self.te('You win!')
          if self.lose == True:
               self.te(f'You lose, it was ')
          
               
     def run(self):
          self.window.mainloop()
     def xi(self, x):
          output = {}
          output['type'] = x['type'] + ('✅' if self.qualitie['type'] == x['type'] else '❌')
          output['source'] = x['source'] +('✅' if self.qualitie['source'] == x['source'] else '❌')
          output['episodes'] = str(x['episodes']) +('✅' if self.qualitie['episodes'] == x['episodes'] else '❌')
          gen = [t + ('✅' if t in self.qualitie['genre'] else '❌') for t in x['genre']]
          output['genre'] = gen 
          output['popularity'] = str(x['popularity']) +('✅' if self.qualitie['popularity'] == x['popularity'] else '❌')
          output['score'] = str(x['score']) +('✅' if self.qualitie['score'] == x['score'] else '❌')
          output['rating'] = str(x['rating']) +('✅' if self.qualitie['rating'] == x['rating'] else '❌')
          return output

xiyang = game()
xiyang.run()