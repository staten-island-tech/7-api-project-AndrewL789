import requests

def getWord(word):
     response = requests.get(f"https://lingua-robot.p.rapidapi.com/language/v1/entries/en/{word.lower()}")
     if response.status_code != 200:
          print("Error fetching data")
          return None
     data = response.json()
     for key, value in data.items():
          print(key,  "→", value )
     return 


     
pokemon = getWord("Xiyang")
print(pokemon)

    