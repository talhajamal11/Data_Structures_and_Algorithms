"""
Chapter 10 of Jay Wengrow's book focuses on Recursion. The below are some examples of Python Functions 
that use recursion to solve simple problems.

Recursion has the following characteristics:
1. It needs a base case on which to break the recursion process - When writing a recursive function, start from the base case and
move upwards from there.
2. 
"""
from array import array

def factorial(n:int) -> int:
    """
    Args:
        num (int): [The number to calculate the factorial for - must be positive]

    Returns:
        int: [Factorial for input number]
    """

    if n < 1:
        return "Number must be positive"
    else:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
        
def fileTraversalSystem(dir:str) -> any:
    # File Traversal is possible using recursion only
    return None

# Question 1: Function to print every other number from a low number to a high number
def everyOtherNumber(low:int, high:int) -> None:
    if low > high:
        return None 
    else:
        print(low)
        everyOtherNumber(low+2, high)


# Question 2: Factorial uses n-2 instead of n-1

def factorialComplicated(n:int) -> int:
    """
    if n < 1:
        return "input must be greater than or equal to 1"
    else:
        if n == 1:
            return n
        else:
            return n * factorialComplicated(n-2)
    """
    # This function leads to infinite recursion as we never reach the base case
    return None
        
# Questions 3: Function that calculates the sum of all numbers between low and high

def sumRange(low:int, high:int) -> int:
    if low > high:
        return "Low must be greater than High"
    if low == high:
        return low
    if low < high:
        return low + sumRange(low+1, high)

# Question 4: Take an array containing numbers and arrays inside it. Write a recursive function that prints all the numbers
def printNumber(arr: array) -> int:
    """
    Loop over the entire array -> if the value is an array, recursively call the function, otherwise print the value
    Args:
        array (array): [Input Array]

    Returns:
        int: [Print all numbers inside this array]
    """
    for value in arr:
        if type(value) == list:
            printNumber(value)
        else:
            print(value)




if __name__ == '__main__':
    
    print(factorial(5))
    everyOtherNumber(6,11)
    print(factorialComplicated(4))
    print(sumRange(1,10))

    arr = [
        1,
        2,
        3,
        [4, 5, 6],
        7,
        [8,
            [9, 10, 11,
                [12, 13, 14]
            ]
        ],
        [15, 16, 17, 18, 19,
            [20, 21, 22,
                [23, 24, 25,
                    [26, 27, 29]
                ], 30, 31        
            ], 32
        ], 33
          
    ]
    printNumber(arr)
