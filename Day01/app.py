from pathlib import Path
import prova as p
# Creo un oggetto Path
path = Path("Day01/input.txt")

# Apro il file in lettura
with open(path, "r") as file:
    
    lista_risultati: list[int] = []
    numeri_in_lettere = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for riga in file:
        print("Stiamo valutando la riga %s" % (riga))
       
        lista_caratteri: list[int] = []
        
        """Dentro questa funzione, che puoi vedere sul nuovo file che ho creato, c'è un dizionario che racchiude tutte 
        le eccezioni possibili perche purtroppo non sono riuscito ad automatizzare il processo quindi le ho scritte a 
        mano ;) 
        
        questa soluzione dovrebbe funzionare poi va controllata"""
        
        #chiamo la funzione per rimpiazzare i numeri
        nuova_riga = p.replace_words(riga)

        print("riga rielaborata = %s" % (nuova_riga))

        #trasferisco i caratteri numerici in una lista
        for carattere in nuova_riga:
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