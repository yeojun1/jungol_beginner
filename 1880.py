alpha='abcdefghijklmnopqrstuvwxyz'
key=input()
encoded=input()
decoded=''

for i in range(len(encoded)):
    j=encoded[i]
    if j==' ':
        decoded+=' '
        continue
    if j.isupper():
        decoded+=key.upper()[alpha.upper().index(j)]
        continue
    decoded+=key[alpha.index(j)]


print(decoded)