# Write a list comprehension to generate a list of squares of even numbers from 1 to 20.
from pygments.lexer import words

t=[item**2 for item in range(1,100) if item%2==0]
print(t)

# Given a list of words, use list comprehension to create a new list containing only the words that have the letter 'a'.
words = ["apple", "banana", "cherry", "kiwi", "mango", "grape"]
only_a= [element for element in words if element.__contains__("a")]
a=[new_a for new_a in words if 'a' in new_a]
print("first", a)
print(only_a)# both returns the same result


#Given a string, use list comprehension to extract all vowels from it.
sentence = "Hello World, Python is amazing!"
vowels=[words for words in sentence if words.lower() in "aeiouu"]
print("coo",vowels)

# Given a list of numbers, use list comprehension to remove duplicates and return a sorted list.
numbers = [4, 2, 9, 1, 2, 6, 4, 7, 9, 8, 6]
numbers.sort()
set_1=set(numbers)
print(set_1)

unique_num=[]
[unique_num.append(num) for num in numbers if num not in unique_num]
unique_num.sort()
print("another approach", unique_num)

# Use dictionary comprehension to create a dictionary where keys are numbers from 1 to 10,
# and values are their squares.

square_dict={num: num**2 for num in range(1,11) }
print(square_dict)

# farenheight to celcius

# List of temperatures in Fahrenheit
fahrenheit_temps = [32, 50, 77, 104, 212]

# Convert to Celsius using list comprehension
celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]

print(celsius_temps)
# Given a sentence, create a dictionary where keys are words and values are their frequencies.
sentence = "python is fun and python is powerful"
wordss=sentence.split()
print(wordss)
sen_dict={word: wordss.count(word) for word in set(wordss)}
print(sen_dict)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3=set1.intersection(set2)
print((set3))

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

dict1.update(dict2)  # This modifies dict1 by adding key-value pairs from dict2
print(dict1)

# 10. Find the Most Frequent Element
# Given a list, find the most frequently occurring element.

numbers = [1, 3, 3, 2, 1, 3, 4, 1, 1]
count=0
num={}
for fo in numbers:
    if fo in num:
        num[fo]+=1
    else:num[fo]=1
most_freq=max(num,key=num.get)
print("mf",most_freq)




