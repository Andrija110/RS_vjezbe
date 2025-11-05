def count_vowels_consonants (tekst):
    vowels  = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    broj_samoglasnika = 0
    broj_suglasnika = 0

    
    for slovo in tekst:
        if slovo.isalpha():
            if slovo in vowels:
                broj_samoglasnika += 1
            elif slovo in consonants:
                broj_suglasnika += 1

    return {"Samoglasnici": broj_samoglasnika, "Suglasnici": broj_suglasnika}


Tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(Tekst))