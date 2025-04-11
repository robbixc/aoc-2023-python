import re

def get_game_id(text: str):
    """questa funzione prende il pattern lo trova nel testo dato e ritorna un integer del numero trovato\n
    :param: una stringa di testo
    :return: il numero trovato dentro il pattern"""  
    pattern = r'Game (\d+):'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        print("No game ID found in the input")

def remove(text: str) -> str:
    """questa funzione rimuove il suffisso game + numero dalla stringa di testo\n
    :param: una stringa di testo
    :return: la stringa di testo modificata"""
    pattern = r'Game (\d+):'
    new_text = re.sub(pattern, "", text)
    return new_text

def get_information(text: str) -> dict[str, list[int]]:
    """Questa funzione analizza la stringa alla ricerca di due parametri di cui uno e un numero e l'altro il nome
    di un colore, poi una volta trovati la funzione crea un dizionario con chiave il colo9re e come valore la lista dei numeri\n
    :param: una stringa di testo
    :return: un dizionari completo per ogni istanza nella stringa"""
    
    dizionario: dict[str, list[int]] = {}
    megapattern = r"((?P<numero>[0-9]{1,2})+\s(?P<colore>[a-z]+),?)+"
    matches = re.findall(megapattern, text)
    for match in matches:
        if match[2] in dizionario:
            dizionario[match[2]].append(int(match[1]))
        else:
            dizionario[match[2]] = list([int(match[1])])
    return dizionario 

def filter_game_id(partite: dict[int, dict[str, list[int]]]) -> list[int]:
    """Questa funzione filtra i game id in base a tre condizioni:\n
    1. Se il colore rosso contiene un numero compreso tra 12 e 20, il game id viene escluso.
    2. Se il colore verde contiene un numero compreso tra 13 e 20, il game id viene escluso.
    3. Se il colore blu contiene un numero compreso tra 14 e 20, il game id viene escluso.\n
    :param: un dizionario con i game id e i colori
    :return: una lista di game id che soddisfano le condizioni"""
    lista_ids_coretti = []

    lista1 = set(range(13, 21))
    lista2 = set(range(14, 21))
    lista3 = set(range(15, 21))

    for game_id, colori in partite.items():
        if colori: # Verifica se il dizionario non è vuoto
            if any(value in lista1 for value in colori.get("red", [])):
                continue
            if any(value in lista2 for value in colori.get("green", [])):
                continue
            if any(value in lista3 for value in colori.get("blue", [])):
                continue
        
        lista_ids_coretti.append(game_id)

    return lista_ids_coretti


