import random

options = {
  1: "Rock",
  2: "paper",
  3: "Scissors",
  4: "Lizard",
  5: "Spock"
  }

print('.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨¨*:·.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨')
print('༶•┈┈୨♡୧┈┈•༶Rock Paper Scissors Lizard Spock༶•┈┈୨♡୧┈┈•༶')
print('.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨¨*:·.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨')
print('Rules:\nRock crushes scissors and lizard\nPaper covers rock and disproves Spock\nScissors cuts paper and decapitates lizard\nLizard poisons Spock and eats paper\nSpock vaporizes rock and smashes scissors')
print('.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨¨*:·.·:*¨¨* ≈☆≈ *¨¨*:·≈☆≈ *¨')
while True:
    player_choice = int(input('pick one:\n1)Rock\n2)Paper\n3)Scissors\n4)Lizard\n5)Spock\n'))
    if player_choice not in [1,2,3,4,5] :
      print('invalid responce')
      continue
    print('now its time for the computer to pick...')
    computer_choice = random.randint(1, 5)
    print(f'the computer plays {options[computer_choice]}')
    
    if player_choice == computer_choice:
      print('tie, try again')
    elif (player_choice == 1 and computer_choice in [3, 4]) or (player_choice == 2 and computer_choice in [1, 5]) or (player_choice == 3 and computer_choice in [2, 4]) or (player_choice == 4 and computer_choice in [2, 5]) or (player_choice == 5 and computer_choice in [1, 3]):
      print('Player wins!')
    elif (computer_choice == 1 and player_choice in [3, 4]) or (computer_choice == 2 and player_choice in [1, 5]) or (computer_choice == 3 and player_choice in [2, 4]) or (computer_choice == 4 and player_choice in [2, 5]) or (computer_choice == 5 and player_choice in [1, 3]):
      print('Computer wins!')