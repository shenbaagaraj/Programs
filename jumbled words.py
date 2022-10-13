import random
def choose():
    lis = ["water","titanic","anaconda","sita","mahabharatam"]
    pick = random.choice(lis)
    return pick 
def jumble(word):
    jumbled = "".join(random.sample(word),len(word))
    return jumbled
def thank(p1name,p2name,pp1,pp2):
    print("Thank you",p1name,"Your score is ",pp1)
    print("Thank you",p2name,"Your score is ",pp2)
    print("Thanks for playing")
 

def play():
    player1_name = input("Player1 name, Enter your name :")
    player2_name = input("Player2 name, Enter your name :")
    player1score = 0
    player2score = 2
    turn = 0
    while True:
        pickword = choose()
        qn = jumble(pickword)

        if turn % 2 == 0:
            print(player1_name,"Your Turn")
            print(qn)
            answer = input("Enter your answer : ")
            if answer == pickword:
                print("Congrats,Right answer")
                player1score += 1
                print("Type go ahead to continue , exit to quit the game ")
                wor = "exit"
                option = input("Enter your option")
                option.lower()
                if option == wor:
                    thank(player1_name,player2_name,player1score,player2score)
                    break

            else:
                print("Oops,Better Luck next time ")
                print("I thought the right answer is : ",pickword)
        else:
            print(player2_name,"Your Turn")
            print(qn)
            answer = input("Enter your answer : ")
            if answer == pickword:
                print("Congrats,Right answer")
                player2score += 1
                print("Type go ahead to continue , exit to quit the game ")
                wor = "exit"
                option = input("Enter your option")
                option.lower()
                if option == wor:
                    thank(player1_name,player2_name,player1score,player2score)
                    break
            else:
                print("Oops,Better luck next time")
                print(" I thought the right answer is",pickword)
        turn += 1
                
            