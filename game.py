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
        Health = 70
        print ("Je hebt de appel gegeten je hebt nu 20 health erbij gekregen")
        print ("Totale health 70")
    else:
        Health = 50
        print ("Je hebt de appel niet gegeten je health blijft 50")
    print ("    ")
    print ("Je loopt verder")
    KleinHutje = input("Je ziet een klein hutje kijk erin of loop verder? ")
    if KleinHutje == "kijk erin":
        print ("Je gaat naar binnen. ")
        print ("Je bent binnen en ziet een klein zakmes liggen deze neem je mee.")
        print ("Je gaat weer naar buiten")
        print ("    ")
        print ("Je loopt verder ")
    else:
        print ("    ")
        print ("Je gaat niet naar binnen en loopt verder ")
    print ("        ")
    print ("Je ziet een wolf en hij valt je aan.")

    