import random
player2= random.choice([1,2,3])
player1str= input("enter your choice: ")
player1Dict={"snake":1,"water":2,"gun":3}
player1= player1Dict[player1str]
reverseDict={1:"snake",2:"water",3:"gun"}


print("player1 chooses: ",reverseDict[player1])
print("player 2 chooses: ",reverseDict[player2])

if(player1==player2):
    print("it's a draw")

else:    


    if(player1==1 and player2==2):
        print("player 1 wins")
    elif(player1==2 and player2==3):
        print("player 1 wins")
    elif(player1==3 and player2==1):
        print("player 1 wins")
    elif(player1==1 and player2==3):
        print("player 2 wins")
    elif(player1==2 and player2==1):
        print("player 2 wins")
    elif(player1==3 and player2==2):
        print("player 2 wins")
    else:
        print("something went wrong")




