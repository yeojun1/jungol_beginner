queue=[]
for _ in range(int(input())):
    command=input()
    match command[0]:
        case "i":
            queue.append(command[2:])
        case "o":
            if queue:
                print(queue[0])
                queue.pop(0)
            else:
                print("empty")
        case "c":
            print(len(queue))