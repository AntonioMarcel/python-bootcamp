# 1
print("1-------")
st = 'Print only the words that start with s in this sentence'
word_list = st.split(" ")

for word in word_list:
  if word.startswith("s"):
    print(word)

# 2
print("2-------")
for num in range(11):
  if num % 2 == 0:
    print(num)

# 3
print("3-------")
my_list = [num for num in range(1,51) if num % 3 == 0]
print(my_list)

