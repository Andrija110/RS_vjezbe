import asyncio
import time

async def dohvati_podatke_s_weba():
    """
    Korutina koja simulira dohvaćanje podataka s weba s kašnjenjem od 3 sekunde.
    """
    print(" Pokrenuto simuliranje dohvaćanja podataka...")

    await asyncio.sleep(3)

    podaci = [i for i in range(1, 11)]

    print(" Podaci dohvaćeni.")

    return podaci

if __name__ == "__main__":
    print(f"Početak programa: {time.strftime('%H:%M:%S')}")

    rezultat = asyncio.run(dohvati_podatke_s_weba())

    print(f"Kraj programa: {time.strftime('%H:%M:%S')}")
    print(f"Vraćeni podaci: {rezultat}")