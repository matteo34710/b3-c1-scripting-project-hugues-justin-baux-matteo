import csv
print("Tri commencé!")

#ouverture du fichier qui doit être trié
file = open('conso-annuelles_v1.csv', 'r')
csvFile = csv.reader(file, delimiter=';')
