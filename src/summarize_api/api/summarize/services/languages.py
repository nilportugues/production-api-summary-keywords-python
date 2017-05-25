class LanguagesServices:
    def __init__(self):
        pass

    @staticmethod
    def execute():
        data = [
            'danish',
            'dutch',
            'english',
            'finnish',
            'french',
            'german',
            'hungarian',
            'italian',
            'norwegian',
            'porter',
            'portuguese',
            'romanian',
            'russian',
            'spanish',
            'swedish'
        ]

        return True, {
            "languages": data
        }
