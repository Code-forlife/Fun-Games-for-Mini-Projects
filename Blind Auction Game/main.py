import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print('Welcome to the secret auction program')
players={}
max=0
winner=""
while True:
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))
  players[name]=bid
  if bid>max:
    max=bid
    winner=name
  check=input("Are there any other bidders? Type 'yes' or 'no'.")
  if check=="yes":
    os.system('clear')
  elif check=="no":
    os.system('clear')
    break
  else:
    print("Invalid Option")

print(f'The winner is {winner} with a bid of ${max}')
