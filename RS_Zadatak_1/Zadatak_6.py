#%%

suma_for = 0

for broj in range(2, 101, 2):
    suma_for += broj

print("Suma parnih brojeva od 2 do 100 je:", suma_for)
#%%

suma_while = 0
broj = 2

while broj <= 100:
    suma_while += broj
    broj += 2

print("Suma parnih brojeva od 2 do 100 je:", suma_while)
#%%

neparni_brojevi = []

for i in range (1, 20, 2):
    neparni_brojevi.append(i)

print("\nPrvih 10 neparnih brojeva u obrnutom redoslijedu: ")

for broj in reversed(neparni_brojevi):
    print(broj, end=" ")
#%%

print("\nPrvih 10 neparnih brojeva u obrnutom redoslijedu: ")

brojac = 19
while brojac >= 1:
    print(brojac, end=" ")
    brojac -= 2
#%%

print("\nFibonaccijev niz do 1000 :")
a = 0
b = 1

print(a, end=" ")
for _ in range(1, 20):
    if b > 1000:
        break
    print(b, end=" ")
    sljedeci = a + b
    a = b
    b = sljedeci
#%%

print("\nFibonaccijev niz do 1000 :")
a = 0
b = 1

while a <= 1000:
    print(a, end=" ")
    sljedeci = a + b
    a = b
    b = sljedeci