a="Hello Codegnan"
w=0
upper=0
lower=0
l_w=a.split()
w=len(l_w)
for i in a:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
print("number of uppercase letters:",upper)
print("number of lowercase letters:",lower)
print("numbers of worda",w)



    

    

    

