import random

prefs = {}

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["Fluffy", "Solid", "Winged", "Purple", "Lofty", "Zippy"]
nouns = ["Elephant", "Smoothie", "Sin", "Poodle", "Kitten"]

def get_preferences():
  for q in questions:
    a = raw_input(questions[q])
    if a == "yes" or a == "y" or a == "Yes":
      a = True
    else:
      a = False
    prefs[q]=a
#  print prefs  

def make_drink():
  print "Enjoy your {} {} drink".format(random.choice(adjectives).upper(), random.choice(nouns).upper())
  drink =[]
  for pref in prefs:
    if prefs[pref] == True:
      print random.choice(ingredients[pref])
  
if __name__ == '__main__':
  agree = True
  get_preferences()
  make_drink()
  while agree:
    agree = raw_input("Would you like another drink?")
    if agree == "yes" or agree == "y" or agree == "Yes":
      agree = True
    else:
      agree = False
    if agree:
      get_preferences()
      make_drink()
    else:
      print "Thanks, mate, for drinkin' at the Hearty Ale"
  