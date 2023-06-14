from algemene_functies import mijn_functie_2



# vraag 5

def aanbieding_1(smaak,prijs,korting):

    korting_prijs=prijs*(1-korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs}0 euro.")

aanbieding_1("aardbei",4,.1)   

#vraag 6 en 7

def inkomsten_totaal(inkomsten,btw_tarief):
    totaal=sum(inkomsten)
    btw=btw_tarief*totaal
    inkomsten_tekst=f"Het totaal van alle inkomsten van deze week is {totaal} euro (excl.btw), waarover {btw} euro Btw betaald dient te worden."
    return inkomsten_tekst

omzet=[220,430,125,160,205,90,345]

print(inkomsten_totaal(omzet,.09))


#vraag 8

def laag_en_hoog(mijn_lijst):
    result=[max(mijn_lijst),min(mijn_lijst)]
    return result

print(laag_en_hoog(omzet))


#vraag 9 en 10

def gemiddelde(mijn_lijst):
    aantal=len(mijn_lijst)
    totaal=sum(mijn_lijst)
    gemiddelde=totaal/aantal
    tekst=f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    print(tekst)

gemiddelde(omzet)


#vraag 11

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)



# vraag 12

getallen=(10,5,3,2,1,2,9)

def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    return korte_lijst
    
print(combinatie(getallen))

print(mijn_functie_2(combinatie(getallen)))