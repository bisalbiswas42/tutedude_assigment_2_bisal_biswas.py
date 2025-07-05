a=0
c=int(input('enter the first tern: '))
d=int(input('enter the second tern: '))
for b in range(c,d+1):
    a=a+b
    if b==d:
        print("sum of number from",c,"to",d,"is:",a)
