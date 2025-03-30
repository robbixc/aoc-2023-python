from pathlib import Path

def replace_words(text):
    """Questa funzione prende una stringa a fa due controlli, il primo per rivelare parole strane, l'altro per
    per controllare i numeri normali, ed ha l'obbiettivo di scambiare i numeri strani in numeri ed i numeri normali in
    numeri\n
    
    :param: una stringa di testo
    :return: una stringa modificata"""
    
    numeri_in_lettere = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    numeri_strani = {18:"oneight", 38:"threeight", 21:"twone", 82:"eightwo", 83:"eighthree", 58:"fiveight", 
                     79:"sevenine", 98:"nineight" }
    for number, word in numeri_strani.items():
        text = text.replace(word, str(number))
    for number, word in numeri_in_lettere.items():
        text = text.replace(word, str(number))
    return text

