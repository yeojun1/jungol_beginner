card=list(range(1,int(input())+1))

while card:
    print(card[0],end=" ")
    card.pop(0)
    if not card:
        break
    card.append(card[0])
    card.pop(0)