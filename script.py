# Numbers
# 1
exp = (((5 * 5 - 5) / 2 ) ** 2 ) + 0.25
print(exp)
# 2
print(4 * (6 + 5)) #44
print(4 * 6 + 5 ) #29
print(4 + 6 * 5) #34
# 3
print(type(3 + 1.5 + 4))
# 4
print(4**2)
print(4**1/2)

# String
s = 'hello'
# 1
print(s[1])
# 2
print(s[::-1])
# 3
print(s[-1])
print(s[4])

# List
#1
my_list1 = [0,0,0]
my_list2 = list((0, 0, 0))
print(my_list1)
print(my_list2)
#2
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)
#3
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#Dictionaries
#1
d = {'simple_key':'hello'}
print(d["simple_key"])
#2
d = {'k1':{'k2':'hello'}}
print(d["k1"]["k2"])
#3
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"][0]["nest_key"][1][0])
#4
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])


original = {'b': 1, 'a': 3, 'c': 2}
sorted_dict = dict(sorted(original.items(), key=lambda item: item[1]))
print(sorted_dict)  # {'a': 1, 'b': 2, 'c': 3}
