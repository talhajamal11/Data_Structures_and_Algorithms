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

    def __init__(self) -> None:
        
        pass

if __name__ == '__main__':



