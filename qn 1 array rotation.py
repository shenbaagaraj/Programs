n=list(map(int, input("elements of array:-"). strip(). split()))
a = len(n)
k = int(input("enter the rotation value : "))
rev = a - (k%a)
ct = 0
while ct<a:
    if rev == a:
        rev = 0
    print(n[rev],end= " ")
    rev += 1
    ct += 1