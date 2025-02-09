stack=[]
for _ in range(int(input())):
    command=input()
    match command[0]:
        case "i":
            stack.append(command[2:])
        case "o":
            if stack:
                print(stack[len(stack)-1])
                stack.pop(len(stack)-1)
            else: print("empty")
        case "c":
            print(len(stack))