import requests
import random
import tkinter as tk
from tkinter import ttk 
#anime wordle 
#https://api.jikan.moe/v4/ <- the url base
def anicheck(x):
     try:
          thething = requests.get(f"https://api.jikan.moe/v4/anime?q={x}")
          gah = thething.json()
          senor = gah['data'][0]
          compare = [t['title_english'] if t['title_english'] is not None else t['title'] for t in gah['data']]
     except:
          senor = [] 
          compare = []
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
     id = anime['mal_id']
     return names, qualities, id
def lazy(x,y):
     if x == y:
          q = '✅'
     else:
          q = '❌'
     return q
def lazy2(x,y): 
     try:
          if int(x) > int(y):
               g = "⬇️"
          if int(x) < int(y):
               g = '⬆️'
          if int(x) == int(y):
               g = '✅'
     except:
          g = '❌'
     return g
class game:
     def __init__(self):
          self.window = tk.Tk()
          self.window.title("The game")
          self.window.geometry("960x540")
          self.window.configure(bg="#2C2F33")
          self.x = randoman()
          self.names, self.qualitie, self.id = analyze(self.x)
          self.guess_count = 0
          self.label =tk.Label(self.window, text="Type anime name in textbox and click enter then go to dropdown.", font=("Arial", 14, "bold"),bg="#23272A", fg="#FFFFFF",)
          self.label.pack(pady=15)
          self.drop = ttk.Combobox(self.window, width = 90)
          self.drop['values'] = []
          self.drop.set("")
          self.entry = tk.Entry(self.window,bg="#23272A", fg="#FFFFFF", font=("Arial", 14), width=30)
          self.entry.pack(pady =10, padx = 5)
          self.drop.pack(pady=10, padx = 5)
          self.entry.bind("<Return>", self.update)
          self.drop.bind("<Return>", self.on_enter)
          self.win = False
          self.lose = False
     def update(self, event):
          text = self.entry.get()
          compare, ball = anicheck(text)
          self.drop['values'] = compare
     def te(self, x):
          lotion= tk.Text(self.window, height=10, width=180, bg="#23272A", fg="#FFFFFF", font=("Arial", 10))
          lotion.insert("end", x)
          lotion.config(state="disabled")
          lotion.pack(pady=9)
     def on_enter(self, event):
          if self.drop.get() in self.drop['values'] and self.guess_count < 5 and self.win == False and self.lose == False:
               value = self.drop.get()
               yao, senor = anicheck(value)
               xi , qualities, id = analyze(senor)
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
               if id == self.id:
                    self.win = True
          if self.guess_count == 5 and self.win == False:
               self.lose = True
          if self.win == True:
               self.te(f'You win! in {self.guess_count} attempts!')
               self.drop.destroy()
               self.entry.destroy()
          if self.lose == True:
               self.te(f'You lose, it was {self.x['title_english'] or self.x['title']}')
               self.drop.destroy()     
               self.entry.destroy()  
     def run(self):
          self.window.mainloop()
     def xi(self, x):
          output = {}
          output['type'] = x['type'] + lazy(self.qualitie['type'],x['type'])
          output['source'] = x['source'] + lazy(self.qualitie['source'], x['source'])
          output['episodes'] = str(x['episodes']) + lazy2(x['episodes'],self.qualitie['episodes'])
          output['genre'] = [t + lazy(t,self.qualitie['genre']) for t in x['genre']]
          output['popularity'] = str(x['popularity']) +lazy2(x['popularity'], self.qualitie['popularity'])
          output['score'] = str(x['score']) + lazy2(x['score'], self.qualitie['score'])
          output['rating'] = str(x['rating']) + lazy(x['rating'], self.qualitie['rating'])
          return output

xiyang = game()
xiyang.run()