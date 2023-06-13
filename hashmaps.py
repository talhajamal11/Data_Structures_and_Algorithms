"""
Dictionaries in Python are Hash Maps
"""
from array import array


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

print("Is number present: {}".format(isNumPresent(-1, array)))

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
print("If the smaller Array a subset of the Larger Array: {}".format(isArraySubset(array1, array2)))


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
print("Intersection of two arrays: {}".format(returnIntersection(array1, array2)))



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
print("Looking for Duplicate: {}".format(duplicateString(duplicate_array)))