from stack import Stack

def check(mul):
    stack = Stack()
    for i in mul:
        if i == "(":
            stack.push(i)
        elif i == "{":
            stack.push(i)
        elif i == "[":
            stack.push(i)
        elif i == ")":
            if stack.pop() == "(":
                pass
            else:
                return(False)
        elif i == "}":
            if stack.pop() == "{":
                pass
            else:
                return(False)
        elif i == "]":
            if stack.pop() == "[":
                pass
            else:
                return(False)
    return stack.is_empty()

print(check("(1+2+[3+4]+5)"))