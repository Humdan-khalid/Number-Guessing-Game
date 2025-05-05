import random

print("=====Guessing Game=====\n")
print("total chance: 5")

def guess_number():
  attempts : int = 5
  score : int = 0
  
  while attempts > 0:
    print(f"\nremaining {attempts} attempts.")
    computer_num = random.randint(1 , 5)
  
    try:
      user_input = int(input("\nguess the computer number (1 to 5): "))
    except ValueError:
      print("please enter a valid integer.\n")
      print("Game Restart")
      continue
    
    if user_input == computer_num:
      print("nice Hamdan, you are guess the right number.")
      score += 5
    else:
      print(f"wrong guess.computer number was: {computer_num}")
      
    attempts -= 1

  
  if score >= 10:
    print(f"\nyou are win the match because your score is: {score}")
  else:
    print(f"\nyou are lose because your score is: {score}")
  
guess_number()