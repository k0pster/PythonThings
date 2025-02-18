#TextAnalyzer class count frequency of unique words in provided text
class TextAnalyzer(object):
#Inicjalizacja klasy przyjmującej string z pozbyciem się nie chcianych znaków i usunięciem wielkich liter
    def __init__(self,text):
        formattedText = text.replace('.','').replace(',','').replace('!','').replace('?','').replace('#','')

        formattedText = formattedText.lower()
        self.fmtText = formattedText


#Metoda freqAll czyli slownik w ktorym liczone jest wystapienie danego slowa w tekscie
    def freqAll(self):
        #Tworzymy najpierw listę wszystkich wyrazów inicjalizatorem klasy używajac metody split
        #wykorzystując spację jako separator
        wordList = self.fmtText.split(' ')

        #tworzymy słownik ze słowem(dodatkowo metoda set() dla usunięcia powtórek) i liczbą wystąpienia w tekście
        freqMap = {}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap

#Metoda freqOf przyjmujaca dane słowo unikalne i pokazująca ile razy było w tekscie
    def freqOf(self,word):
        #pobieramy nasz wypełniony słownik metodą freqAll()
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0