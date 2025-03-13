from pathlib import Path

# Creo un oggetto Path
path = Path("Day01/input.txt")


# creo una lista per verificare se un numero è presente nelle righe
lista_numeri: list[int] = [numero for numero in range(1, 2021)]


# Apro il file in lettura
with open(path, "r") as file:
    riga = file.readline()
    """Le righe di sotto iterano sul file cercando di trovare i numeri ma purtroppo trovano dei numeri 
    che non sono presenti nel file, quindi non riesco a trovare i numeri giusti"""
    for riga in file:
        numeri = [numero for numero in lista_numeri if str(numero) in riga]
        print(numeri)
        
        
print("\nPROGRAMMA TERMINATO")        