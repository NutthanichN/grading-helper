import random
def convert_to_int(st):
    if(st == "rock"):
        return 0
    elif(st == "paper"):
        return 2
    elif(st == "scissor"):
        return 4
    elif(st == "spock"):
        return 1
    elif(st=="lizard"):
        return 3
'''
  play game 2 player with more options
  >>> game2()
  Player chooses rock
  Computer chooses scissor
  Player wins
'''
def game2():
  end = True
  choiceList = ["rock","paper","scissor","spock","lizard"]
  while(end == True):
      p = random.choice(choiceList)
      print(f"Player chooses {p}")
      com = random.choice(choiceList)
      print(f"Computer chooses {com}")
      p1 = convert_to_int(p)
      com1 = convert_to_int(com)
      if (p1  == com1):
          print("Both ties")
      elif (((p1+1)%5)== com1 or((p1+2)%5)== com1):
          print("computer wins")
          end = False
      else:
          print("Player wins")
          end = False

    

