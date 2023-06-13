"""
Dictionaries in Python are Hash Maps
"""
from array import array
import string


# Searching for a number inside an array can be done linearly - this would have a time complexity of O(n)
# Searching for a number inside an array can be done via an algo like Binary Search which would have a time complexity
# of O(log(n)), but the array would need to be ordered
# The fastest way would be to use a hashmap - this would reduce the time complexity down to O(1)

def isNumPresent(num, array):
    hashmap = {}
    for i in array:
        hashmap[i] = True

    try: 
        if hashmap[num] == True:
            return True
    except:
        return False

array = [5,2,3,1,4]

print("Chapter Question: Is number present: {}".format(isNumPresent(-1, array)))

def isArraySubset(array1: array, array2: array) -> bool:
    """
    Write a function to determine of one array is a subset of another array
    The function should use a hashmap
    """
    
    # First we need to determine which array is the larger array

    if len(array1) > len(array2):
        largerArr = array1
        smallerArr = array2
    else:
        largerArr = array2
        smallerArr = array1

    # Create a hashmap and fill the keys with the largerArray's values and values as Boolean
    hashmap = {}

    for i in largerArr:
        hashmap[i] = True
    
    for j in smallerArr:
        try:
            if hashmap[j] == True:
                continue
        except:
            return False
    
    return True

array1 = [1, 2, 4, 2, 5, 9]
array2 = [10]
print("Chapter Question: If the smaller Array a subset of the Larger Array: {}".format(isArraySubset(array1, array2)))


def returnIntersection(array1: array, array2: array) -> array:
    """
    Exercise 1: Write a function that returns the intersection of two arrays. The intersection is a third array that contains
    all values within the first two arrays. The function should have a complexity of O(N)
    """
    
    # Determine larger array and store that in an Index (hashmap) to lookup

    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    hashmap = {}

    for value in largerArray:
        hashmap[value] = True
    
    outputArray = []

    for value in smallerArray:
        try:
            if hashmap[value] == True:
                outputArray.append(value)
        except:
            continue

    if len(outputArray) == 0:
        return "No intersection found!"
    else:
        return outputArray    

array1 = [1, 2, 4, 2, 5, 9]
array2 = [1, 9]
print("Exercise Q1: Intersection of two arrays: {}".format(returnIntersection(array1, array2)))



"""
Write a function that accepts an arrray of strings and returns the first duplicate value it finds.
Make sure the function has an efficiency of O(N)
"""

def duplicateString(arr: array) -> any:
    
    hashmap = {}
    for i in arr:
        try: 
            if hashmap[i] == True:
                return i        
        except:
            hashmap[i] = True

    return "No duplicate found"

duplicate_array = ["a", "b", "c", "d", "e"]
print("Exercise Q2: Looking for Duplicate: {}".format(duplicateString(duplicate_array)))



"""
Write a function that accepts a string that contains all the lettters of the alphabet except one and returns the missing letter.
The function should have the time complexity of O(N)
"""

def returnMissingLetter(phrase: str) -> str:
    # Take input, make it lowercase and strip any spaces
    phrase = phrase.replace(" ", "").lower()
    # Get a list of all letters in the alphabet
    letters = list(string.ascii_lowercase)
    # Make Hashmap of the alphabets inside the phrase - this is our Lookup Index
    hashmap = {}
    for alphabet in phrase:
        hashmap[alphabet] = True

    # Compare each letter in the alphabet with the Lookup Index
    for i in letters:
        try: 
            if hashmap[i] == True:
                continue
        except:
            return i
        
    return "No letters missing"

test_string = "the quick brown box jumps over a lazy dog"
print("Exercise Q3: Testing for Missing Letter: {}".format(returnMissingLetter(test_string)))



"""
Write a function that returns the first non-duplicated character in a string.
The function should have an efficiency of O(N)
"""

def returnFirstUnique(phrase: str) -> str:
    # Remove whitespaces and make phrase lowercase
    phrase = phrase.replace(" ", "").lower()
    # Create an empty hashmap for lookup index - fill the hashmap with the letters as Keys and the number of times the letter
    # exists as the value
    hashmap = {}
    for letter in phrase:
        try:
            if hashmap[letter] == True:
                hashmap[letter] += 1
        except:
            hashmap[letter] = 1

    # Iterate of the phrase and hashmap to find the key value pair with 1 value - return the key
    for i in range(0, len(phrase)):
        if hashmap[phrase[i]] == 1:
            return phrase[i]
        
    return "No unique letter"

nonduplicate_phrase = "remember"
print("Exercise Q4: The First Unique letter in your phrase is: {}".format(returnFirstUnique(nonduplicate_phrase)))