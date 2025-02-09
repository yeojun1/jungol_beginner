_ = int(input())
command = list(input().split())
number = []

for i in range(len(command)):
    if command[i] in ["+","-","*","/"]:
        a = int(number.pop())
        b = int(number.pop())
        match command[i]:
            case "+": number.append(b+a)
            case "-": number.append(b-a)
            case "*": number.append(b*a)
            case "/": number.append(b/a)
    else: number.append(command[i])

print(int(number[0]))