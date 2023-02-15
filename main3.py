#0
print("Tanulok kezelése.")

#1
tanulok = []

while True:
    print("\nKérem a tanukó adatait:")
    tanulo= {}
    tanulo["nev"]=input("Tanulo neve")
    tanulo["szid"]=input("Születési idő: ")
    tanulo["magassag"]= int(input("Magassag: "))

    tanulok.append(tanulo)

    valasz = input("További tanuló (igen/nem): ")
    if valasz.lower() !="igen":
        break

#3feldolgozás lista alias elem (item) segítségével
for item in tanulok:
    #!!!!! figyeljünk arra hogy az f string és a kulcsoknak a határolóinak különböző legyen
    print(f'Tanuló neve: {item["nev"]}, születési ideje:{item["szid"]}, magasság:{item["magassag"]}')
