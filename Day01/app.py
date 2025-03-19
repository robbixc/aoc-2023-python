from pathlib import Path

# Creo un oggetto Path
path = Path("Day01/input.txt")

# Apro il file in lettura
with open(path, "r") as file:
    
    lista_risultati: list[int] = []
    
    for riga in file:
        print("Stiamo valutando la riga %s" % (riga))
       
        lista_caratteri: list[int] = []
        
        #trasferisco i caratteri numerici in una lista
        for carattere in riga:
            if carattere.isnumeric(): #controlla se il carattere è un numero
                carattere = int(carattere)
                lista_caratteri.append(carattere)

        #prendo il primo numero e l'ultimo numero e li metto adiacenti
        for _ in lista_caratteri:
            str1 = lista_caratteri[0]
            str2 = lista_caratteri[-1]

            risultato = int(str(str1) + str(str2))

        lista_risultati.append(risultato)

    #stampa la somma di tutti i risultati    
    print(sum(lista_risultati))

print("\nPROGRAMMA TERMINATO")        