class Dictionary:

    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = {}
        self.dictionary = dictionary


    def loaddict(self, dictionary):
        self.dictionary = dictionary

    def addWord(self, chiave, traduzione):
        chiave = chiave.lower()
        traduzione = traduzione.lower()

        if chiave not in self.dictionary:
            self.dictionary[chiave] = [traduzione]
        else:
            self.dictionary[chiave].append(traduzione)


    def translate(self, query):
        query = query.lower()
        try:
            return self.dictionary.get(query, "Parola aliena non trovata non trovata")
        except Exception as e:
            print(f"Error: {str(e)}")

    def saveToFile(self, filename):

        with open(filename, "w") as file:
            for key, value in self.dictionary.items():
                stringa = ""
                for traduzione in value:
                    stringa += traduzione + " "
                file.write(f"{key} {stringa}\n")








    def translateWordWildCard(self, query):
        query = query.lower()
        if query.count("?") != 1:
            return "Errore: deve esserci esattamente un punto interrogativo!"
        for chiave in self.dictionary:
            cnt = 0
            if len(chiave) == len(query):
                for i in range(len(query)):
                    if query[i] == chiave[i]:
                        cnt += 1
            if cnt == len(query)-1:
               return self.dictionary[chiave]
        