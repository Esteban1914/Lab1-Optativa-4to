
if __name__=='__main__':
    while True:
        cadenas=input("8 Cadenas:\n")
        my_list=cadenas.split(", ")
        my_cond=my_list.__len__()
        class MyException(Exception):
            pass
        try:
            if my_cond != 8:
                raise MyException("Solo hay {}/8 cadenas separadas por ','+' '".format(my_cond))
            my_cond=True
            for element in my_list:
                if element.isalpha()==False:
                    raise MyException("Cadena '{}' tiene caracteres que no son letras".format(element))
            break
        except MyException as exception:
            print(exception.args[0])
    for count in range(my_list.__len__()):
        my_list[count]=my_list[count].lower()
    def myFunc(e):
        return len(e)
    my_list.sort(key=myFunc)
    for element in my_list:
        print(element)
        