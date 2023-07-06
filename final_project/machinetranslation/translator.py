from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    englishText = translator.translate(frenchText)
    return englishText

