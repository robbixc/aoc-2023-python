import re

def get_game_id(text):
    """questa funzione prende il pattern lo trova nel testo dato e ritorna un integer del numero trovato\n
    :param: una stringa di testo
    :return: il numero trovato dentro il pattern"""  
    pattern = r'Game (\d+):'
    match = re.search(pattern, text)
    if match:
        return int(match.group(1))
    else:
        print("No game ID found in the input")

"""
questa è una funzione working in progress che mira ad estrapolare dal testo usando un pattern, i numeri e le parole
affibbiate ad esse per poi inserirle in un dizionario da cui poi potremmo riprendere le informazioni
per calcolare quale game sono andati a buon fine per poi trasferire gli id nella lista id e fare la somma degli id vincenti
e consueguentemente risolvere il day2 


def get_information(text):
    input_string = text

    numbers = re.findall(r'\d+', input_string) 
    words = re.split('[0-9]', input_string)[1:]

    result_dict = {}
    for idx, key in enumerate(numbers):  
        result_dict[key] = words[idx].strip().split(',')[0]

    print(result_dict)

    return result_dict
"""    