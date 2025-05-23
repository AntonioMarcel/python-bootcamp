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

result = lesser_of_two_evens(5,3)
print(result)

## 2
def animal_crackers(text):
  split_text = text.split(" ")
  return split_text[0][0] == split_text[1][0]
  
result = animal_crackers('Levelheaded Llama')
print(result)

## 3
def makes_twenty(n1, n2):
  if n1 + n2 == 20 or n1 == 20 or n2 == 20:
    return True
  else:
    return False

result = makes_twenty(8,12)
print(result)

# Level 1
## 1

def old_macdonald(text):
  count = 0
  new_string = ""
  
  for letter in text:
    if count == 0 or count == 3:
      new_string = new_string + letter.capitalize()
    else:
      new_string = new_string + letter
    count += 1
  
  return new_string

result = old_macdonald("macgonagal")
print(result)




