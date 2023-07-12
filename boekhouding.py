#vraag 10.4
from helper import *
#vraag 10.9
from presentatie import *
#vraag 10.11
import csv

#vraag 10.2
inkomsten={"Aardbeien-ijs-totaal":1000,"Vanille-ijs-totaal":2000,"Chocolade-ijs-totaal":1500,"Waterijsjes-totaal":750}

#vraag 10.5
totaal_inkomsten=som(inkomsten)

# vraag 10.10
presenteer(inkomsten,totaal_inkomsten)

#vraag 10.12
with open('boekhouding.csv', 'w',newline='') as csvfile:
     for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])


     