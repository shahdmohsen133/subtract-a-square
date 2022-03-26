#Header: This is a two-player mathematical game of strategy with a pile of coins which 'called Subtract a square'
# each player take turns to remove a non-zero square number of coins The player who removes the last coin wins.
# outher:Shahd Mohsen Mohamed Mohamed 
# date:28/2/2022


from math import* 
import random 


choice= input("would you rather to' choose' number of coins or randomly , please write 'choose' or 'randomly\n \n ") .strip() .lower()
if choice=='randomly':  
      number_of_coins =random.randint(2,700) 
elif choice == "choose":
 number_of_coins=int(input("please, enter number of coins:\n")) # ask user to enter number of coins
 while number_of_coins<=0:# check that number is positive
    print(" sorry wrong input, please enter a none-zero positive number:\n")
    number_of_coins=int(input("please, enter number of coins:"))
else:
    print("sorry, wrong choice") 


while True:
  print(f"the total coins ={number_of_coins}\n")  #print the total coins on screen 
  player_one=int(input("player 1:"))
  while player_one<= 0:            # check that the number is positive 
    print("sorry , you have to pull a non-zero positive number\n")
    player_one=int(input("player 1:")) 
  while int(sqrt(player_one ))!=sqrt(player_one) :   # check number has square root
    print("sorry, you have to pull a square root number \n ") 
    player_one=int(input("please, enter a complet square number:")) 
  while player_one > number_of_coins :  #  check that the number less than number of coins
      print(f"sorry , pull number less than {number_of_coins}\n")
      player_one=int(input("player 1 :"))
  number_of_coins = int(number_of_coins-player_one) # calculate the new sum by subtracting the total from the player input 
  print(f"ther remaining coins = {number_of_coins}")
  if number_of_coins==0:  # check if the player won 
    print( "player 1 is the winner") 
    break 
  
  else:
    player_two=int(input(" player 2:"))
    while(player_two<0) or(player_two==0):
      print(" sorry , you have to pull a non-zero positive number\n")
      player_two=int(input(" player 2:"))
    while int(sqrt(player_two ))!=sqrt(player_two) :
      print("sorry, you have to pull a square root number") 
      player_two=int(input("player2:")) 
    while player_two > number_of_coins :
      print(f"sorry , enter number less than {number_of_coins}")
      player_two=int(input("player 2: "))
    number_of_coins=number_of_coins-player_two 
    if (number_of_coins ==0 ) :
      print("player 2 is the winner")  
      break 

