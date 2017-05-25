# coding=utf-8
from ..infrastructure.sumarizer_service import SumarizerProvider


class LanguagesServices:
    def __init__(self):
        self.service = SumarizerProvider()

    def list(self):
        return self.service.language_list.keys()
