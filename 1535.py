result=[]
wordList=[]
while 1:
    inp=input().split()
    if inp[0]=='END': break
    for i in inp:
        if i not in wordList:
            wordList.append(i)
    result.append(' '.join(wordList))

for z in result:
    print(z)