prijzen={"aardbei":"3","vanille":"4","chocolade":"5"}
aanbieding=prijzen["vanille"]=4*.8
reclame_tekst="vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € "
reclame_tekst3=(f"{reclame_tekst}{aanbieding}0").swapcase()
reclame_tekst4=reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el)<5:
        print(el.lower())
    else:
        print(el.upper())
