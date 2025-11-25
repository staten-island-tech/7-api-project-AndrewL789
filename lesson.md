Skip to main content
Google Classroom
Classroom
Comp Sci/Engineering T1
SKS21T_20 (Period 2) 2025 1
Home
Calendar
Enrolled
To-do
S
SITHS Library Google Classroom
N
NHS Cohort Class of 2029
Current Freshmen
S
SITHS Career Development Center 2025-26
C
Class of 2029 - College Advisement
GAS11QC_9 (Period 13) 2025 1
p
p9 MONDAY Chem Lab
C
Comp Sci/Engineering T1
SKS21T_20 (Period 2) 2025 1
P
Pd 7 Chemistry
SCS21H_74 (Period 7) 2025 1
I
Intro Tech Careers T1
RZS21TF_62 (Period 6) 2025 1
P
PE T1
PPS71_45 (Period 4) 2025 1
A
AP World History T1
HGS41X_88 (Period 8) 2025 1
P
Pd 3 English T1 - Fall Honors 2025
EES81H_39 (Period 3) 2025 1
G
Geometry T1-PD 1
MGS21H_10 (Period 1) 2025 1
P
Period 5 - Freshmen
(FRS61H-54)
Archived classes
Settings
Assignment details
API Project
Michael Whalen
•
Nov 5 (Edited Nov 19)
Learning Progress
•
15 points
Repo: https://classroom.github.com/a/QKx7Ys58

Directions: Select an API and build a project around that. The project must show the user some data from the API in a manner that is easy to read. You have a large degree of freedom of what the project is. User should be able to request and view different types of data through the terminal. Example, show users some stock data. Then allow users to search for new stock data, sort stock data etc. 
We will also be leveraging Tkinter for this project
For leveraging Tkinter I will be allowing the use of an AI assistant but you must save your prompts. All prompts must ONLY be related to tkinter and not the logic of the application. You can copy and paste your prompts and the AI response into a google doc to be shared with me at the end of the project. See my example below.
lesson.md
Text

Tkinter AI Chat Log.pdf
PDF

virtualenv.md
Text

Class comments
Your work
Assigned
Private comments

# 🧠 Lesson: Catching Pokémon with Python 

### SWBAT (Students Will Be Able To):

* Explain what the `requests` library does and why we use it
* Use list comprehensions to make new lists quickly
* Use `.items()` to loop through key-value pairs in a dictionary

---

## 🕹️ Step 1: What’s happening in our code?

```python
import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon)
```

---

## 🧩 Step 2: Understanding `requests`

Imagine your Python program as a **trainer** 👩‍💻 sending a message to a **Pokémon Center** 🏥 (the internet).

When you do:

```python
requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
```

you’re saying:

> “Hey Pokémon Center! Please send me all the information you have on Bulbasaur!”

The center sends back a **big package** 📦 of data.
That package is called a **response**.

We open the box using:

```python
data = response.json()
```

Now we can see everything inside — names, types, height, weight, etc.
It’s like opening a Pokédex entry!

---

## 🧠 Step 3: What is a Dictionary?

A **dictionary** in Python is like a **backpack with labeled pockets** 🎒.

Example:

```python
pokemon = {
    "name": "Bulbasaur",
    "type": "grass",
    "weight": 69
}
```

Each pocket has:

* A **key** (the label) → `"name"`, `"type"`, `"weight"`
* A **value** (what’s inside) → `"Bulbasaur"`, `"grass"`, `69`

So when you ask:

```python
print(pokemon["type"])
```

Python looks for the pocket labeled `"type"` and gives you `"grass"` 🌿.

---

## 🔍 Step 4: Looping with `.items()`

What if you want to look inside **every pocket** in your backpack?

You can use:

```python
for key, value in pokemon.items():
    print(key, "→", value)
```

Output:

```
name → Bulbasaur
type → grass
weight → 69
```

Analogy:

> `.items()` lets you say, “Show me *each pocket label* and *what’s inside it*.”

---

## ⚡ Step 5: What’s that weird `[t["type"]["name"] for t in data["types"]]` thing?

That’s called a **list comprehension** — a short way to make a new list.

The long way would be:

```python
types = []
for t in data["types"]:
    types.append(t["type"]["name"])
```

The short version:

```python
types = [t["type"]["name"] for t in data["types"]]
```

Analogy:

> Think of it like making a tray of cookies 🍪.
> You take each dough ball (`t`) and shape it into a cookie (`t["type"]["name"]`).
> When you’re done, you have a whole new tray (a new list).

---

## 🧠 Step 6: Putting it all together

After your function runs, you get something like:

```python
{
  'name': 'bulbasaur',
  'height': 7,
  'weight': 69,
  'types': ['grass', 'poison']
}
```

Now you can use `.items()` to print it nicely:

```python
pokemon = getPoke("Bulbasaur")

for key, value in pokemon.items():
    print(f"{key.title()}: {value}")
```

Output:

```
Name: bulbasaur
Height: 7
Weight: 69
Types: ['grass', 'poison']
```

---

## 🧠 Recap

| Concept            | What it does                   | Analogy                                |
| ------------------ | ------------------------------ | -------------------------------------- |
| `requests.get()`   | Gets info from a website       | Sending a letter to the Pokémon Center |
| `.json()`          | Opens the package              | Opening your data box                  |
| Dictionary         | Stores info as key:value       | Backpack with labeled pockets          |
| `.items()`         | Loops through both key + value | Checking every pocket                  |
| List comprehension | Builds new lists quickly       | Cookie cutter for data                 |

---
lesson.md
Displaying lesson.md.