import markovify
import random

try:
    with open("hey.txt", 'r', encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("Error:The file was not found")
    exit()

# Initialize text_mod after reading the file
def generate_birthday_wish_markov(text,sonakshi,keywords):
    #if not text:
       # return f"Happy birthday,{sonakshi}! Wishing You a wonderful day1"
    text_mod = markovify.Text(text)
    if keywords:
        
        gen=text_mod.make_sentence()
        # Add a random word to the generated sentence
        random_word = random.choice(["amazing", "fantastic", "joyful", "lovely", "sparkling"])
        if not gen:
            return f"Happy birthday, {sonakshi}!  Wishing you a {random_word} day{text}."
        else:
            return f"Happy birthday, {sonakshi}! {gen} {random_word} Wishing you a wonderful day."
data_file="hey.txt"
keywords=["happy","birthday","wish","wonderful","day","cute","hugs"]
print(generate_birthday_wish_markov(text, "sonakshi", keywords))

