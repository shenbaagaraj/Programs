
n = int(input("enter value"))
for i in range(n+1):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz","the nunber is = ",str(i))
    else:
        if (i%3) == 0:
            print("fizz", "the number is ",str(i))
        elif (i%5) == 0:
            print("buzz","the number is ",str(i))
        else:
            print(str(i))


### in this code, initially created an empty list. using the for loop we can get the input from the user and append to the list which was existing.
# length of the list is alloted as end value for the "for loop". and the loop runs , results will shown in the terminal
### Thank you ###