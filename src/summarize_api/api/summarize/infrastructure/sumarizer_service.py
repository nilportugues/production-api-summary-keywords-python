# coding=utf-8
import summa

class SumarizerProvider:
    def __init__(self):
        self.language_list = {
            'da': 'danish',
            'nl': 'dutch',
            'en': 'english',
            'fi': 'finnish',
            'fr': 'french',
            'de': 'german',
            'hu': 'hungarian',
            'it': 'italian',
            'no': 'norwegian',
            'pt': 'portuguese',
            'ro': 'romanian',
            'ru': 'russian',
            'es': 'spanish',
            'sv': 'swedish',
        }

    def extract_keywords(self, text, language, words=None):

        if self.is_supported(language) is False:
            return False, []

        language = self.language_list.get(language)
        text = text.encode('utf-8').strip()

        if words is None:
            return summa.keywords.keywords(text=text, language=language, split=True, ratio=0.2)
        else:
            return summa.keywords.keywords(text=text, language=language, split=True, ratio=0.2, words=words)

    def extract_summary(self, text, language, words=None):

        if self.is_supported(language) is False:
            return False, ""

        language = self.language_list.get(language)
        text = text.encode('utf-8').strip()

        if words is None:
            return summa.summarizer.summarize(text=text, language=language, )
        else:
            return summa.summarizer.summarize(text=text, language=language, words=words,)

    def is_supported(self, code):
        return code in self.language_list
