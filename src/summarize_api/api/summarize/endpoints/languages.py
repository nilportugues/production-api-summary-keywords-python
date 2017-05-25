# coding=utf-8
import logging

from flask_restplus import Resource

from ..services.languages import LanguagesServices
from ...restplus import api
from ...summarize.serializers import languages_success_response

log = logging.getLogger(__name__)
ns = api.namespace('')


@ns.route('/languages')
class LanguagesResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        self.languages_service = LanguagesServices()
        super(LanguagesResource, self).__init__(api, *args, **kwargs)

    @api.response(200, 'Success', languages_success_response)
    def get(self):
        """
        Returns a list with all the supported languages.
        """
        languages = self.languages_service.list()
        return {'languages': languages}, 200
