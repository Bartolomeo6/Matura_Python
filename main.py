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
    id = 0
    do_usuniecia = 0
    puste = ""
    slowo = "wakacje"
    dlugosc = len(slowo)
    
    with open("przyklad.txt") as dane:
        for wiersz in dane:
            x = wiersz.strip()
            for litera in x:
                if dlugosc == id:
                    id = 0
                    puste = ""
                if litera == slowo[id]:
                    puste += slowo[id]
                    id+=1
                else:
                    do_usuniecia+=1
            if slowo != puste:
                do_usuniecia+= len(puste)
                if len(x) < 7:
                    do_usuniecia = len(x)

            wynik3.write(str(do_usuniecia) +"\n")
            do_usuniecia = 0
            id = 0
            puste = ""
            
    wynik3.close()
    
print(zadanie1())
print(zadanie2())
print(zadanie3())

