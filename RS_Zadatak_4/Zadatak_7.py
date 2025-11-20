import asyncio, time

async def fetch_data(param):
    # Korutina počinje s radom.
    print(f"Nešto radim s {param}...")
    
    # Korutina predaje kontrolu Event loop-u i čeka 'param' sekundi. 
    # U tom trenutku ulazi u stanje Waiting.
    await asyncio.sleep(param) 
    
    # Nakon isteka 'param' sekundi, vraća se u stanje Ready i ispisuje poruku.
    print(f'Dovršio sam s {param}.')
    
    # Korutina završava i vraća rezultat.
    return f"Rezultat za {param}"

async def main():
    # 1. Kreiramo prvi task. Task 1 se šalje Event loop-u i počinje raditi (traje 1s).
    task1 = asyncio.create_task(fetch_data(1)) 
    
    # 2. Kreiramo drugi task. Task 2 se šalje Event loop-u i počinje raditi (traje 2s).
    # Oba taska (task1 i task2) sada rade konkurentno.
    task2 = asyncio.create_task(fetch_data(2)) 
    
    # 3. Čekamo (await) samo task1.
    # Event loop čeka 1 sekundu dok task1 ne završi. Za to vrijeme task2 radi u pozadini.
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    
    # U ovom trenutku (T=1s):
    # - task1 je završen.
    # - task2 je radio 1 sekundu i treba mu još 1 sekunda da završi.
    
    # 4. KLJUČNI KORAK: Umjesto da await-amo task2 (što bi nam dalo rezultat),
    # dodajemo umjetno kašnjenje u main korutini koje je duže od preostalog vremena
    # potrebnom task2 da završi (2s - 1s = 1s).
    print("Main korutina ide na kratki spavanac da task2 završi...")
    await asyncio.sleep(1.5) 
    
    # U ovom trenutku (T=1s + 1.5s = 2.5s), Event loop je imao dovoljno vremena 
    # (ukupno 2 sekunde) da task2 ispiše "Dovršio sam s 2." i završi.
    print("Main korutina se probudila.")
    
    # 5. Budući da nismo await-ali task2, ne možemo dobiti njegov rezultat, ali 
    # se ispis iz korutine dogodio jer se ona stigne izvršiti dok main čeka.
    
    return [result1]

# --- Pokretanje programa ---
t1 = time.perf_counter()
# asyncio.run() pokreće Event loop i izvršava main(). 
# Event loop se neće ugasiti dok se main() ne završi.
results = asyncio.run(main()) 
t2 = time.perf_counter()

print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

# Očekivani ispis:
# Nešto radim s 1...
# Nešto radim s 2...
# Dovršio sam s 1.   <--- Nakon 1 sekunde
# Fetch 1 uspješno završen.
# Main korutina ide na kratki spavanac da task2 završi...
# Dovršio sam s 2.   <--- Unutar 1.5 sekundi, task2 se završi
# Main korutina se probudila.
# ['Rezultat za 1']
# Vrijeme izvođenja 2.50 sekunde