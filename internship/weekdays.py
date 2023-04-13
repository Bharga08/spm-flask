days=["sunday","monday","tuesday","wednesday","friday","saturday"]
user_input=int(input("enter a day 1-7:"))
if user_input:
    print(days[user_input-1])
else:
    print("the number is not valid")
    


days_dict={'1':"sunday",'2':"monday",'3':"tuesday",'4':"wednesday",'5':"thursday",'6':"friday",'7':"saturday"}
print(days_dict[input("enter a day(from 1-7):")])
