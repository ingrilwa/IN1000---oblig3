"""
Programmet under lager lister, legger til og fjerner verdier fra listene og skriver alt dette ut. Det tas inn brukerinput som
også legges inn i lister, og vi sjekker om disse faktisk blir med i listene. Vi regner ut sum og produktet av listenes innhold,
konkatenerer lister og printer alt dette ut igjen.
"""

"""
Her lager jeg en liste med hensiktsmessig navn og legger til en ekstra verdi med append(). Vi printer også ut første og tredje
element i lista.
"""
tall_liste = [3,5,7]
tall_liste.append(9)
print(tall_liste[0],tall_liste[2])

"""
Jeg spør om brukerinput og legger navnene inn i en ny liste. Så gjør jeg lista om til en mengde for å sjekke om et bestemt
navn er med i lista, eller nå, mengden. Her kjører vi en if-test
"""
navneliste = input("Oppgi et navn her"), input("Oppgi et navn her"), input("Oppgi et navn her"), input("Oppgi et navn her")

navneliste = set(navneliste)

if "ingrid" in navneliste or "Ingrid" in navneliste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

"""
Jeg regner her ut summen av den første lista. Visste ikke helt hva som var best måte å gjøre dette, men tror dette
var hensiktsmessig. Etterpå sjekker jeg produktet av lista. Det er sikkert en funksjon for dette, men gjorde det ledd for ledd
her, og synes ikke det var for tungvint heller.
"""
Sum = sum(tall_liste)
print(Sum)

produkt = tall_liste[0] * tall_liste[1] * tall_liste[2] * tall_liste[3]
print(produkt)

"""
Her lager jeg enda en ny liste som konkatenerer sum- og produktslista sammen, og printer dette ut. På slutten lager jeg en
liste sammensatt av den helt første tall_liste og den siste ny_liste og printer dette ut.
"""
ny_liste = []
ny_liste.append(Sum)
ny_liste.append(produkt)
print(ny_liste)

full_liste = tall_liste + ny_liste
print(full_liste)

"""
Her "popper", eller fjerner, jeg de to siste elementene i lista ut, slik oppgaven ba om, og printer dette ut på nytt
"""
full_liste.pop()
full_liste.pop()
print(full_liste)
