def decoreer(tekst=""):
    lengte=len(tekst)+4
    print()
    print(lengte* "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    bedrag_pp=bedrag/personen
    return f"Het gemiddelde bedrag is {bedrag_pp} euro."

def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    aantal=len(tekst)
    streep=(aantal*"=")
    uit.append(streep)
    return uit

# vraag 10.3
def som(invoer={}):
    totaal=0
    for i in invoer.values():
        totaal+=i
    return totaal



