# Python Class to implement a Queue

class Queue:

    """
    A queue needs to do the following three tasks:
    1. Insert objects at the end of the Queue
    2. Read objects at the front of the Queue
    3. Remove objects from the front of the Queue

    This can be accomplished with a simple array and some built in functions for lists in Python

    Queues are great for asynchronous requests like Printer Managers, call centers, patients waiting for a Doctor... etc
    """

    def __init__(self) -> None:
        # Create and Initialize an empty queue using a List
        self.queue = []
        return None

    def enqueue(self, element: str) -> None:
        # Add elements to end of the queue
        self.queue.append(element)
        return None
    
    def dequeue(self) -> any:
        # Remove and return the element at the front of the queue
        try:
            return self.queue.pop(0)
        except: 
            print("The queue is empty")
            return None
    
    def read(self) -> any:
        # Print and return the element at the beginning of the queue
        try:
            print(self.queue[0])
            return self.queue[0]
        except:
            print("The queue is empty")
            return None

class PrinterManager(Queue):

    def __init__(self) -> None:
        # Use inheritance and intialize a Queue Object for the Printer Manager
        super().__init__()
        self.queue = Queue()
        return None
    
    def queue_print_job(self, document:str) -> None:
        # Add a document to the Printer Manager's Queue
        self.queue.enqueue(document)
        return None

    def print(self, document:str) -> None:
        # Print the Document
        print(document)
        return None
        
    def run(self) -> None:
        # If there is anything in the queue, print it
        while (self.queue.read() == True):
            print(self.queue.read())
            self.queue.dequeue()
        return None
    


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.dequeue()
    queue.read()
    
