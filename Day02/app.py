from pathlib import Path
import funzioni_day2 as fd

# Creo un oggetto Path
path = Path("Day02/input.txt")

#creo una lista per gli id dei giochi
lista_ids = []


"""
lista_numeri = [numero for numero in range(1, 101)] funzione non usata 
"""

# Apro il file in lettura
with open(path, "r") as file:
    righe = file.readlines()

    for riga in righe:
        print("Stiamo valutando la riga: %s" % (riga))

        #prendiamo il game id
        game_id = fd.get_game_id(riga)
        print(game_id)
        lista_ids.append(game_id)

        
        
                

        







print("\nPROGRAMMA TERMINATO")    