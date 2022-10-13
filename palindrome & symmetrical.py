from xml.dom import minidom


def palindrome(a):
    mid = (len(a)-1//2)
    start = 0
    last = len(a)-1
    flag = 0
    while start <= last:
        if a[start] == a[last]:
            start += 1
            last -=1
        
        else:
            flag = 1
            break
    
    if flag == 0:
        print("The string is palindrome")
    else:
        print("It is not palindrome")

def symmetry(a):
    sta = 0
    
    n = len(a)
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
    
    fin = mid 
    
    while (sta < mid and fin < n):
        if sta == fin:
            sta += 1
            fin += 1
        else:
            flag = 1 
            break 
    
    if flag == 0:
        print("This is symmetry")
    else:
        print("Asymmmetry")



       

a = "khokho"
symmetry(a)
string = "khokho"
palindrome(string)
