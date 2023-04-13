class employee:
    def __init__(self,idl,name,dept):
        self.idl=idl
        self.name=name
        self.dept=dept
    def is_nightshift(self,choice):
        if choice=='yes':
            return 'he works in night shift'
        else:
            return 'works in morning shifts'
bhagi=employee(23965,'bhagi','IT')
kusu=employee(7625,'kusu','HR')

        
    
