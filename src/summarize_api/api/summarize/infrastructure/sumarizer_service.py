# coding=utf-8
import os
from hunspell import HunSpell

import nltk
import summa


class SumarizerProvider:
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
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

        self.dictionary_list = {
            'da': {
                'dic': self.path + '/hunspell-dictionaries/da_DK/index.dic',
                'aff': self.path + '/hunspell-dictionaries/da_DK/index.aff',
            },
            'nl': {
                'dic': self.path + '/hunspell-dictionaries/nl_NL/index.dic',
                'aff': self.path + '/hunspell-dictionaries/nl_NL/index.aff',
            },
            'en': {
                'dic': self.path + '/hunspell-dictionaries/en_US/index.dic',
                'aff': self.path + '/hunspell-dictionaries/en_US/index.aff',
            },
            'fi': {
                'dic': None,
                'aff': None,
            },
            'fr': {
                'dic': self.path + '/hunspell-dictionaries/fr_FR/index.dic',
                'aff': self.path + '/hunspell-dictionaries/fr_FR/index.aff',
            },
            'de': {
                'dic': self.path + '/hunspell-dictionaries/de_DE/index.dic',
                'aff': self.path + '/hunspell-dictionaries/de_DE/index.aff',
            },
            'hu': {
                'dic': None,
                'aff': None,
            },
            'it': {
                'dic': self.path + '/hunspell-dictionaries/it_IT/index.dic',
                'aff': self.path + '/hunspell-dictionaries/it_IT/index.aff',
            },
            'no': {
                'dic': self.path + '/hunspell-dictionaries/nn_NO/index.dic',
                'aff': self.path + '/hunspell-dictionaries/nn_NO/index.aff',
            },
            'pt': {
                'dic': self.path + '/hunspell-dictionaries/pt_PT/index.dic',
                'aff': self.path + '/hunspell-dictionaries/pt_PT/index.aff',
            },
            'ro': {
                'dic': self.path + '/hunspell-dictionaries/ro_RO/index.dic',
                'aff': self.path + '/hunspell-dictionaries/ro_RO/index.aff',
            },
            'ru': {
                'dic': self.path + '/hunspell-dictionaries/ru_RU/index.dic',
                'aff': self.path + '/hunspell-dictionaries/ru_RU/index.aff',
            },
            'es': {
                'dic': self.path + '/hunspell-dictionaries/es_ES/index.dic',
                'aff': self.path + '/hunspell-dictionaries/es_ES/index.aff',
            },
            'sv': {
                'dic': self.path + '/hunspell-dictionaries/sv_SE/index.dic',
                'aff': self.path + '/hunspell-dictionaries/sv_SE/index.aff',
            },
        }
        self.lemmanizer = nltk.wordnet.WordNetLemmatizer()

    def extract_keywords(self, text, language, words=None):

        if self.is_supported(language) is False:
            return False, []

        language_name = self.language_list.get(language)
        text = text.encode('utf-8').strip()

        # How about lemmatizing and stemming ALL words?
        stemmer = self._build_stemmer(language)
        text = self._normalize_text_keywords(stemmer, text)

        if words is None:
            return summa.keywords.keywords(text=text, language=language_name, split=True, ratio=0.2)
        else:
            return summa.keywords.keywords(text=text, language=language_name, split=True, ratio=0.2, words=words)

    def _normalize_text_keywords(self, stemmer, text):
        result_list = []
        word_list = text.split(' ')
        for word in word_list:
            lemmanized = self.lemmanizer.lemmatize(word.decode('utf-8'))

            # Ideally now we would ask for the stem or base word form and append that one instead.
            if stemmer is not None:
                stemmed = stemmer.stem(lemmanized.encode('utf-8').strip())

                if len(stemmed) > 0:
                    result_list.append(stemmed[0].decode('utf-8'))
                else:
                    result_list.append(lemmanized)

            else:
                result_list.append(lemmanized)
        text = str.join(' ', result_list)
        text = text.encode('utf-8').strip()
        return text

    def _build_stemmer(self, language):
        stemmer = None

        dictionary = self.dictionary_list.get(language)
        if dictionary is not None and dictionary.get('dic') is not None:
            stemmer = HunSpell(dictionary.get('dic'), dictionary.get('aff'))

        return stemmer

    def extract_summary(self, text, language, words=None):

        if self.is_supported(language) is False:
            return False, ""

        language = self.language_list.get(language)
        text = text.encode('utf-8').strip()

        if words is None:
            return summa.summarizer.summarize(text=text, language=language, )
        else:
            return summa.summarizer.summarize(text=text, language=language, words=words, )

    def is_supported(self, code):
        return code in self.language_list
