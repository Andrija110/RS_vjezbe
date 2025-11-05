def brojanje_riječi(tekst):
    Rijeci = tekst.lower().split()
    Rjecnik = {}

    for Rijec in Rijeci:
        if Rijec in Rjecnik:
            Rjecnik[Rijec] += 1
        else:
            Rjecnik[Rijec] = 1
    return Rjecnik


Tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(Tekst))