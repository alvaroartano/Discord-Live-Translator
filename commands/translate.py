from libretranslatepy import LibreTranslateAPI
lt = LibreTranslateAPI("https://translate.argosopentech.com/")


def detectLanguage(text):
    print(lt.detect(text))
    return lt.detect(text)


def getlanguages():
    return lt.languages()


def translate(text, lang):
    return lt.translate(text, "auto", lang)
