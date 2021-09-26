from libretranslatepy import LibreTranslateAPI
lt = LibreTranslateAPI("https://libretranslate.de/")


def detectLanguage(text):
    return lt.detect(text)


def getlanguages():
    return lt.languages()
