# write a code for factorial 



n = int(input("enter the number : "))
result=1
# 5! = 5*4*3*2*1
# we need to go backward , right so use for loop
for i in range(n,0,-1):
    result=result*i
   
print("factoprial of",n,"is",result)