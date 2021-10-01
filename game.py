StartGame = input("type iets om de game te starten ")
print ("     ")
print ("Je bent verdwaald in een onbekend bos.")
print ("In dit bos lopen gevaarlijke beesten.")
print ("Om deze beesten te kunnen verslaan moet je wapens en levens zien te krijgen.")
print ("Je begint met 50 health en geen wapens")
print ("Om meer health te krijgen kan je appels vinden en opeten")
print ("Maar pas op want als je een verkeerde appel eet dan gaat er health af")
print ("        ")
EerstePadKiezen = input("je komt op een splitsing van 2 paden welke kant ga je op links of rechts? ")
if EerstePadKiezen == "links":
    print ("Je bent het linker pad ingegaan.")
    print ("        ")
    AppelEten = input("Je ziet een appel onder een boom liggen, ga je hem opeten ja of nee? ")
    if AppelEten == "ja":
        Health = str(70)
        print ("Je hebt de appel gegeten je hebt nu 20 health erbij gekregen")
        print ("Totale health 70")
    else:
        Health = str(50)
        print ("Je hebt de appel niet gegeten je health blijft 50")
    print ("    ")
    print ("Je loopt verder")
    KleinHutje = input("Je ziet een klein hutje kijk erin of loop verder? ")
    if KleinHutje == "kijk erin":
        ZakMes = 'gekregen'
        print ("Je gaat naar binnen. ")
        print ("Je bent binnen en ziet een klein zakmes liggen deze neem je mee.")
        print ("Je gaat weer naar buiten")
        print ("    ")
        print ("Je loopt verder ")
    else:
        ZakMes = 'niet gekregen'
        print ("    ")
        print ("Je gaat niet naar binnen en loopt verder ")
    print ("        ")
    print ("Je ziet een wolf en hij valt je aan.")
    if Health >= "70" and ZakMes == "gekregen":
        print ("De wolf heeft je 1 keer gebeten voordat je hem met je zakmes stak.")
        print ("Je totale health is met 10 afgenomen.")
        print ("Totale health 60.")
    elif Health >= "70" and ZakMes == "niet gekregen":
        print ("De wolf heeft je aan gevallen en heeft je 2 keer gebeten voordat hij wegrende.")
        print ("Je totale Health 50.")
    
        

    