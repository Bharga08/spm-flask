class man:
#class attributes
    species='Homosapiens'
    def __init__(self,name,age,gender):    #class attribute
         self.name=name
         self.age=age
         self.gender=gender
h=man('bhagi',20,'f')
j=man('ramya',21,'f')
h.name='kaki'
j.name='kusu'
print(h.name,h.age,h.gender,h.species)
print(j.gender,j.age,j.name,j.species)
