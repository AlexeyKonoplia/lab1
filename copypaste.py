import wikipedia
import pypandoc
from KnutMorrisPratt import KnutMorissPratt

def copypaste(name = 'Улыбка.docx', wikiname = 'Улыбка', language = 'ru'):
    wikipedia.set_lang(language)
    wikitxt = wikipedia.page(wikiname).content.lower()
    txt = pypandoc.convert_file(name, 'plain').lower()
    sym = ',.-=!:()—[];"' + "'"

    for i in sym:
        wikitxt = wikitxt.replace(i, '')
        txt = txt.replace(i, '')
    txtarr = txt.split()

    counter = ''
    for i in txtarr:
        if KnutMorissPratt(wikitxt, i):
            counter += '1' * len(i) + '0'
        else:
            counter += ' '
    
    counterArr = counter.split()

    copied = 0
    for i in counterArr:
        lenght = len(i)
        if KnutMorissPratt(i, '0') >= 3:
            copied += KnutMorissPratt(i, '1')
    return (copied / len(txt)) * 100

print(copypaste())