# Functions and Methods Homework
## 1
import math
import string

def vol(rad):
  return 4/3*math.pi*rad**3

print("vol(rad)")
print(vol(2))

## 2
def ran_check(num, low, high):
  if num >= low and num <= high:
    return f"{num} is in the range between {low} and {high}"
  else:
    return False
      
def ran_bool(num, low, high):
  if num >= low and num <= high:
    return True
  else:
    return False
print("")
print("ran_check(num, low, high)")
print(ran_check(3, 3, 7))
print("ran_bool(num, low, high)")
print(ran_bool(5, 2, 7))

##3
def up_low(s):
  n_upper = 0
  n_lower = 0
  
  for l in s:
    if l.isupper():
      n_upper += 1
    elif l.islower():
      n_lower += 1

  return f"{n_upper}, {n_lower}"

print("")
print("up_low(s)")
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

## 4
def unique_list(lst):
  return list(set(lst))

print("")
print("unique_list(lst)")
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

## 5
def multiply(numbers):  
  result = 1
  for n in numbers:
    result *= n

  return result

print("")
print("multiply(numbers)")
print(multiply([1,2,3,-4]))

## 6
def palindrome(s):
  s = s.replace(" ", "")
  return s == s[::-1]

print("")
print("palindrome(s)")
print(palindrome("helleh"))

## Hard
def pangram(s):
  alphabet_list = [l for l in string.ascii_lowercase]

  return sorted(list(set("".join(s.replace(" ", "").lower())))) == alphabet_list

print("")
print("pangram(s)")
print(pangram("hi"))
print(pangram("The quick brown fox jumps over the lazy dog"))