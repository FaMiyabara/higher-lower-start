from art import logo,vs
from game_data import data
from random import choice
from replit import clear

def format_data(account):
  
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return (f"{account_name} a {account_descr}, from {account_country }")

def check_answer(guess,a_followers,b_followers):
  
  if a_followers>b_followers:
    return guess == 'a'
  else:
    return guess == 'b'
  
  
print(logo)
points = 0
should_continue = True
account_b = choice(data)

while should_continue:

  account_a = account_b
  account_b =  choice(data)
  if account_a == account_b:
    account_b = choice(data)
    
  print(f"\nCompare A: {format_data(account_a)}.")
  print(vs)
  print(f"\nVersus B: {format_data(account_b)}.")
  
  guess =input("\nWho has more followers? Type 'A' or 'B': ").lower()
  
  
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  clear() 
  print(logo)
  
  if is_correct:
    points+=1
    print (f"\nYor're right!!!. Your score is {points}")
  else:
    should_continue = False
    print(f"\nSorry, that's wrong. Final score was {points}")
    
 
   
  


      


