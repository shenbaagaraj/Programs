
n = int(input("Enter the number : "))
x = int(input("Enter your choice : "))
element = []

for i in range(n):
    element.append(i)

print(element)
count = 0
if (x<500):
    for i in range(500):
        if i == x:
         count +=1
         if (i==x):
            print("Yes! , Found the number at position : ", str(i))
            break
elif (x>500 and x<1000):
    for i in range(500,1000):
        count +=1
        if (i==x):
            print("Yes!, Found the number at position : ",str(i))
            break
elif (x>1000 and x <1500):
    for i in range(1000,1501):
        count += 1
        print("Yes!, Found the number at position : ",str(i))
        break
else:
    print("Couldn't able to find the position")

print("Number of iterations taken : ",str(count))




    


