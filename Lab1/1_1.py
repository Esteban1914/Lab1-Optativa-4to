
def isPalindrome(element):
     return element == element[::-1]

"""
def isPalindrome0(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True  
def isPalindrome1(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False    
"""
if __name__=='__main__':
    my_list=[]
    for i in range(5):
        while True:
            my_string=input("Palabra {}/5:\n".format(i+1))
            if my_string.__len__() % 2 != 0:
                break             
            print("Palabra no valida")
        my_list.append(my_string)
    for element in my_list:
        if isPalindrome(element):
            print("[OK] Palabra '{}' es palindromo".format(element))
        else:
            print("[X] Palabra '{}' NO es palindromo".format(element))
    


