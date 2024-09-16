import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start == "y":
  play_game = True  
elif start == "n":
  print ("see you later")  
else :
  print("please type correctly")

while play_game:
  # bilgisayar kart secimi $
  com_cards = []
  for i in range(0,2):     
    a = random.choice(cards)
    com_cards.append(a)
  total_value = com_cards[0] + com_cards[1]
  if total_value < 17:
    b = random.choice(cards)
    com_cards.append(b)
    total_value += com_cards[2]
    if total_value < 17:
      c = random.choice(cards)
      com_cards.append(c)
      total_value += com_cards[3]  
      if total_value > 21:
        if com_cards.count(11) == True:
           total_value -= 10    
    elif total_value > 21:
      if com_cards.count(11) == True:
        total_value -= 10
        
  print(art.logo)
    
  user_cards = []
    
  for i in range(0,2):
    d = random.choice(cards)
    user_cards.append(d)
  total_value2 = user_cards[0] + user_cards[1]
  print(f"    Your cards {user_cards}, total score is {total_value2} ")
  print(f"    Computer first card is {com_cards[0]} ")
  card_or_pass1 = input("Type 'y' to get another card, type 'n' to pass:")
      
  if card_or_pass1 == "y":
    e = random.choice(cards)
    user_cards.append(e)
    total_value2 +=  user_cards[2]
    if total_value2 > 21:
       if user_cards.count(11) == True:
         total_value2 -= 10
    print(f"    Your cards {user_cards}, total score is {total_value2} ")
    print(f"    Computer first card is {com_cards[0]} ")  

    card_or_pass2 = input("Type 'y' to get another card, type 'n' to pass:")
    
    if card_or_pass2 == "y":
      f = random.choice(cards)
      user_cards.append(f)
      total_value2 +=  user_cards[3]
      if total_value2 > 21:
        if user_cards.count(11) == True:
          total_value2 -= 10
      print(f"    Your cards {user_cards}, total score is {total_value2} ")
      print(f"    Computer first card is {com_cards[0]} ")   
        
    elif card_or_pass2 == "n":
      print(f"    Your final hand: {user_cards} , final score: {total_value2} ")
      print(f"    Computer's final hand: {com_cards} , final score: {total_value} ")
    if total_value2 > 21 and total_value >21 :
      print ("Both went over. DRAFT.")
    if total_value2 > 21:
      if total_value <= 21:
        print("You went over. You Lost.")
    elif total_value2 <= 21:
      if total_value > 21:
        print("Computer went over. You Win.")
      elif total_value <= 21:
        if total_value2 == total_value:
          print("Equal numbers. DRAFT")
        elif total_value2 > total_value:
          print("You Win")
        else:
          print("You lost")
    play_game3 = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")  
    if play_game3 == "y":
      play_game = True
    elif play_game3 == "n":
      print ("see you later")
      play_game = False
    
  elif card_or_pass1 == "n":
    print(f"    Your final hand: {user_cards} , final score: {total_value2} ")
    print(f"    Computer's final hand: {com_cards} , final score: {total_value} ")
    if total_value2 > 21 and total_value >21 :
      print ("Both went over. DRAFT.")
    if total_value2 > 21:
      if total_value <= 21:
        print("You went over. You Lost.")
    elif total_value2 <= 21:
      if total_value > 21:
        print("Computer went over. You Win.")
      elif total_value <= 21:
        if total_value2 == total_value:
          print("Equal numbers. DRAFT")
        elif total_value2 > total_value:
          print("You Win")
        else:
          print("You lost")
    play_game2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if play_game2 == "y":
      play_game = True  
    elif play_game2 == "n":
      print ("see you later")
      play_game = False
    
      
 







