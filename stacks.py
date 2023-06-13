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
        try:
            self.stack.pop()
        except:
            print("The stack is empty - cannot pop from empty stack")
        
    
    def read(self) -> any:
        try:
            return self.stack[-1]
        except:
            print("The stack is empty")

    def size(self) -> any:
        return len(self.stack)    

class Linter(Stack):
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
        self.linter = Stack()
        self.bracketsDictionary = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        pass


    def isOpeningBracket(self, element) -> bool:
        if element == "(":
            return True
        else:
            return False

    def isOpeningSquareBracket(self, element) -> bool:
        if element == "[":
            return True
        else:
            return False
    
    def isOpeningCurlyBracket(self, element) -> bool:
        if element == "{":
            return True
        else:
            return False
        
    def isClosingBracket(self, element) -> bool:
        if element == ")":
            return True
        else:
            return False

    def isClosingSquareBracket(self, element) -> bool:
        if element == "]":
            return True
        else:
            return False
    
    def isClosingCurlyBracket(self, element) -> bool:
        if element == "}":
            return True
        else:
            return False
        
    def matchBrackets(self, element:str, comparison:str) -> bool:
        if self.bracketsDictionary[element] == comparison:
            return True
        else:
            return False

    def identifyError2AndError3(self, element) -> any:
            comparison = self.linter.pop()
            try:
                self.linter.pop()
                if self.matchBrackets(element, comparison) == True:
                    pass
                else:
                    return "Brackets do not match -> Error 3 identified"
            except:
                return "Stack was empty -> Error 2 identified" 
    
    def identifyError1(self) -> any:
        if self.linter.size() != 0:
            return "Stack is not empty -> Error 1 identified"

    def read_text(self, element) -> any:

        # If element is opening bracket, push it onto the Stack
        if (self.isOpeningBracket(element) == True):
            self.linter.push(element)
        if (self.isOpeningSquareBracket(element) == True):
            self.linter.push(element)
        if (self.isOpeningCurlyBracket(element) == True):
            self.linter.push(element)


        # If element is closing bracket, pop the stack and compare the current element with the popped element
        if (self.isClosingBracket(element) == True):
            self.identifyError2AndError3(element)

        if (self.isClosingCurlyBracket(element) == True):
            self.identifyError2AndError3(element)
            
        if (self.isClosingSquareBracket(element) == True):
            self.identifyError2AndError3(element)
            
        self.identifyError1()


if __name__ == '__main__':

    # Taking another Python File as sample to test Linter
    file_path = "/Users/talhajamal/Documents/Coding Practice/Data Structures and Algorithms/test.py"
    with open(file_path, "r") as f:
        code = f.read()
        code = code.replace(" ","")
    
    #print(code)

    bracket_linter = Linter()

    for character in code:
        print(bracket_linter.read_text(character))
