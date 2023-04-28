"""
Dette programmet regner ut billettprisen for kjøperne basert på alderen deres. Programmet består av en prosedyre som kalles på.
"""

"""
Her lager jeg en prosedyre som jeg kaller billett. Den inneholder to variabler, alder og billettpris. Alder får verdien som
brukeren skriver inn, og dette blir til en tallverdi med int. Billettprisen er inntil videre 0 kr.
"""

"""
Så kjører jeg en if-test som sjekker alderen. Hvis alderen er mindre eller lik 17, blir billettprisen 30 kr, barnebillett.
Eller hvis alderen er over 17 og under 63 blir billettprisen 50 kr. Eller hvis billettprisen er større enn eller lik 63 blir
billettprisen 35 kroner, seniorbillett. Jeg la til en else test, selv om ikke oppgaven spør om dette, for da får brukren vite
om det de skrev inn ikke er gyldig. På slutten printer jeg ut en setning til kjøper som forteller billettprisen og grunnlaget.
"""
def billett():
    alder = int(input("Skriv inn alderen på kjøperen her"))
    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder > 17 and alder < 63:
        billettpris = 50
    elif alder >= 63:
        billettpris = 35
    else:
        print("Du er ikke innenfor godkjent alder")

    print("Du er", alder, "år, og biletten din koster derfor", billettpris, "kr.")

billett()

"""
Her kaller jeg på prosedyren billett
"""

"""
Prosedyren funker når jeg skriver inn alderne, 15, 31 og 63, som oppgaven spør om. Jeg tror derfor den skal være riktig.
"""
