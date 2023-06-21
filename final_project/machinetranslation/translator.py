'''
Translates text from French to English and vice-versa
depending on the language of the passed-in text
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    Translates passed-in english text to french
    and returns the translated french text.
    '''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    Translates passed-in french text to english
    and returns the translated english text.
    '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
