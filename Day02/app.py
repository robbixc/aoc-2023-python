from pathlib import Path
import funzioni_day2 as fd

# Creo un oggetto Path
path = Path("Day02/input.txt")

#creo una lista per gli id dei giochi
lista_ids = []

# Apro il file in lettura
with open(path, "r") as file:
    righe = file.readlines()

    #creo una lista degli game id coretti
    lista_game_id_corretti = []

    #creo un dizionario cosi che le ogni partita venga affibbiata col proprio game id
    lista_partite = {}

    for riga in righe:
        print("\nStiamo valutando la riga: %s\n" % (riga))

        #prendiamo il game id
        game_id = fd.get_game_id(riga)
        lista_ids.append(game_id)

        riga_nuova = fd.remove(riga)
        lista_partita: dict[int, str] = fd.get_information(riga_nuova)
        print(lista_partita)

        lista_partite[game_id] = lista_partita

    """allora io ho provato a cancellare i game id dove le partite venivano perse ma non ci sono riuscito benissimo
    credo che ci siano ancora degli errori poi ce da dare una controllata"""
    for game_id in lista_ids:
        if lista_partite[game_id].values() in range(15,21):
            lista_partite.pop(game_id)
        else:
            lista_game_id_corretti.append(game_id)

print(sum(lista_game_id_corretti))

print("\nPROGRAMMA TERMINATO")    