import string
import random

symbols = list(string.ascii_letters)
card1 = [0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
#pos1 and pos2 are the samesymbol positions in both card 1 and card 2 respectively
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)

if pos1 == pos2:
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i = 0 
while i<5:
    if (i!= pos1 and i!= pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        card1[i]=alphabet1
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card2[i]=alphabet2
    i += 1

print(card1)
print(card2)

yourchoice = input("Spot the similarity : ")
if yourchoice == samesymbol:
    print("You are right")
else:
    print("Wrong,Better luck next time ")





