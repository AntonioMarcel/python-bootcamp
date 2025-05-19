import random

answer = random.randint(1,100)
player_guess = None
turn_number = 1
print(answer)

while player_guess != answer:
  previous_guess = player_guess
  player_guess = int(input("Guess the number: "))

  if player_guess == answer:
    print(f"Congratulations! You've answered correctly and it took {turn_number} turns! ")
    break
  
  if player_guess < 1 or player_guess > 100:
      print("out of bounds")
      turn_number += 1
      continue
  
  if turn_number == 1:
    if abs(player_guess - answer) <= 10:
      print("WARM!")
    elif abs(player_guess - answer) > 10:
      print("COLD!")
  else: 
    if abs(player_guess - answer) < abs(previous_guess - answer):
      print("WARMER!") 
    elif abs(player_guess - answer) >= abs(previous_guess - answer):
      print("COLDER!")

  turn_number += 1


