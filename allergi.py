"""
I denne oppgaven skal du lage et system som spør om brukerinput der de kan fylle inn allergiene sine.
Dette skal legges inn i en egnet type samling og innholdet i samlingen, altså hvilken mat som bør unngås,
skal til slutt printes ut.
"""

print("Du skal svare på hvilke allergier du har i dette programmet.")

"""
Under definerer jeg en tom liste som skal inneholde alle allergier. Videre danner jeg en prosedyre som jeg
kaller allergisjekk. Her kjører jeg ut input til brukeren og kjører en rekke if-tester som sjekker svarene
og legger til varene de svarer de er allergiske mot. Dette legges inn i lista jeg først definerte, via append()
"""
allergier = []

def allergisjekk():
    svar = input("Har du noen allergier?")
    if svar == "ja":
        svar = input("Har du glutenallergi?")
        if svar == "ja":
            allergier.append("gluten")
        svar = input("Har du laktoseintoleranse?")
        if svar == "ja":
            allergier.append("lakose")
        svar = input("Er du allergisk mot nøtter?")
        if svar == "ja":
            allergier.append("nøtter")
        svar = input("Spiser du kjøtt?")
        if svar == "nei":
            allergier.append("kjøtt")
        svar = input("Er det noe annet du ikke tåler? (svar ja eller nei)")
        if svar == "ja":
            svar = input("Hva annet er det du ikke tåler?")
            allergier.append(svar)

    else:
        print("Den er grei")

    print("Den fullstendige listen over allergier er:", allergier)

allergisjekk()

"""
Jeg legger også til en else på den første if-testen slik at hvis brukeren ikke har noen allergier, skal
de slippe å svare på alle de andre spørsmålene. Til slutt printer jeg ut den fullstendige listen med allergiene
brukeren har lagt til. Alt dette ligger inne i en prosedyre. Denne kaller jeg på på slutten. 
"""
