k=list(map(int,input('enter  numbers with spaces').split()))
new_lst=list(filter(lambda x:x%2==0,k))
print(new_lst)
