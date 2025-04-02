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

def get_information(text: str) -> dict[int, str]:
    """Questa funzione analizza la stringa alla ricerca di due parametri di cui uno e un numero e l'altro il nome
    di un colore, poi una volta trovati la funzione crea un dizionario con chiave il numero e come valore la parola\n
    :param: una stringa di testo
    :return: un dizionari completo per ogni istanza nella stringa"""
    dizionario: dict[int, str] = {}

    for word in text.split():
        pattern1 = r"^[0-5]?\d$"  
        pattern2 = r"red|blue|green"  

        if re.match(pattern1, word):
            number = int(word)

        elif re.match(pattern2, word):
            color = word

            if number in dizionario:
                existing_color = dizionario[number]  

                if not isinstance(existing_color, list):
                    dizionario[number] = [existing_color, color]
                else:
                    existing_color.append(color)
            else:
                dizionario[number] = color

    return dizionario