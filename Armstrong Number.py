# print a armstrong number 
for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
    while i != 0:
        dig = i%10
        result = result + dig**n
        i = i//10
    if num == result:
        print("The number is armstrong is ",result)
