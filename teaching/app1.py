import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "the word doesnt exist .Please double check ie"
         
word = input("Enter word: ")


print(translate(word))
