class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False


def PostfixEvaluation(string):
    stack = Stack()
    for a in string:
        if a.isdigit():
            stack.push(a)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if a == '+':
                value = int(num1) + int(num2)
                stack.push(value)
            elif a == '-':
                value = int(num2) - int(num1)
                stack.push(value)
            elif a == "*":
                value = int(num1) * int(num2)
                stack.push(value)
            elif a == "/":
                try:
                    value = int(num2)/int(num1)
                    stack.push(value)
                except ZeroDivisionError:
                    print("Can not divide by 0")
            else:
                value = int(num2)**int(num1)
                stack.push(value)

    return stack.pop()


if __name__ == '__main__':
    while True:
        Input = input("Enter the expression:")
        print("The result is:", PostfixEvaluation(Input))