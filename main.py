def zadanie1():
    wynik = open("wyniki4_1.txt", "w")

    with open("slowa.txt") as dane:
        for wiersz in dane:
            x = wiersz.strip()
            if x.count("w") == x.count("k"):
                wynik.write(wiersz + "\n")
                print(x)

    wynik.close()
    
def wakacje(x):
    w = x.count('w')
    a = x.count('a') // 2
    k = x.count('k')
    c = x.count('c')
    j = x.count('j')
    e = x.count('e')
    return min(w, a, k, c, j, e)
    

    
def zadanie2():
    wynik2 = open("wyniki4_2.txt", "w")
    
    with open("slowa.txt") as dane:
        for wiersz in dane:
            y = wiersz.strip()
            w = wakacje(y)
            wynik2.write(f"{w}\n")
            # print(w)
            
    wynik2.close()
    

    
def zadanie3():
    
    wynik3 = open("wyniki4_3.txt", "w")
    
    with open("przyklad.txt") as dane:
        for wiersz in dane:
            z = wiersz.strip()
            print(z)
    
    wynik3.close()
    
print(zadanie1())
print(zadanie2())

