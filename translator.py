import dictionary
from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        print("------------------------")
        print("Translator Alien-Italian")
        print("------------------------")
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca una wildcard")
        print("4. Exit")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit


    def loadDictionary(self, nomeFile):
        dizionario = {}
        with open(nomeFile, "r") as file:
            for line in file:
                campi = line.rstrip("\n").split(" ")
                traduzioni = campi[1:]
                dizionario[campi[0]] = traduzioni
        self.dictionary.loaddict(dizionario)
        # dict is a string with the filename of the dictionary

    def stampa_dizionario(self):
        for chiave in self.dictionary.dictionary:
            print(f"{chiave} {self.dictionary.dictionary[chiave]}")


    def handleAdd(self, entry):
        campi = entry.split(" ")
        if len(campi) < 2:
            print("Errore devi inserire almeno <parola aliena> <traduzione>")
            return
        chiave = campi[0]
        traduzioni = campi[1:]
        for traduzione in traduzioni:
            self.dictionary.addWord(chiave, traduzione)
        self.dictionary.saveToFile("dictionary.txt")
        print(chiave, traduzioni)
        print("Aggiunta!")

        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        lista = self.dictionary.translate(query)
        print(lista)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        lista = self.dictionary.translateWordWildCard(query)
        print(lista)