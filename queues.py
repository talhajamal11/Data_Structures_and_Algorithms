# Python Class to implement a Queue

class Queue:

    def __init__(self) -> None:
        self.queue = []
        return None

    def enqueue(self, element: str) -> None:
        self.queue.append(element)
        return None
    
    def dequeue(self) -> any:
        try:
            return self.queue.pop(0)
        except: 
            print("The queue is empty")
            return None
    
    def read(self) -> any:
        try:
            print(self.queue[0])
            return self.queue[0]
        except:
            print("The queue is empty")
            return None

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.dequeue()
    queue.read()
    

