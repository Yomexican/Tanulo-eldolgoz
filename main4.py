#0
print("Tanulok kezelése.")

#1
tanulok = []

while True:
    print("\nKérem a tanukó adatait:")
    tanulo={}
    tanulo["nev"]=input("Tanulo neve: ")
    tanulo["szid"]=input("Születési idő: ")
    tanulo["magassag"]= int(input("Magassag: "))

    tanulo = (nev, szid, magassag)
    tanulok.append(tanulo)

    valasz = input("További tanuló (igen/nem): ")
    if valasz.lower() !="igen":
        break

#3feldolgozás listaelem indexe segítségével
i=0
while i<len(tanulok):
    print(f'{i+1}. - Tanuló neve: {tanulok[i]["nev"]}, születési ideje:{tanulok[i]["szid"]}, magasság:{tanulok[i]["magassag"]}')
   
    i+=1