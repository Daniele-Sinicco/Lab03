import string
import time as t

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multidizionario = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        input_modif = replaceChars(txtIn).lower()
        start_contains = t.time()
        parole_processate_c = self.multidizionario.searchWord(input_modif, language)
        end_contains = t.time()
        print("______________________________\n"+
              "Using Contains"
              )
        for w in parole_processate_c:
            if w.corretta is False:
                print(w)
        print("Time elapsed:" + str(end_contains-start_contains))
        print("______________________________")

        start_linear = t.time()
        parole_processate_l = self.multidizionario.searchWordLinear(input_modif, language)
        end_linear = t.time()
        print("Using linear search")
        for w in parole_processate_l:
            if w.corretta is False:
                print(w)
        print("Time elapsed:" + str(end_linear - start_linear))
        print("______________________________")

        start_dicho = t.time()
        parole_processate_d = self.multidizionario.searchWordDichotomic(input_modif, language)
        end_dicho = t.time()
        print("Using dichotomic search")
        for w in parole_processate_d:
            if w.corretta is False:
                print(w)
        print(f"Time Elapsed: {(end_dicho - start_dicho):e}\n")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    new_text = ""
    for char in text:
        if char in string.punctuation or char == '\n':
            new_text += ""
        else:
            new_text += char.lower()
    return new_text
