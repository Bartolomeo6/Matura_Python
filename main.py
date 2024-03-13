def zadanie1():
    wynik = open("wyniki4_1.txt", "w")

    with open("slowa.txt") as dane:
        for wiersz in dane:
            x = wiersz.split()
            if x.count("w") == x.count("k"):
                wynik.write(wiersz + "\n")

    wynik.close()

def zadanie2():
    wynik = open("wyniki4_2.txt", "w")

    with open("slowa.txt") as dane:
        for wiersz in dane:
            x = wiersz.split()
            
    wynik.close()

print(zadanie1())
print(zadanie2())
