import spellchecker as sp

class Dictionary:
    def __init__(self, language):
        self._language = language
        self._dict = []

    def loadDictionary(self,path):
        f = open(path, "r", encoding="utf-8")  #encoding per risolvere parzialmente errore di lettura della codifica
        riga = f.readline()                 #del diz. spagnolo (toglie l'errore di esecuzione ma non legge correttamente
        #print(riga)
        while riga != "":
            riga_modif = ""
            for letter in riga:
                if letter != '\n':
                    if letter == '/':   #controllo per eliminare le estensioni della codifica errata nel diz. spagnolo
                        break
                    else:
                        riga_modif += letter
            self._dict.append(riga_modif.lower())
            riga = f.readline()
        f.close()

    def printAll(self):
        for w in self._dict:
            print(w + "\n")


    @property
    def dict(self):
        return self._dict
