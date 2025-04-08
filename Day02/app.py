from pathlib import Path
import funzioni_day2 as fd

# Creo un oggetto Path
path = Path("Day02/input.txt")

# Apro il file in lettura
with open(path, "r") as file:
    righe = file.readlines()

    #creo un dizionario cosi che le ogni partita venga affibbiata col proprio game id
    lista_partite = {}

    for riga in righe:
        print("\nStiamo valutando la riga: %s\n" % (riga))

        #prendiamo il game id
        game_id = fd.get_game_id(riga)

        lista_partite[game_id] = fd.get_information(riga)
        print(lista_partite[game_id])

    #filtro i game id e creo una lista con i game id che soddisfano le condizioni
    lista_ids_coretti = fd.filter_game_id(lista_partite)
    
    print("\n\nLista dei game id corretti: %s" % (lista_ids_coretti))
    print("\nLa somma dei game id corretti è: %s" % (sum(lista_ids_coretti)))

print("\nPROGRAMMA TERMINATO")    