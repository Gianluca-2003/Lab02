import translator as tr
from dictionary import Dictionary


def main():
    t = tr.Translator()
    t.loadDictionary("dictionary.txt")
    t.printMenu()
    #4t.stampa_dizionario()
    while True:
        txtIn = int(input("Inseriesci un numero: "))
        if txtIn == 1:
            entry = input("Inserisci le parole: ")
            t.handleAdd(entry)
        if txtIn == 2:
            query = input("Ok, quale parola devo cercare? ")
            t.handleTranslate(query)
        if txtIn == 3:
            query = input("Ok, quale parola devo cercare? ")
            t.handleWildCard(query)
        if txtIn == 4:
            break

main()


