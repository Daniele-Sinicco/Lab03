import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self._mappa_dizionari = {}
        diz_italian = d.Dictionary("italian")
        diz_italian.loadDictionary("resources/Italian.txt")
        diz_english = d.Dictionary("english")
        diz_english.loadDictionary("resources/English.txt")
        diz_spanish = d.Dictionary("spanish")
        diz_spanish.loadDictionary("resources/Spanish.txt")
        self._mappa_dizionari["italian"] = diz_italian
        self._mappa_dizionari["english"] = diz_english
        self._mappa_dizionari["spanish"] = diz_spanish


    def printDic(self, language):
        if language == "italian" or language == "english" or language == "spanish":
            self._mappa_dizionari.get(language, None).printAll()



    def searchWord(self, words, language):
        if language == "italian" or language == "english" or language == "spanish":
            diz = self._mappa_dizionari.get(language, None)
            words_split = words.split(" ")
            lista_richword = []
            """for i in range(0, len(words_split)):
                parola = rw.RichWord(words_split[i])
                if words_split[i] in diz.dict:
                    parola.corretta = True
                else:
                    parola.corretta = False
                lista_richword.append(parola)
            return lista_richword"""

            for i in range(0, len(words_split)):
                parola = rw.RichWord(words_split[i])
                if diz.dict.__contains__(words_split[i]):
                    parola.corretta = True
                else:
                    parola.corretta = False
                lista_richword.append(parola)
            return lista_richword

    def searchWordLinear(self, words, language):
        if language == "italian" or language == "english" or language == "spanish":
            diz = self._mappa_dizionari.get(language, None)
            words_split = words.split(" ")
            lista_richword = []
            for i in range(0, len(words_split)):
                parola = rw.RichWord(words_split[i])
                for w in diz.dict:
                    if words_split[i] == w:
                        parola.corretta = True
                        break
                if parola.corretta == None:
                    parola.corretta = False
                lista_richword.append(parola)
            return lista_richword

    def searchWordDichotomic(self, words, language):
        if language == "italian" or language == "english" or language == "spanish":
            diz = self._mappa_dizionari.get(language, None)
            words_split = words.split(" ")
            lista_richword = []
            for i in range(0, len(words_split)):
                parola = rw.RichWord(words_split[i])
                inf = 0
                sup = len(diz.dict)-1
                medio_attuale = 0
                while parola.corretta == None and inf <= sup:
                    medio_attuale = (inf + sup) // 2
                    if words_split[i] == diz.dict[medio_attuale]:
                        parola.corretta = True
                        break
                    elif words_split[i] < diz.dict[medio_attuale]:
                        sup = medio_attuale-1
                        continue
                    else:
                        inf = medio_attuale+1
                        continue
                if parola.corretta == None:
                    parola.corretta = False
                lista_richword.append(parola)
            return lista_richword
