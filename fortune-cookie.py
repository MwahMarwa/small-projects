import random
options = {
  1:"Don't pursue happiness – create it.",
  2: "All things are difficult before they are easy.",
  3: "The early bird gets the worm, but the second mouse gets the cheese.",
  4: "Someone in your life needs a letter from you.",
  5: "Don't just think. Act!",
  6: "Your heart will skip a beat.",
  7: "The fortune you search for is in another cookie.",
  8: "Help! I'm being held prisoner in a Chinese bakery!"
}
random_note = random.randint(1, 8)
def function():
  print(f'{options[random_note]}')

function()