from pathlib import Path

def search(substring):
    #print("Stiamo valutando la sottostringa %s" % (substring))
    numeri_in_lettere = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    for key, valore in numeri_in_lettere.items():
       # print("Stiamo valutando la chiave %d con valore %s" % (key, valore))
        risultato = substring.find(valore)
        if risultato > -1:
            return key
    
    return 0

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
        for key, valore in numeri_in_lettere.items():
            start = 0
            while True:
                start = riga.find(valore, start)
                if start == -1:
                    break
                if start > -1:
                    lista_di_sostituzione[start] = valore
                    start += len(valore)
            
            
        lista_di_sostituzione_ordinata = dict(sorted(lista_di_sostituzione.items()))
        for key, carattere in enumerate(riga):
            if key in lista_di_sostituzione_ordinata.keys():
                # trova il corrispondente numerico del valore in lettere
                valore_da_sostituire = lista_di_sostituzione_ordinata[key]
                corrispondente_numerico = list(numeri_in_lettere.keys())[list(numeri_in_lettere.values()).index(valore_da_sostituire)]
                lista_caratteri.append(corrispondente_numerico)
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


