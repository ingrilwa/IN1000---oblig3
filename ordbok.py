"""
Dette programmet inneholder en ordbok som holder på matvarer og deres tilhørende pris i butikk. Programmet utvides med å ta
inn brukerinput med to nye nøkler og verdier som legges til i ordboka. Til slutt printer vi ut den fullstendige ordboka
"""

"""
Først lager jeg en variabel som blir ordboka mi, kalt matvarer. Deretter legger jeg inn nøkler og verdier og skriver dette ut
"""
matvarer = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(matvarer)

"""
Her lager jeg en ny variabel med de nye matvarene og spør om brukeren kan legge til matvare og tilhørende pris med et kolon
i mellom. Altså nøkkel : verdi. Så lager jeg en ny variabel mat, der jeg splitter forrige variabel i to rundt kolonet, slik
at nøkkel og verdi splittes. I neste linje legger jeg disse to verdiene inn i ordboka matvarer som nøkkel:verdi, og gjør
samtidig verdien om til et flyttall slik at man kan skrive inn desimaler.
"""

nye_matvarer = input('Skriv inn en matvare og tilhørende pris med ":" mellom')
mat = nye_matvarer.split(":")
matvarer[mat[0]] = float(mat[1])

nye_matvarer = input('Skriv inn en matvare og tilhørende pris med ":" mellom')
mat = nye_matvarer.split(":")
matvarer[mat[0]] = float(mat[1])

print(matvarer)
