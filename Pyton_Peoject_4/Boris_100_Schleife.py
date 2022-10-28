#!/usr/bin/env python
# coding: utf-8

# Exercise 1
# 
# Write a program that generates a random number (0-10) and ask you to guess it. You have three asserts.
# 
#     Define a random_number with randit between 0-10.
#     Initialize guesses_left to 3.
#     Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
#     Ask the user for their guess, just like the second example above.
#     If they guess correctly, print 'You win!' and break. Decrement guesses_left by one.
#     Use an else: case after your while loop to print:You lose.
# 

# In[9]:


from random import randint

# generate a number from 1 through 10 inclusive
random_number = randint(1,10)

guesses_left = 3
# start your game
while guesses_left > 0 :
    guess = int(input(" EAnter your guess"))
    if guess == random_number:
        print("you win")
        break
    guesses_left-=1
else:
    print (" you lose")


# Exercise 2
# 
# Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.

# In[10]:


hobbies = []
for i in range(3):
    hob = input("enter hobby")
    hobbies.append(hob)


# Exercise 3
# 
# REmember: The , character after our print statement means that our next print statement keeps printing on the same line. Let's filter out the letter 'A' from our string.
# 
# phrase = "A bird in the hand..."
# 
#     Do the following for each character in the phrase.
#     If char is an 'A' or char is an 'a', print 'X', instead of char. Make sure to include the trailing comma.
#     Otherwise (else:), please print char, with the trailing comma.
# 

# In[18]:


phrase = " A bird in a the hand "
for char in phrase:
    if char == "A" or char == "a":
        print("X")
    else:
        print (char)


# Exercise 4
# 
# Define a function is_even that will take a number x as input.If x is even, then return True. Otherwise, return False. Note: even means that is divisible by two.Check if it works.

# In[19]:


def is_even(x):
    if x%2 == 0 :
        return True
    else:
        return False


# In[20]:


is_even(7)


# Exercise 6
# 
# Let's try a factorial problem. To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example: 3! is equal to 123

# In[35]:


def factorial(x):
    count = 1
    for i in range(x):
        count = count*(i + 1)
    return count


# In[36]:


factorial(11)


# Exercise 7
# 
# Define a function called count that has two arguments called sequence and item. Return the number of times the item occurs in the list.For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

# In[49]:


def count(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total


# In[50]:


count([1,2,1,1,1,3],1)


# Exercise 8
# 
# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.For example: remove_duplicates([1,1,2,2]) should return [1,2].

# In[57]:


def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# In[58]:


remove_duplicates([1,1,3,4,5,6,6,7,7,8,3])


# Exercise 3
# 
# Follow the steps:
# 
#     First, make a list called groceries with the values "banana","orange", and "apple".
#     Define this two dictionaries:
# 
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# 
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# 
#     Define a function compute_bill that takes one argument food as input. In the function, create a variable total with an initial value of zero.For each item in the food list, add the price of that item to total. Finally, return the total. Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.
#     Make the following changes to your compute_bill function:
#         While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
#         If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
# 

# In[ ]:




