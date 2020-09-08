import random
'''
  play game 2 player
  >>> game()
  Player chooses spock
  Computer chooses scissor
  Player wins
'''
def game():
  end = True
  choiceList = ["rock","paper","scissor"]
  while(end == True):
      p = random.choice(choiceList)
      print(f"Player chooses {p}")
      com = random.choice(choiceList)
      print(f"Computer chooses {com}")
      if(com==p):
          print(f"Both ties")

      elif((com == "scissor" and p == "paper") or (com == "paper" and p == "rock") or (com == "rock" and p == "scissor")):
          print(f"Computer wins")
          end = False
      else:
          print(f"Player wins")
          end = False
