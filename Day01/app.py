from pathlib import Path

# Creo un oggetto Path
path = Path("Day01/input.txt")

# Apro il file in lettura
with open(path, "r") as file:
    
    lista_risultati: list[int] = []
    numeri_in_lettere = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for riga in file:
        print("Stiamo valutando la riga %s" % (riga))
       
        lista_caratteri: list[int] = []
        # iteriamo il nostro dizionario di corrispondenze tra numeri e parole
        for chiave, valore in numeri_in_lettere.items():
            # sostituiamo la parola con il numero nella riga e la sovrascriviamo così alla
            # prossima iterazione la riga valutata sarà già aggiornata.
            riga = riga.replace(valore, str(chiave))

        # Questa soluzione ha ancora un difetto:
        #    le parole sono sostituite in un ordine preciso (quello del dizionario `numeri_in_lettere`)
        #    quindi se abbiamo una riga come `twone4oasd` alla prima iterazione la riga diventerà `tw14oasd`
        #    e alla seconda iterazine la parola `two` all'inizio della riga non verrà trasformata in numero.
        #    
        #    Una possibile soluzione sarebbe individuare queste parole senza modificare la riga.

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