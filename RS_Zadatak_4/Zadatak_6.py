import asyncio, time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.') # <--- Ovu poruku želimo vidjeti
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) # scheduled
    task2 = asyncio.create_task(fetch_data(2)) # scheduled
    
    # 1. Cekamo samo na task1
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    
    # 2. Dodajemo umjetno kašnjenje (sleep)
    # Task2 je poceo raditi zajedno s Task1. Nakon 1 sekunde (task1 je gotov),
    # task2 treba jos 1 sekundu da se zavrsi.
    # Cekanjem od 1.5 sekundi dajemo event loop-u dovoljno vremena da završi task2.
    print("Main korutina ide na kratki spavanac da task2 završi...")
    await asyncio.sleep(1.5) 
    print("Main korutina se probudila.")
    
    # NE AWAITAMO task2, ali se njegov ispis 'Dovršio sam s 2.' izvršio u pozadini.
    # Budući da ga nismo awaitali, ne možemo dohvatiti njegov rezultat.
    
    return [result1] # Vracamo samo rezultat task1 jer task2 nismo awaitali

t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()

print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")