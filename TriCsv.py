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

