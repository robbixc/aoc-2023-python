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

def get_information(text: str) -> dict[int, list[int]]:
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