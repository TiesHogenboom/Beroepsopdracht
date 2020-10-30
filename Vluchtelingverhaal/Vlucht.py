import time
import os

def deel1():
    print(""" Toen ik 28 jaar oud was, moest ik van mijn land Syrië vluchten.
            Het was niet meer veilig in mijn land.
        Na een vreedzame burgeropstand in 2011 tegen het regiem van president
        al Assad ontstond een burger oorlog in Syrië.
        Sinds dien zijn er 100 duizenden mensen omgekomen, zijn delen van het land verwoest,
        en vochten er in Syrië verschillende groeperingen tegen elkaar. Miljoenen mensen zijn het land ontvlucht. 
        De situatie was zo erg in Damascus. Ze dreigde om mij op te pakken.
        Ze hebben mij een paar keer gedreigd om te doden, maar gelukkig waren het alleen maar dreigingen.
        Ik was enig kind maar toch wouden ze dat ik voor de militaire dienst zou werken,
        en daarom zou ik opgepakt worden.
        Mijn vader zei tegen mij dat de enigste optie was dat ik naar een ander beter land ging vluchten.

        Ga je gelijk weg of wacht je nog even?""")
    answer = input("A. Gelijk weg \nB. Even wachten \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel2()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel13()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel1()
#------------------------------------------------------------------------------#
def deel2():
    print("""  In 2 weken moest ik alles voorbereiden om weg te gaan.
            Ik moest een ticket boeken, en tegen sommige vrienden gedag zeggen.
            Ik vloog naar een Syrische stad en toen moest ik mijn weg vinden naar Damascus,
            een plek bekend voor de Syriërs die daar zijn gekomen om een weg te vinden naar een veilig land (Europa). 

            Ga je zelf verder naar de grens of zoek je iemand waarmee je samen kan vluchten?""")
    answer = input("A.Zelf verder \nB. Samen \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel3()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel19()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel2()
#--------------------------------------------------------------------------------#
def deel3():
    print("""  Van Damascus tot de grens moest ik 5 keer gecheckt worden door de douane.
            Onderweg zie je veel mensen die smokkelen, en toen moest ik de risico nemen om met een van hun mee te gaan.
            Toen heb ik iemand gevonden en hem betaald.
            S‘ avonds zei hij tegen mij dat we weg gingen.
            Eerst met de auto voor ongeveer 10 uur naar het strand en toen met een klein bootje naar Griekenland. .

            Er zijn heel veel mensen op 1 boot en het ziet er krap uit. Ga je mee?""")
    answer = input("A.Mee \nB. Andere manier \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel4()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel13()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel3()
#------------------------------------------------------------------------------#
def deel4():
    print(""" Om 9 uur was ik aangekomen en toen heb ik mijn familie gebeld omdat die niet wisten
            dat ik gelijk door naar Griekenland ging.
            Bij Griekenland kwam er een groot boot naar ons toe en die heeft ons geholpen naar om veilig
            aan te komen op hun boot terwijl ze die van ons sloopte.
            In Griekenland moest ik mij daar inschrijven en toen kreeg ik een papiertje en toen kon ik naar Athene gaan.

            Wacht je eerst even om uit te rusten of ga je gelijk verder?""")
    answer = input("A.Rusten \nB. Verder \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel18()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel5()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel4()
#------------------------------------------------------------------------------#
def deel5():
    print("""  Ik kwam daar om 12 uur s’ nachts aan en toen heb ik gelijk een taxi genomen naar de grens van Griekenland.
            Daar zag ik politie dus was ik bang, """)
    time.sleep(2)
    os.system('cls')
    deel6()
#------------------------------------------------------------------------------#
def deel6():
    print(""" Ze waren aardig tegen mij. Ik moest lang lopen en ook met de trein en na een tijdje kwam ik bij Hongarije.
            Daar  was er een man die mij verder naar Budapest heeft genomen.
            Daar was het laat, donker en koud.

            Ga je gelijk verder naar het treinstation of vraag je aan mensen om hulp?""")
    answer = input("A.Hulp \nB. Verder \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel19()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel7()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel6()
#------------------------------------------------------------------------------#
def deel7():
    print("""Toen ben ik naar het treinstation gegaan en zag ik dat er veel organisaties voor vluchtelingen waren,
            dus kon ik wat eten en veilig slapen. 

           Blijf je in Budapest of ga je door naar Amsterdam?""")
    answer = input("A. Amsterdam \nB. Budapest \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel22()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel8()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel7()
#------------------------------------------------------------------------------#
def deel8():
    print("""  De volgende dag heb ik de trein genomen naar Amsterdam, en kwam ik aan op zaterdag 11 uur s’ avonds. Ik had een rugzak mee met veel herinneringen van mijn familie. Ik was op zoek naar een politie station voor hulp. Toen zei iemand tegen mij dat ik naar de politie station moest gaan omdat daar immigratie politie is.
            Na een nachtje slapen in het treinstation ben ik de volgende ochtend naar de immigratie politie gegaan.
            Toen ben ik ingeschreven in het Nederlandse systeem.
            Ik was tevreden en erg blij dat ik veilig was aangekomen, en dat er iemand voor mij was (de overheid.)
            Ik ben erg dankbaar aan Nederland.""")
            
    answer = input("A. Terug naar begin \nB. Stoppen met het verhaal \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel1()
    elif answer == "B" or answer == "b":
        print("Bedankt voor het spelen!")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel8()
#------------------------------------------------------------------------------#
def deel9():
    print("""  In de stad kwam ik Amar tegen. Amar kwam uit een grote familie, waarvan er veel aan het vluchten waren.
                Amar stelde voor dat we gelijk weg gingen van Damascus naar een stad die daar dichtbij zat.
                Daar konden we met een contact praten die ons naar de kust van Libanon kon brengen, en dan een boot naar Griekenland kon regelen.

                Kies je om met Amar mee te gaan of ga je toch zelf?""")
    answer = input("A.Mee \nB. Zelf \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel11()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel10()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel9()
#------------------------------------------------------------------------------#
def deel0():
    print("""  Voordat ik het wist was Amar al weg, en ging ik zelf ook richting de grens""")
    time.sleep(10)
    os.system('cls')
    deel3()
#------------------------------------------------------------------------------#
def deel11():
    print("""  We kwamen erg vroeg in de ochtend aan bij de contact van Amar. Ik heb niet met hem gesproken, alleen Amar zei wat tegen hem.
                Een paar uur later moest ik al weer verder gaan mee in de auto. Langs de douane en toen na een lange rit kwamen we aan bij de kust.
                Ik weet nog dat het erg donker was, en dat er een grote groep mensen al op de boot zaten. Te veel mensen. Ik en Amar moesten mee op de boot.
                Ik vroeg aan mijzelf of het wel veilig was om op zo een drukke boot mee te gaan. Amar zei tegen mij dat ik gewoon samen met hem de boot op moest.

               Volg je Amar de boot op of zoek je toch zelf?""")
    answer = input("A. Volg Amar \nB. Zelf \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel12()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel13()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel1()
#------------------------------------------------------------------------------#
def deel12():
    print("""De boottocht was zwaar, soms kon ik niet slapen door al het geluid wat iedereen maakte en soms was het doodstil.
            Na 9 uur waren we nog steeds niet dichtbij, het ging niet goed op de boot. De eerste persoon verdronk halverwege de rit.
            De boot stopte niet omdat er te weinig ruimte was. Het laatste wat ik mij herinner is dat ik in het water lag, de boot zag ik wegvaren in de verte en ik verloor mijn hoop.
            Ik ben terug op land gehaald door een vissers boot, en kwam aan in Turkije. Door de trauma kon ik niet meer verder in mijn reis.""")
            
    answer = input("A. Terug naar begin \nB. Stoppen met het verhaal \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel1()
    elif answer == "B" or answer == "b":
        print("Bedankt voor het spelen!")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel12()
#------------------------------------------------------------------------------#
def deel13():
    print("""Ik heb een tijdje gezocht voor een betere optie in mijn eentje.
            Ik heb na 4 dagen iemand gevonden die nog ruimte had om mij op zijn boot mee te nemen.
            Ik heb gelijk ja gezegd en al snel was ik op weg naar Griekenland""")
    time.sleep(10)
    os.system('cls')
    deel3()
#------------------------------------------------------------------------------#
def deel14():
    print("""  Elke dag werd het erger en erger. Er waren veel protesten waar rebellen en Syrische veiligheidsdiensten elkaar doden.
            Elke dag werd ik banger voor mijn toekomst en of ik het wel zou overleven.
            Ik kreeg ook steeds meer dreigingen om bij het militaire dienst te komen.

              Blijf je nog langer wachten of ga je toch vluchten?""")
    answer = input("A. Wacht \nB. Vlucht \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel15()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel17()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel4()
#------------------------------------------------------------------------------#
def deel5():
    print("""Het einde van 2011 was niet beter dan de vorige maanden,
            normaal is het leuk als we het eind van de jaar vieren maar het land was vol met protesten dus zat niemand het nieuwe jaar te vieren.
            Heel veel vrienden zijn gevlucht naar andere landen om een betere toekomst te zorgen. Ik heb heel veel negatieve emoties,
            mijn familie ging ook nog uit elkaar. Ik begreep niet waarom ik zo lang had zitten te wachten.
            We hebben besloten om richting de hoofdstad te gaan omdat het bij ons te onveilig was.""")
    time.sleep(10)
    os.system('cls')
    deel7()
#------------------------------------------------------------------------------#
def deel16():
    print("""  Het einde van 2011 was niet beter dan de vorige maanden,
            normaal is het leuk als we het eind van de jaar vieren maar het land was vol met protesten dus zat niemand het nieuwe jaar te vieren.
            Ik heb besloten om te vluchten en alles achter te laten. Ik moest een ticket boeken, en tegen sommige vrienden gedag zeggen.
            Ik vloog naar een Syrische stad en toen moest ik mijn weg vinden naar Damascus,
            een plek bekend voor de Syriërs die daar zijn gekomen om een weg te vinden naar een veilig land. Net voor ik daar aan kwam was er een grote knal.
            Een bombardement in Damascus. 

            Ga je door naar domascus of neem je een andere route?""")
    answer = input("A. Door \nB. Andere route \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel3()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel17()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel16()
#------------------------------------------------------------------------------#
def deel17():
    print("""Damascus was niet veilig. Er was al een bombardement en er konden er nog meer afgaan.
            Ik heb besloten om naar Douma te gaan, een stad naast Damascus. In Douma ben ik naar een smokkelaar gegaan die mij samen met een andere groep naar Turkije kon brengen.
            Ik wou niet graag naar Griekenland maar ik wou zo snel mogelijk het land uit dus ging ik mee.
            Toen we eenmaal in Griekenland aankwamen werden we al snel doorgestuurd naar kamp Moria.
            Toen we aankwamen waren we erg blij om eindelijk vrijheid te hebben.
            Maar al snel hadden we het door dat het daar niet zo geweldig was. Het kan nog een jaar duren voordat ik uit dit kamp mag. Het leven is niet fijn, maar het is beter dan niks.
""")
            
    answer = input("A. Terug naar begin \nB. Stoppen met het verhaal \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel1()
    elif answer == "B" or answer == "b":
        print("Bedankt voor het spelen!")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel17()
#------------------------------------------------------------------------------#
def deel18():
    print("""Als ik in Griekenland wou blijven had ik naar een kamp moeten gaan. Ik heb toch nog Griekenland verlaten voordat dit moest.
            In de krant las ik dat het erg slecht was in die kampen. Ik wou graag verder Europa in,
            waar ik een beter leven kon hebben en een nieuwe toekomst zou kunnen beginnen. Ik ging eerst verder naar de Athene. """)
    time.sleep(2)
    os.system('cls')
    deel5()
#------------------------------------------------------------------------------#
def deel19():
    print("""Hongarije overspoelde aan vluchtelingen, het was overal wel een chaos.
            Ik zocht voor meer informatie en toen kwam ik een groep tegen die in dezelfde situatie als mij zaten, 2 andere vluchtelingen uit Syrië.
            Het voelde goed om weer met iemand te praten en deels normaal te leven voor een paar dagen. Er was een trein naar die naar Oostenrijk ging.
            We wisten niet zeker of we de trein moesten nemen omdat er in het nieuws gesproken werd van treinen die stopte bij vluchtelingen kampen. 

            Neem je de trein naar Oostenrijk of zoek je een andere manier?""")
    answer = input("A. Trein \nB. Andere manier \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel20()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel21()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel19()
#------------------------------------------------------------------------------#
def deel20():
    print("""We namen de trein naar Oostenrijk en kwamen aan in Wenen vroeg in de ochtend.
            Na wat door te vragen werden we naar een plaats gestuurd wat aan het zuiden van wenen lag,
            genaamd Traiskirchen.
            Hier kwamen we in contact met Oasis. Zij hielpen ons om weer een nieuw leven te beginnen en zij gaven ons hoop om weer een toekomst te zoeken.
""")
            
    answer = input("A. Terug naar begin \nB. Stoppen met het verhaal \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel1()
    elif answer == "B" or answer == "b":
        print("Bedankt voor het spelen!")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel20()
#------------------------------------------------------------------------------#
def deel21():
    print("""Op straat leven was zwaar en niet iets waarvoor ik zocht.
            Na een paar nachten werden we midden in de nacht opgepakt door de politie.
        We moesten naar het bureau daar. Het was of de trein nemen naar Oostenrijk,
            of naar een vluchteling kamp in Hongarije. We hadden besloten om toch de trein te nemen""")
    time.sleep(10)
    os.system('cls')
    deel20()
#------------------------------------------------------------------------------#
def deel22():
    print("""Hongarije overspoelde aan vluchtelingen, het was overal wel een chaos.
            Ik zocht voor meer informatie en toen kwam ik een groep tegen die in dezelfde situatie als mij zaten, 2 andere vluchtelingen uit Syrië.
            Het voelde goed om weer met iemand te praten en deels normaal te leven voor een paar dagen. Er was een trein naar die naar Oostenrijk ging.
            We wisten niet zeker of we de trein moesten nemen omdat er in het nieuws gesproken werd van treinen die stopte bij vluchtelingen kampen. 

            Wacht je nog wat langer in budapest of zoek je voor een andere weg om verder europa in te gaan?""")
    answer = input("A. Wacht \nB. Andereweg \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel24()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel23()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel1()
#------------------------------------------------------------------------------#
def deel23():
    print("""Het leven in Budapest was erg moeilijk,
            en de enigste optie die ik nog zag was het zoeken van een vluchteling kamp,
            en hopen dat ik zo nog mijn toekomst kon redden. Er werd tegen mij gezegd dat het te druk was in Hongarije en dat ik werd weg gestuurd naar Griekenland.
            Na een hele lange reis werd ik gestuurd naar kamp Moria. Het was hier erg moeilijk om te leven, en het was er veel te druk.
            Ik zit nu nog steeds vast en ik mag er hopelijk volgend jaar uit om een betere toekomst te zoeken.
""")
            
    answer = input("A. Terug naar begin \nB. Stoppen met het verhaal \n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel1()
    elif answer == "B" or answer == "b":
        print("Bedankt voor het spelen!")
        time.sleep(2)
        os.system('cls')
        exit()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel23()
#------------------------------------------------------------------------------#
def deel24():
    print("""Ik heb een tijdje gezocht voor de beste optie, en toen had ik besloten om naar Nederland te gaan.
    Ik hoorde op het nieuws dat het nog steeds erg slecht was in Syrië en dat er steeds meer vluchtelingen kwamen naar Europa.
    Ik moest nog even wachten op de trein naar Nederland""")
    time.sleep(10)
    os.system('cls')
    deel8()
    
os.system('cls')
deel1()
