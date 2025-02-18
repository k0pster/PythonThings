from TextAnalyzer import TextAnalyzer

#tworzymy jakiś string tekstu, który chcemy przeanalizować
givenstring = "Odkąd pamiętam, grałam solo całe dni Ma intuicja ciągle zawodziła mnie I nie miałam z kim przy Beatles-ach wina pić Było słabo, wiem Codziennie narzekałam, gdzie ten happy end Me vibrato chciało dalej się wznieść Ja nie pytam już i wiem o co chodzi mu A w mej głowie luz"

#tworzymy obiekt klasy TextAnalyzer
analyzed = TextAnalyzer(givenstring)

#sprawdzenie poprawności listy po sformatowaniu poprzez wynikową inicjalizatora klasy
print("Formatted text: ",analyzed.fmtText)

#sprawdznie wszystkich słów z licznikiem metodą klasy freqAll()
print(f"Unique words in text: {analyzed.freqAll()}")

#sprawdzenie wystapienia np. słowa 'wiem' metodą klasy freqOf()
lookingWord = 'wiem'
print(f"word '{lookingWord}' count in text {analyzed.freqOf(lookingWord)} times")