from datetime import datetime


if __name__=='__main__':
    my_list=[
        "N:Amanda,CI:03062224105,A:Industrial",
        "N:Alberto,CI:03082165760,A:Mecanica",
        "N:Maria,CI:97022324402,A:Civil",
        "N:Melisa,CI:99052234145,A:Arquitectura",
        "N:Claudia,CI:03082124902,A:Quimica",
    ]
    def myFunc(e):
        try:
            if e[e.find("CI:")+3 : e.find("CI:")+5] >  datetime.today().year.__str__()[2:]:
                return '1'+ e[e.find("CI:")+3 : e.find("CI:")+9]
            else:
                return '2'+e[e.find("CI:")+3 : e.find("CI:")+9]
        except:
            print("Ha ocurrido un error")
            return None
    my_list.sort(key=myFunc)
    for element in my_list:
        print(element)