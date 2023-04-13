import random
player1=input('enter rock/paper/scissor:')
cpu=random.choice(('rock','paper','scissor'))
if player1==cpu:
    print("it is a draw")
elif player1=='rock':
    if cpu=='scissor':
        print('player1 rocks cpu shocks')
    else:
            print('cpu rocks player1 shocks')
elif player1=='paper':
    if cpu=='scissor':
        print('cpu rocks player1 shocks')
    else:
            print('player1 rocks cpu shocks')
elif player1=='scissor':
     if cpu=='paper':
         print('player1 rocks cpu shocks')
     else:
             print('cpu rocks player1 shocks')
else:
    print('there is a type erorr try again')
    
         
    
     
















              
