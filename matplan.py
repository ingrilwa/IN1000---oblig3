"""
Dette programmet skal kjøre ut matplanen, bestående av tre måltider per dag, til en gitt beboer. Dette gjøres med en ordbok og en prosedyre. Først lager jeg en ordbok bestående av nøkler og verdier som lister inni ordboka.
"""

maltider = {"Kari Larsen":["havregrøt", "suppe", "lapskaus"], "Trine Skogli":["brød", "egg", "pølser"], "Marit Lund":["knekkebrød", "grøt", "viltgryte"]}

"""
Her definerer jeg en prosedyre med navn matplan og skriver først ut alle nøklene, altså navnet på beboerne, som en liste. Så spør jeg om brukeren kan skrive inn en av beboerne sitt navn. Deretter kjører jeg en if-test som printer ut matplanen til den beboeren brukeren skrev inn som input. Jeg har også med en else som printes hvis brukeren skriver noe annet enn beboerne sine navn. Til slutt kaller jeg på prosedyren.
"""

def matplan():
    print(list(maltider))
    navn = input("Skriv inn et av brukerne sitt navn her")


    if navn == "Kari Larsen":
        print("Matplanen til denne beboeren er", maltider["Kari Larsen"])
    elif navn == "Trine Skogli":
        print("Matplanen til denne beboeren er", maltider["Trine Skogli"])
    elif navn == "Marit Lund":
        print("Matplanen til denne beboeren er", maltider["Marit Lund"])
    else:
        print("Navnet du har skrevet inn er ikke en beboer")

matplan()

"""
Svar på oppgave 3:
a) Hvis man kun skulle skrevet ut brukernavnene på alle IN1000-studentene, ville jeg valgt en liste eller en
mengde. Det er nok ikke noen grunn for å ha brukernavnene i riktig rekkefølge, så mengde ville kanskje vært
mest hensiktismessig og greit.

b) For å skrive ut alle brukernavn og tilhørende antall poeng, ville jeg absolutt brukt en ordbok. Man kan
slå opp i den, finne det man trenger, og den er ryddig og oversiktlig.

c) Navn på alle vinnere i Lotto det siste året, kunne man organisert i mengder eller lister. Kanskje lister
hadde vært mest hensiktismessig her, slik at man fyller på på slutten av lista når det kommer en ny vinner
og at de står oppført i en viss rekkefølge.

d) Man kunne samlet all mat noen er allergisk mot i en mengde. Det trengs ikke noen viss rekkefølge, men da
slipper man at det står "gluten" 3 forskjellige ganger for eksempel. Hvis man hadde valgt en liste, hadde alt
blitt skrevet ut, uten å tenke på eventuelle duplikasjoner.
"""
