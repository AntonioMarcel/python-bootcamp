# 1 
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError as e:
        print("Not possible to exponentiate string type.")

print("")

# 2
x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError as e:
    print("Not possible to divide by zero.")
finally:
    print("All done!")

print("")

# 3
def ask():
    while True:
        try:
            my_num = int(input("Choose an integer: "))
        except ValueError as e:
            print("Incorrect type!")
        else:
            print(my_num**2)
            break

ask()