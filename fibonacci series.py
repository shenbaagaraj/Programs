# write a code to print fibonacci series 
n = int(input("Enter how many numbers have to print in the output : "))
first = 0
second = 1
for i in range(n):
    print(first,end='  ')
    tem = first
    first = second
    second = tem + first
    
