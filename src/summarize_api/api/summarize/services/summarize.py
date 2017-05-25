import googletrans

ALLOWED_LANGUAGES = ['af', 'sq', 'ar', 'be', 'bg', 'ca', 'zh-CN', 'zh-TW', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et',
                     'tl', 'fi', 'fr', 'gl', 'de', 'el', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'ko', 'la',
                     'lv', 'lt', 'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es', 'sw',
                     'sv', 'th', 'tr', 'uk', 'vi', 'cy', 'yi', ]

FIELD_TEXT = 'text'
FIELD_FROM_LANGUAGE = 'from_language'

ERROR_FIELD_FROM_LANGUAGE = 'Missing `from_language` field in the request\'s body.'
ERROR_FIELD_TEXT = 'Missing `text` field in request\'s body.'
ERROR_FIELD_FROM_LANGUAGE_NOT_SUPPORTED = 'Provided `from_language` value `{language}` is not supported.'


class SummarizeService:
    def __init__(self):
        pass

    def execute(self, dto):

        # Validate input
        errors = self._validate_dto(dto)
        if errors != {}:
            return False, errors

        # Read data
        from_language = dto.get(FIELD_FROM_LANGUAGE, 'auto')
        text = dto.get(FIELD_TEXT, "")

        summary = ''

        return True, {
            "summary": summary
        }

    def _validate_dto(self, dto):
        errors = {}

        if dto.get(FIELD_FROM_LANGUAGE, None) is None:
            errors[FIELD_FROM_LANGUAGE] = ERROR_FIELD_FROM_LANGUAGE
        else:
            from_language = dto.get(FIELD_FROM_LANGUAGE)
            if not self._is_valid_language(from_language) and not 'auto' == from_language:
                errors[FIELD_FROM_LANGUAGE] = ERROR_FIELD_FROM_LANGUAGE_NOT_SUPPORTED \
                    .replace('{language}', from_language)

        if not FIELD_TEXT in dto:
            errors[FIELD_TEXT] = ERROR_FIELD_TEXT

        return errors

    @staticmethod
    def _is_valid_language(language):

        if language in ALLOWED_LANGUAGES:
            return True

        return False
