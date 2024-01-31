# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
## void push(int x) Pushes element x to the back of the queue.
## int pop() Removes the element from the front of the queue and returns it.
## int peek() Returns the element at the front of the queue.
## boolean empty() Returns true if the queue is empty, false otherwise.

# Notes: You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.

class MyQueue(object):
    # define two stacks
    # firstDown is used for push
    # firstUp is used for pop and peek
    def __init__(self):
        """
        Initialize data structure
        """
        self.firstDown = []
        self.firstUp = []

    # when push, push to firstDown
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.firstDown.append(x)
        
    # when pop, check if firstUp is empty
    # if firstUp is empty, pop all elements from firstDown and push to firstUp
    # then pop firstUp
    def pop(self):
        """
        :rtype: int
        """
        if len(self.firstUp) == 0:
            while len(self.firstDown) > 0:
                self.firstUp.append(self.firstDown.pop())
        return self.firstUp.pop()

    # when peek, check if firstUp is empty
    # if firstUp is empty, pop all elements from firstDown and push to firstUp
    # then peek firstUp
    def peek(self):
        """
        :rtype: int
        """
        if len(self.firstUp) == 0:
            while len(self.firstDown) > 0:
                self.firstUp.append(self.firstDown.pop())
        return self.firstUp[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.firstDown) == 0 and len(self.firstUp) == 0
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
    
# Testing with example file
if __name__ == "__main__":
    file_name = "232.test_data.txt"
    with open(file_name, 'r') as f:
        # Read the first line of the file with commands and the second line with parameters
        commands = f.readline().strip().split(',')
        params = f.readline().strip().split(',')
        output = []
        for i in range(len(commands)):
            # Remove whitespace and quotes from commands
            command = commands[i].strip().strip('\"')
            # Remove whitespace and square brackets from params
            param = params[i].strip().strip('[]')
            if (command == "MyQueue"):
                obj = MyQueue()
                output.append(None)
            elif (command == "push"):
                obj.push(int(param))
                output.append(None)
            elif (command == "pop"):
                output.append(obj.pop())
            elif (command == "peek"):
                output.append(obj.peek())
            elif (command == "empty"):
                output.append(obj.empty())
            else:
                print("Invalid command: {}".format(command))
        print(output)