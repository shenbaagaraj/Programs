def check_vow(string,vowels):
    res = [letter for letter in string if letter in vowels]
    print(res)
    print(len(res))

string = "Shenbagaraj"
vowels = "aeiou"
check_vow(string,vowels)