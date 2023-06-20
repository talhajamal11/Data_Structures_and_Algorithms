"""
Chapter 10 of Jay Wengrow's book focuses on Recursion. The below are some examples of Python Functions 
that use recursion to solve simple problems.

Recursion has the following characteristics:
1. It needs a base case on which to break the recursion process - When writing a recursive function, start from the base case and
move upwards from there.
2. 
"""

def factorial(num:int) -> int:
    """
    Args:
        num (int): [The number to calculate the factorial for - must be positive]

    Returns:
        int: [Factorial for input number]
    """

    if num < 1:
        return "Number must be positive"
    else:
        if num == 1:
            return 1
        else:
            return num * factorial(num-1)
        
def fileTraversalSystem(dir:str) -> any:
    # File Traversal is possible using recursion only
    return None

if __name__ == '__main__':
    
    print(factorial(5))
