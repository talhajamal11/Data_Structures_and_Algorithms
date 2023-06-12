"""
Dictionaries in Python are Hash Maps
"""

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

print(isNumPresent(1, array))
