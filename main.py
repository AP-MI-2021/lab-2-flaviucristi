def get_temp(temp,frm,to):
    '''
    Transforma un tip de grade in alt tip de grade
    :param x: Numarul de grade
    :param t1: Tipul in care sunt gradele
    :param t2: Tipul in care trebuie sa se transforme gradele
    :return: Returneaza numarul de grade in tipul dat, t2
    '''
    if frm=="C":
        if to=="K":
            return temp+273.15
        else:
            return (temp*1.8)+32
    elif frm=="F":
        if to=="C":
            return (temp-32)*(5/9)
        else:
            return (temp-32)*(5/9)+273.15
    else:
        if to=="C":
            return temp-273.15
        else:
            return temp*(9/5)-459.67


def cmmdc(x,y):
    d = x
    i = y
    while i > 0:
        r = d % i
        d = i
        i = r
    return d

def get_cmmmc(list):
    '''
    Calculeaza cmmmc a n numere
    :param list: Lista cu numere intregi
    :return: Returneaza cmmmc
    '''
    d=0
    c=1
    for i in list:
        c = c*i//cmmdc(c,i)

    return c


def numarprim(x):
    if x<2:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                return False

    return True

def get_largest_prime_below(n):
    c=int(n)
    c=c-1
    while numarprim(c)==False:
        c=c-1

    return c


def test_get_largest_prime_below():
    assert get_largest_prime_below("4")==3
    assert get_largest_prime_below("16")==13
    assert get_largest_prime_below("23")==19
    assert get_largest_prime_below("26")==23
    assert get_largest_prime_below("145")==139

def test_get_temp():
    assert get_temp(20,"C","K") == 293.15
    assert get_temp(20, "C", "F") == 68
    assert get_temp(300, "F", "C") == 148.88888888888889
    assert get_temp(300, "K", "F") == 80.32999999999998

def test_get_cmmmc():
    assert  get_cmmmc(list=[1,2,3,4,5]) == 60
    assert get_cmmmc(list=[2,3,4]) == 12
    assert get_cmmmc(list=[12,24,2]) == 24
    assert get_cmmmc(list=[15,5,20]) ==  60

def citire():
    list = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        list.append(int(input("Dati elemente: ")))

    return list



def main():


    while True:

        print(test_get_cmmmc())
        print(test_get_temp())
        print(test_get_largest_prime_below())

        print("1.Determina numarul de grade dintr-un tip dat in alt tip dat.")
        print("2.Determina cmmmc a n numere.")
        print("3.Determina ultimul num??r prim mai mic dec??t un num??r dat")
        print("x.Iesire")

        list = []
        optiune = input("Dati optiune: ")

        if optiune=="1":
            temp=float(input("Dati numarul de grade: "))
            frm=input("Dati tipul gradelor: ")
            to=input("Dati tipul in care doriti sa se transforme gradele: ")
            print(get_temp(temp,frm,to))
        elif optiune=="2":
            list=citire()
            print(get_cmmmc(list))
        elif optiune=="3":
            t=int(input("Dati numar: "))
            print(get_largest_prime_below(t))
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Rincearca")



if __name__ == '__main__':
    main()


