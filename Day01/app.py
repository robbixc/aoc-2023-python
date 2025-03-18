import itertools as it
from pathlib import Path

# Creo un oggetto Path
path = Path("Day01/input.txt")


# creo una lista per verificare se un numero è presente nelle righe
lista_numeri: list[int] = [numero for numero in range(1, 2021)]


# Apro il file in lettura
with open(path, "r") as file:
    riga = file.readline()
    
    lista_risultati: list[int] = []
    
    for riga in file:
        print("Stiamo valutando la riga %s" % (riga))
        #divide la stringa in caratteri
        caratteri = list(it.islice(riga, 0, len(riga) + 1))
        
        lista_caratteri: list[int] = []
        
        #trasferisco i caratteri numerici in una lista
        for carattere in caratteri:
            if carattere.isnumeric(): #controlla se il carattere è un numero
                carattere = int(carattere)
                lista_caratteri.append(carattere)   
            else:
                continue

        #prendo il primo numero e l'ultimo numero e li metto adiacenti
        for _ in lista_caratteri:
            str1 = lista_caratteri[0]
            str2 = lista_caratteri[-1]

            risultato = str(str1) + str(str2)
            risultato = int(risultato)

        lista_risultati.append(risultato)

    #stampa la somma di tutti i risultati    
    print(sum(lista_risultati))

print("\nPROGRAMMA TERMINATO")        