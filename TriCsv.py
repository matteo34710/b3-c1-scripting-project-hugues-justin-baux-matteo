import csv
print("Tri commencé!")

#ouverture du fichier qui doit être trié
file = open('conso-annuelles_v1.csv', 'r')
csvFile = csv.reader(file, delimiter=';')

finalList = []
calculList = []
sortList = []

#Suppression des lignes avec une colonne vide
for line in csvFile:
    if all(line):
        calculList.append(line)

#Suppression de la colonne id logement
for col in calculList:
    del col[1]

#Remplacement des virgules en point pour le calcul
firstline = True
for row in calculList:
    if not firstline:
        row[1] = row[1].replace(',', '.')
        row[2] = row[2].replace(',', '.')
    else:
        firstline = False

#Calcul an1 + an2
firstlineDeux = True
for row in calculList:
    if not firstlineDeux:
        try:
            calc = float(row[1]) + float(row[2])
            row.append(calc)
            sortList.append(row)
        except:
            continue
            break
    else:
        row.append('Année 1 + Année 2')
        finalList.append(row)
        firstlineDeux = False

#Definition pour le tri
def avantDernierCol(col):
    return float(col[4])

def dernierCol(col):
    return col[3]

sortList.sort(key=avantDernierCol, reverse=True)
sortList.sort(key=dernierCol)

#Export des données dans le fichier conso-clean.csv
with open('conso-clean.csv', 'w', newline='') as files:
    writer = csv.writer(files, delimiter=';')
    for line in finalList:
        writer.writerow(line)
        for row in sortList:
            writer.writerow(row)
        break

print('Tri terminée!')