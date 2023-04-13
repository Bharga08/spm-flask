'''import time
k=input('enter numbers with spaces')
print(k.split())

l=[]
for i in k.split():
    l.append(int(i))
print(l)'''
def square(a):
    return a**2
lst=list(map(float,input('enter numbers with spaces').split()))
new_lst=list(map(square,lst))
print(new_lst)

