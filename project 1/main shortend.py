''' 
1 for snake
-1 for water 
 0 for gun'''
import random
computer =random.choice([-1,0,1])
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]

#By now we have 2 numbers(variables),you and computer.

print(f"you chose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")
if(computer==you):
    print("its a draw")
else:
    # if(computer==-1 and you==1):   (computer-you)=-2
    #     print("you win!")    
    # elif(computer==-1 and you==0):   ( computer-you)=-1
    #     print("you lose!")    
    # elif(computer==1 and you==-1):   (computer-you)=2
    #     print("you lose!") 
    # if(computer==1 and you==0):      (computer-you)=1
    #     print("you win!") 
    # elif(computer==0 and you==-1):  (computer-you)=1
    #     print("you win!")    
    # elif(computer==0 and you==1):   ( computer-you)=-1
    #     print("you lose!")   
    # else:
    #     print("something went wrong!")  
    
    #->in short 
    
    if((computer-you)== -2 or (computer -you)==1):
        print("you win!")
    else:
        print("you lose!")    