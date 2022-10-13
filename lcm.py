def lcm(number1 , number2):
    if number2 > number1:
        greater = number2
    else:
        greater = number1
    
    while True:
        if (greater % number1 == 0 )and (greater % number2) == 0:
            break
        
        greater += 1
    return greater
print(lcm(10,32))