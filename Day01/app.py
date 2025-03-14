from pathlib import Path

# Creo un oggetto Path
path = Path("Day01/input.txt")


# creo una lista per verificare se un numero è presente nelle righe
lista_numeri: list[int] = [numero for numero in range(1, 2021)]


# Apro il file in lettura
with open(path, "r") as file:
    riga = file.readline()
    for riga in file:
        print("Stiamo valutando la riga %s" % (riga))
        
        
print("\nPROGRAMMA TERMINATO")        