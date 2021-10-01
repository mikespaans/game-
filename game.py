StartGame = input("type iets om de game te starten ")
print ("     ")
print ("Je bent verdwaald in een onbekend bos.")
print ("In dit bos lopen gevaarlijke beesten.")
print ("Om deze beesten te kunnen verslaan moet je wapens en levens zien te krijgen.")
print ("Je begint met 50 health en geen wapens")
print ("Om meer health te krijgen kan je appels vinden en opeten")
print ("        ")
GoedeAppel = 20
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
        TotalHealth = 60
    elif Health >= "70" and ZakMes == "niet gekregen":
        print ("De wolf heeft je aan gevallen en heeft je 2 keer gebeten voordat hij wegrende.")
        print ("Je totale Health 50.")
        TotalHealth = 50
    elif Health <= "50" and ZakMes == "gekregen":
        print ("De wolf heeft je 1 keer gebeten voordat je hem met je zakmes stak.")
        print ("Je totale health 40")
        TotalHealth = 40
    elif Health <= "50" and ZakMes == "niet gekregen":
        print ("De wolf heeft je 2 keer gebeten voordat hij wegrende.")
        print ("Je totale health 30.")
        TotalHealth = 30
    print ("    ")
    print ("Je loopt verder")
    AppelEtenKeuze = input("Je ziet weer een appel liggen eet je hem op ja of nee? ")
    if AppelEtenKeuze == ("ja"):
        print ("Je hebt de appel opgegeten.")
        print ("je totale health is: ")
        print (TotalHealth + GoedeAppel)
        NewHealth = TotalHealth + GoedeAppel
    else:
        print ("Je hebt de appel niet opgegeten.")
    print ("    ")
    print ("je ziet iets liggen in het gras.")
    WapenKeuze = input("Ga je erheen ja of nee? ")
    if WapenKeuze == "ja":
        print ("Je loopt er heen.")
        print ("Het is een pistool.")
        print ("Het pistool neem je mee")
    else: 
        print ("je gaat er niet heen")
    print ("Je loopt verder.")
    print ("Je ziet de uitgang van het bos.")
    print ("Maar plotseling komt er een beer")
    KeuzeBeer = input("wat doe je naar de uitgang rennen of tegen de beer vechten? ")
    if KeuzeBeer == "tegen de beer vechten":
        if NewHealth >= 70 and WapenKeuze == "ja":
            print ("    ")
            print ("je hebt de beer neergeschoten en verlaat het bos")
        else:
            print ("Helaas de beer was te sterk en heeft je gedood.")
    else:
        print ("    ")
        print ("Helaas de beer kwam achter je aan en was sneller dan jij.")
        print ("Je hebt het niet overleefd")
else:
    print ("Je gaat het rechter pad in.")
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
    print ("Je ziet een huis.")
    HuisKeuze = input("Ga je het huis in ja of nee? ")
    if HuisKeuze == "ja":
        ZakMes = 'gekregen'
        print ("Je gaat het huis in.")
        print ("Plotseling word je door een hond gebeten in het huis vervolgens rent deze weg.")
        print ("je nieuwe totale health is:")
        print (Health - 10)
        print ("Je loopt verder door het huis en vind een zakmes")
        print ("Je gaat weer naar buiten.")
    else:
        ZakMes = 'niet gekregen'
        print ("Je gaat niet het huis in.")
    print ("    ")
    print ("Je loopt verder. ")
    print ("Je ziet een tasje in een boom hangen.")
    BoomKeuze = input("wat doe je erheen gaan ja of nee? ")
    if BoomKeuze == ("ja"):
        if ZakMes == "gekregen":
            Pistool = 'gekregen'
            print ("Je hebt het tasje los kunnen snijden.")
            print ("Er zit een pistool in.")
            print ("Je hebt nu een pistool.")
        else:
            print ("je bent bij het tasje gekomen maar je kan hem niet pakken.")
            print ("Hij zit vast met een touw en je krijgt hem niet los.")
    else:
        print ("    ")
        print (" Je loopt verder.")

    print ("Je ziet de uitgang van het bos.")
    print ("Maar plotseling verschijnt er een leeuw.")
    LeeuwKeuze = input("Wat doe je naar de uitgang rennen of tegen de leeuw vechten. ")
    if LeeuwKeuze == ("tegen de leeuw vechten"):
        if str(Health) >= "60" and Pistool == "gekregen":
            print ("Je hebt de leeuw neergeschoten en verlaat het bos.")
            print ("Je hebt het overleefd.")
        else:
            print ("Helaas de leeuw was sterker dan jij.")
            print ("Je hebt het niet overleefd.")

    else:
        if str(Health) >= "70":
            print ("Je bent snel genoeg het bos uitgerend en de leeuw volgt je niet.")
            print ("je hebt het overleefd.")
        else:
            print ("Je probeerde het bos uit te rennen.")
            print ("Maar helaas was de leeuw sneller dan jij")
            print ("Je hebt het niet overleefd.")




    


