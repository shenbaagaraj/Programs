lower = int(input("Enter the lower value interval: "))
upper = int(input("Enter the upper value interval :"))
for i in range(lower , upper+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)