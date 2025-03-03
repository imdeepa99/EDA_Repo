# data structures in python
# there are 4 builtin data structures in pythen
# list: to stores the collection of datatypes
# list can have many datatypes like strings,int and boolean unlike in othere programming languages

fruits = ["apple", "banana", "cherry"]
print(fruits)

# list are indexed..>first item is 0 indexed and second is 1 and so on
# ,ordered can have duplicates changable

# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#
# If you add new items to a list, the new items will be placed at the end of the list.
fruits.append("mango")
print(fruits)# added at the last of the list so the lists are always ordered

print(type(fruits))
print(len(fruits))

# list comprehension--> shorter syntax when you want to create a new list based on existing list

# var=[expression for item in iterable if condition ='true']
fruits = ["apple", "banana", "cherry","fffff","aaaa"]# only want to make a new list with the letter conatining letter a
# new_list=[]
# for letter_a in fruits:
#     if "a" in letter_a:
#         new_list.append(letter_a)
#     print(new_list)

new_list=[letter_a for letter_a in fruits if "a" in letter_a]
print(("x isss", new_list))
fruits_item = ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]

print("lower", fruits_item)
another_list=[new_fruit if new_fruit!='banana' else 'orange' for new_fruit in fruits_item]
 # descending order

unh_list=["Ms in data","ds in civil","bs in psychology"] # sort is case sensitive means capital letters are treated first
unh_list.sort()

print(unh_list)

print(another_list)

# we cannot copy a list as it is just the reference of original one

list_1=[1,2,3,4,5]
list_1[1]=58 # so the list_2 is also updated
list_2=list_1
print(list_2)

# so using the copy method we can copy lists
list_5=[15,25,3,74,5]
list_3=list_5.copy()
list_5[0]=99# not modified in list_3
print(list_5)
print(list_3)
# if the list contains the sublists
import copy

list1 = [["apple", "banana"], ["cherry", "kiwi"]]
list2 = copy.deepcopy(list1)

list1[0][1] = "orange"

print(list1)  # Output: [['apple', 'orange'], ['cherry', 'kiwi']]
print(list2)  # Output: [['apple', 'banana'], ['cherry', 'kiwi']]
