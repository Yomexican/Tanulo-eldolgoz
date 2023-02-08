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

#3feldolgozás lista alias elem (item) segítségével
for item in tanulok:
    print(f"Tanuló neve: {item[0]}, születési ideje:{item[1]}, magasság:{item[2]}")
