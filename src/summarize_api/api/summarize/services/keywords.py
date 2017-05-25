# coding=utf-8
from ..infrastructure.sumarizer_service import SumarizerProvider

FIELD_TEXT = 'text'
FIELD_WORDS = 'keywords'
FIELD_FROM_LANGUAGE = 'from_language'

ERROR_FIELD_FROM_LANGUAGE = 'Missing `from_language` field in the request\'s body.'
ERROR_FIELD_TEXT = 'Missing `text` field in request\'s body.'
ERROR_FIELD_FROM_LANGUAGE_NOT_SUPPORTED = 'Provided `from_language` value `{language}` is not supported.'
ERROR_FIELD_WORDS = 'Provided `keywords` value `{words}` must be 1 or more.'


class KeywordsService:
    def __init__(self):
        self.service = SumarizerProvider()

    def execute(self, dto):

        # Validate input
        errors = self._validate_dto(dto)
        if errors != {}:
            return False, errors

        # Read data
        from_language = dto.get(FIELD_FROM_LANGUAGE)
        text = dto.get(FIELD_TEXT)
        words = dto.get(FIELD_WORDS, None)

        keywords = self.service.extract_keywords(text, language=from_language, words=words)

        if keywords == "":
            return True, None

        return True, {"keywords":  keywords}

    def _validate_dto(self, dto):
        errors = {}

        if dto.get(FIELD_FROM_LANGUAGE, None) is None:
            errors[FIELD_FROM_LANGUAGE] = ERROR_FIELD_FROM_LANGUAGE
        else:
            from_language = dto.get(FIELD_FROM_LANGUAGE)
            if not self._is_valid_language(from_language):
                errors[FIELD_FROM_LANGUAGE] = ERROR_FIELD_FROM_LANGUAGE_NOT_SUPPORTED \
                    .replace('{language}', from_language)

        if not FIELD_TEXT in dto:
            errors[FIELD_TEXT] = ERROR_FIELD_TEXT

        keywords = dto.get(FIELD_WORDS, None)
        if keywords is not None:
            if not self._is_valid_words(keywords):
                errors[FIELD_WORDS] = ERROR_FIELD_WORDS.replace('{keywords}', keywords)

        return errors

    def _is_valid_language(self, language):
        return self.service.is_supported(language)

    def _is_valid_words(self, amount):
        return amount > 0
