import heapq
import heapq

def dijkstra(graf, pocetni):
    udaljenosti = {cvor: float('inf') for cvor in graf}
    udaljenosti[pocetni] = 0
    
    prioritetni_red = [(0, pocetni)]
    
    while prioritetni_red:
        trenutna_udaljenost, trenutni_cvor = heapq.heappop(prioritetni_red)
        
        if trenutna_udaljenost > udaljenosti[trenutni_cvor]:
            continue
        
        for susjed, tezina in graf[trenutni_cvor]:
            udaljenost_do_susjeda = trenutna_udaljenost + tezina
            if udaljenost_do_susjeda < udaljenosti[susjed]:
                udaljenosti[susjed] = udaljenost_do_susjeda
                heapq.heappush(prioritetni_red, (udaljenost_do_susjeda, susjed))
    
    return udaljenosti

graf = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graf, 'A'))