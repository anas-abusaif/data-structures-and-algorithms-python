from stack_and_queue.stack import Stack


def validate_brackets(string):
    open = ["[","{","("]
    close= ["]","}",")"]
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()
    stack4 = Stack()
    stack5 = Stack()
    stack6 = Stack()
    for value in string:
        if value in open:
            if value == '(':
               stack1.push(value)
            elif value == '[':
                stack2.push(value)
            else:
                stack3.push(value)
        elif value in close:
            if value == ')':
               stack4.push(value)
            elif value == ']':
                stack5.push(value)
            else:
                stack6.push(value)

    if len(stack1) == len(stack4) and len(stack2) == len(stack5) and len(stack3)==len(stack6):
        return True
    else:
        return False

