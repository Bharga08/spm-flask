a={'sno':[1,2,3,4],'names':['bhagi','sai','kaki','kusu']}
b={'gender':['female','male'],'place':['bangloore','chennai']}
x=(**a,**b)
c=a.copy()
c.update(b)
print(c)


   
