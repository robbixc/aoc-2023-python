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
        numeri_in_lettere = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        lista_di_sostituzione = {}
        # per ogni riga itero ogni singola parola/numero. Il problema come abbiamo visto in precedenza è 
        # trovare tutte le occorrenze.
        for key, valore in numeri_in_lettere.items():
            start = 0
            # con questo loop cerchiamo ogni singola parola finchè non abbiamo finito tutti caratteri della riga.
            # complicarlo così sembra necessario perchè `find` ritorna soltanto la prima occorrenza se usato normalmente.
            while True:
                start = riga.find(valore, start)
                if start == -1:
                    # find restituisce -1 quando non trova niente, questo significa che abbiamo di cercare e possiamo uscire dal loop.
                    break
                if start > -1:
                    # se invece `find` trova qualcosa, ci restituisce la posizione. Che io metto in un dizionario così da poter
                    # ricostruire dopo la sequenza di numeri e parole. La chiave sarà la posizione nella riga.
                    lista_di_sostituzione[start] = valore
                    # questo è importante, sposta la posizione di partenza del `find` di una lunghezza equivalente a quella
                    # di valore. Se ad esempio abbiamo trovato la parola `one`, il prossimo find cercherà a partire da 3 caratteri in avanti
                    start += len(valore)
            
        for key, carattere in enumerate(riga):
            # cerco se l'attuale chiave, cioè la posizione della riga che stiamo esaminando, è nel dizionario creato prima.
            # Se c'è vuol dire che in quella posizione c'è una parola numero!
            if key in lista_di_sostituzione.keys():
                # trova il corrispondente numerico del valore in lettere
                valore_da_sostituire = lista_di_sostituzione[key]
                # lo cerco nel dizionario in modo da poter aggiungere alla lista_caratteri il valore numero.
                corrispondente_numerico = list(numeri_in_lettere.keys())[list(numeri_in_lettere.values()).index(valore_da_sostituire)]
                lista_caratteri.append(corrispondente_numerico)
            # questa parte è uguale a prima, se è una cifra non cambia nulla rispetto alla parte 1    
            if carattere.isnumeric(): #controlla se il carattere è un numero
                carattere = int(carattere)
                lista_caratteri.append(carattere)
         
        print(lista_caratteri)        
        #prendo il primo numero e l'ultimo numero e li metto adiacenti
        for _ in lista_caratteri:
            str1 = lista_caratteri[0]
            str2 = lista_caratteri[-1]

            risultato = int(str(str1) + str(str2))

        lista_risultati.append(risultato)

    #stampa la somma di tutti i risultati    
    print(sum(lista_risultati))

print("\nPROGRAMMA TERMINATO")


