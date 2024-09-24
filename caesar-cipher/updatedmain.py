alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class start:
  def __init__(self) -> None:
    self.direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    self.text = input("Type your message:\n").lower()
    self.shift = int(input("Type the shift number:\n")) % 26






def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
      
    
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

person = start()

caesar(start_text= person.text, shift_amount=person.shift, cipher_direction=person.direction)
 
should_continue = True
while should_continue:
  wish = input("do you want to continue type 'yes', otherwise 'no'\n").lower()
  if wish == "no" :
    should_continue = False
    print("Good Bye")
  elif wish == "yes" :
    person = start()
    caesar(start_text= person.text, shift_amount=person.shift, cipher_direction=person.direction)
    should_continue = True
  else:
    print("please type 'yes' or 'no'")
  