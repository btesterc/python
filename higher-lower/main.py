import art
import random
import game_data
import os

print(art.logo)
number = len(game_data.data)
first_select_number = random.randint(0,number)
second_select_number = random.randint(0,number)

A = game_data.data[first_select_number]
B = game_data.data[second_select_number]


score = 0

Game_over = False

while not Game_over:

  os.system('clear')
  print( f"Compare A: {A['name']},  {A['description']},  {A['country']}.") 
  if score > 0:
    print(f"You're right! Current score: {score}.")
  print(art.vs)
  print(f"Compare B: {B['name']},  {B['description']},  {B['country']}.")
  answer = input ("Who has more followers? Type 'A' or 'B':").lower()
  
  if answer == "a":
    if A['follower_count'] < B['follower_count']:      
      Game_over = True
    elif A['follower_count'] > B['follower_count']:
      score += 1
      A = B
      B = game_data.data[random.randint(0,number)]
            
  elif answer == "b":
    if B['follower_count'] < A['follower_count']:
      Game_over = True
    elif B['follower_count'] > A['follower_count'] :
      score += 1
      A = B
      B = game_data.data[random.randint(0,number)]




print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")      

