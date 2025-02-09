inp=input()
KOI,IOI=0,0

for i in range(len(inp)-2):
    if inp[i]=="K" and inp[i+1]=="O" and inp[i+2]=="I":
        KOI+=1
    elif inp[i]=="I" and inp[i+1]=="O" and inp[i+2]=="I":
        IOI+=1

print(KOI,"\n",IOI,sep="")