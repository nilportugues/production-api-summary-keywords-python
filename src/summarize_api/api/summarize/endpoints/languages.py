import logging

from flask_restplus import Resource

from ..services.languages import LanguagesServices
from ...restplus import api
from ...summarize.serializers import *

log = logging.getLogger(__name__)
ns = api.namespace('')

languages = LanguagesServices.execute()

language_list = api.model('language_list', {
    'languages': fields.Raw(languages, required=True)
})


@ns.route('/languages')
class LanguagesResource(Resource):
    @api.response(200, 'Success', language_list)
    def get(self):
        """
        Returns a key-value list with all the supported languages.
        """
        return {'languages': languages}, 200

