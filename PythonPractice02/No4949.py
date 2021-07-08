stack = []
while True:
    stack.clear()
    s = input()
    if s == ".":
        break
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            try:
                p = stack.pop()
                if p == "(":
                    pass
                else:
                    print("no")
                    break
            except:
                print("no")
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            try:
                p = stack.pop()
                if p == "[":
                    pass
                else:
                    print("no")
                    break
            except:
                print("no")
                break
        elif i == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
            