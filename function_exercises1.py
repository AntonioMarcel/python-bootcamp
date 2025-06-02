# Warmup
## 1
def lesser_of_two_evens(num1,num2):
  if num1%2 == 0 and num2%2 == 0:
    if num1 > num2:
      return num2
    elif num2 > num1:
      return num1
  else: 
    if num1 > num2:
      return num1
    elif num2 > num1:
      return num2

print("lesser_of_two_evens()")
print(lesser_of_two_evens(5,3))

## 2
def animal_crackers(text):
  split_text = text.split(" ")
  return split_text[0][0] == split_text[1][0]

print("")
print("animal_crackers()")
print(animal_crackers('Levelheaded Llama'))

# stopped
## 3
def makes_twenty(n1, n2):
  if n1 + n2 == 20 or n1 == 20 or n2 == 20:
    return True
  else:
    return False
  
print("")
print("makes_twenty()")
print(makes_twenty(8,12))

# Level 1
## 1
def old_macdonald(text):
  count = 0
  new_string = ""
  
  for count, letter in enumerate(text):
    if count == 0 or count == 3:
      new_string = new_string + letter.capitalize()
    else:
      new_string = new_string + letter
  
  return new_string

print("")
print("old_macdonald()")
print(old_macdonald("macgonagal"))

## 2
def master_yoda(text):
  word_list = text.split(" ")
  reversed_word_list = word_list[::-1]
  return " ".join(reversed_word_list)  

print("")
print("master_yoda()")
print(master_yoda('We are ready'))

## 3
def almost_there(num):
  if abs(100 - num) <= 10 or abs(200- num) <= 10:
    return True
  else:
    return False

print("")
print("almost_there()")
print(almost_there(210))

# Level 2
# 1
def has_33(num_list):
    index = 0
    for index in range(0, len(num_list)-1):
      if num_list[index] == 3 and num_list[index+1] == 3:
        return True  
    
    return False

print("")
print("has_33()")
print(has_33([1, 3, 3, 3]))

# 2
def paper_doll(text):
  new_string = ""
  for letter in text:
    new_string = new_string + letter*3

  return new_string

print("")
print("paper_doll()")
print(paper_doll("hello"))

# 3
def blackjack(num1, num2, num3):
  num_sum = num1 + num2 + num3
  adjusted_sum = 0

  if any(x < 1 or x > 11 for x in [num1, num2, num3]):
    return "Numbers must be between 1 and 11"

  if num_sum <= 21:
    return num_sum
  elif num_sum > 21 and 11 in [num1, num2, num3]:
    adjusted_sum = num_sum - 10
    if adjusted_sum <= 21:
      return adjusted_sum
    else: # adjusted_sum >= 21
      return "BUST!"
  else: # num_sum > 21:
    return "BUST!"
  
print("")
print("blackjack()")
print(blackjack(0,5,11))

# 4
def summer_69_old(num_list):
  index_6 = None
  index_9 = None

  if 6 in num_list:
    for index, num in enumerate(num_list):
      if num == 6:
        index_6 = index 
      if num == 9:
        index_9 = index 
    return sum(num_list[0:index_6]) + sum(num_list[index_9+1:]) # +1 because I can't include 9 in the sum
  else:
    return sum(num_list)

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print("")
print("summer_69()")
print(summer_69([4, 5, 6, 7, 8, 9, 10, 6, 5, 1, 2, 3, 9, 10]))


# CHALLENGING PROBLEMS
# 1
def spy_game(num_list):

  appended_list = []
  for num in num_list:
    if num == 0:
      appended_list.append(num)
    if num == 7:
      appended_list.append(num)

  # Convert list of ints to str
  appended_list = map(str, appended_list)

  if "007" in "".join(appended_list):
    return True
  else:
    return False  
  
print("")
print("spy_game()")
print(spy_game([1,7,2,0,4,5,0]))

# 2
def count_primes(num):
  n_divs = 0
  n_primes = 0
  
  for num1 in range(2,num+1):
    for num2 in range(1, num1+1):
      if num1%num2 == 0:
        n_divs += 1
    if n_divs == 2:
      n_primes += 1
    n_divs = 0 
  return n_primes


print("")
print("count_primes()")
print(count_primes(100))

# Just for fun
def print_big(letter):
  alphabet = {"a": ["  *"," * *", "*****", "*   *", "*   *"], 
              "b":["****", "*   *", "****", "*   *", "****"], 
              "c":["*****","*","*","*","*****"],
              "d":["****","*   *","*   *","*   *","****"],
              "e":["*****","*","*****","*","*****"],
              }
  for row in alphabet[letter]:
    print(row)

print("")
print("print_big()")
print_big("a")

  