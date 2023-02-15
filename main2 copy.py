#0
print("Tanulok kezelése.")

#1
tanulok = []

while True:
    print("\nKérem a tanukó adatait:")
    nev=input("Tanulo neve")
    szid=input("Születési idő: ")
    magassag= int(input("Magassag: "))

    tanulo = (nev, szid, magassag)
    tanulok.append(tanulo)

    valasz = input("További tanuló (igen/nem): ")
    if valasz.lower() !="igen":
        break

#3feldolgozás listaelem indexe segítségével
i=0
while i<len(tanulok):
    print(f"Tanuló neve: {tanulok[i][0]}, születési ideje:{tanulok[i][1]}, magasság:{tanulok[i][2]}")
   
    i+=1