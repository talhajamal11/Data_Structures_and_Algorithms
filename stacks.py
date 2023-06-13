"""
This Python Script is a sample script to write code for Stacks
"""

class Stack:
    """
    Class for Stack Data Structure. This DS has three rules/functions:
    1. Insert at the end. 
    2. Remove from the end. 
    3. Read from the end.
    """
    def __init__(self) -> None:
        self.stack = []
        pass

    def push(self, element) -> None:
        self.stack.append(element)
        pass

    def pop(self) -> None:
        self.stack.pop()
        pass
    
    def read(self) -> any:
        try:
            return self.stack[-1]
        except:
            print("The stack is empty")    

class Linter:
    """
    This Class simulates a Linter for code that handles brackets 
    It identifies three errors:
        Error 1: An opening bracket was never followed up with a closing bracket
        Error 2: A closing bracket was never preceded by an opening bracket
        Error 3: An incorrect bracket being used to close a bracket
    
    Opening brackets are pushed onto the stack
    If Closing brackets are found, the stack is popped
    If the popped element is not of the same type as the closing bracket -> Error 3 identified
    If there was no popped element, stack is empty, there was no preceding barcket -> Error 2 identified
    If we have reached the end of the program but the stack is not empty -> Error 1 identified
    """
    def __init__(self) -> None:

        pass

if __name__ == '__main__':
    file_path = "/Users/talhajamal/Documents/Coding Practice/Data Structures and Algorithms/binary_search.py"
    with open(file_path) as f:
        code = f.readlines()
    
    print(code)