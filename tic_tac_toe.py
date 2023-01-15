#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import os
import platform

opsys = platform.platform()

if ("Linux" in opsys) or ("linux" in opsys) or ("Mac" in opsys) or ("mac" in opsys):
  cls = "clear"
elif ("Windows" in opsys) or ("windows" in opsys):
  cls = "cls"

os.system(cls)

print("∆_____________∆")
print("|Tic  Tac  Toe|")
print(" \-----------/ ")
print("  \By  Fedor/  ")
print("   \_______/   ")

print()
first = str(input("Who should start? (player/bot) "))
input("Press enter to start!")
os.system(cls)

möglich = [1,2,3,4,5,6,7,8,9]
spielbrett = [[1,2,3], [4,5,6], [7,8,9]]
breite = 3
höhe = 3

def spielbrett_anzeigen():
  for x in range(breite):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(höhe):
      print("", spielbrett[x][y], end=" |")
  print("\n+---+---+---+")

# spielbrett_anzeigen()

def spielzug(num, turn):
  num -= 1
  if(num == 0):
    spielbrett[0][0] = turn
  elif(num == 1):
    spielbrett[0][1] = turn
  elif(num == 2):
    spielbrett[0][2] = turn
  elif(num == 3):
    spielbrett[1][0] = turn
  elif(num == 4):
    spielbrett[1][1] = turn
  elif(num == 5):
    spielbrett[1][2] = turn
  elif(num == 6):
    spielbrett[2][0] = turn
  elif(num == 7):
    spielbrett[2][1] = turn
  elif(num == 8):
    spielbrett[2][2] = turn

def gewinnen(spielbrett):
  pwin = "The player wins!"
  bwin = "The bot wins!"

  #waagerechte fälle
  if(spielbrett[0][0] == "X" and spielbrett[0][1] == "X" and spielbrett[0][2] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][0] == "O" and spielbrett[0][1] == "O" and spielbrett[0][2] == "O"):
    print(bwin)
    return "O"
  elif(spielbrett[1][0] == "X" and spielbrett[1][1] == "X" and spielbrett[1][2] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[1][0] == "O" and spielbrett[1][1] == "O" and spielbrett[1][2] == "O"):
    print(bwin)
    return "O"
  elif(spielbrett[2][0] == "X" and spielbrett[2][1] == "X" and spielbrett[2][2] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[2][0] == "O" and spielbrett[2][1] == "O" and spielbrett[2][2] == "O"):
    print(bwin)
    return "O"

  #senkrechte fälle
  elif(spielbrett[0][0] == "X" and spielbrett[1][0] == "X" and spielbrett[2][0] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][0] == "O" and spielbrett[1][0] == "O" and spielbrett[2][0] == "O"):
    print(bwin)
    return "O"
  elif(spielbrett[0][1] == "X" and spielbrett[1][1] == "X" and spielbrett[2][1] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][1] == "O" and spielbrett[1][1] == "O" and spielbrett[2][1] == "O"):
    print(bwin)
    return "O"
  elif(spielbrett[0][2] == "X" and spielbrett[1][2] == "X" and spielbrett[2][2] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][2] == "O" and spielbrett[1][2] == "O" and spielbrett[2][2] == "O"):
    print(bwin)
    return "O"

  #über kreuz fälle
  elif(spielbrett[0][0] == "X" and spielbrett[1][1] == "X" and spielbrett[2][2] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][0] == "O" and spielbrett[1][1] == "O" and spielbrett[2][2] == "O"):
    print(bwin)
    return "O"
  elif(spielbrett[0][2] == "X" and spielbrett[1][1] == "X" and spielbrett[2][0] == "X"):
    print(pwin)
    return "X"
  elif(spielbrett[0][2] == "O" and spielbrett[1][1] == "O" and spielbrett[2][0] == "O"):
    print(bwin)
    return "O"
  else:
    return "N"

loop_verlassen = False
if first == "bot":
  counter = 0
elif first == "player":
  counter = 1 # null = bot; 1 = spieler
else:
  counter = random.randint(1, 2)

while(loop_verlassen == False):
  if(counter % 2 == 1):
    spielbrett_anzeigen()
    try:
      eingabe = int(input("\nChoose a number: "))
    except:
      eingabe = 0
    os.system(cls)
    if(eingabe >= 1 and eingabe <= 9): #or
      spielzug(eingabe, "X")
      möglich.remove(eingabe)
    else:
      print("Number is not in the range of 1-9!")
      print("You have to miss a round!") #temp
    counter += 1
  else:
    while(True):
      bot_wahl = random.choice(möglich)
      print("\nBot choose: ", bot_wahl)
      if(bot_wahl in möglich):
        spielzug(bot_wahl, "O")
        möglich.remove(bot_wahl)
        counter += 1
        break

  winner = gewinnen(spielbrett)
  if(winner != "N"):
    print("\nThe End! :)")
    break
