# coding=utf-8
from flask_restplus import fields

from api.restplus import api
from .services.languages import LanguagesServices

vnd_error = api.model('api_error', {
    'message': fields.String(required=True, description='Error description'),
    'path': fields.String(required=True, description='Field or parameter causing the error'),
})
vnd_errors = api.model('api_errors', {
    'errors': fields.List(fields.Nested(vnd_error, required=True), required=True)
})

vnd_error_schema = api.model('vnd_error_schema', {
    'total': fields.Integer(required=True, description='Total errors'),
    '_embedded': fields.Nested(vnd_errors, required=True)
})

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------


summarize_text_request = api.model('Summarize text', {
    'from_language': fields.String(description='Language'),
    'text': fields.String(description='Text to Summarize'),
    'words': fields.Integer(description='Number of words to summarize', required=False),
})

summarized_text_response = api.model('Summarized text', {
    'summary': fields.String(description='Summarized text'),

})

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

keywords_text_request = api.model('Keywords', {
    'from_language': fields.String(description='Language'),
    'text': fields.String(description='Text to extract keywords from'),
    'keywords': fields.Integer(description='Number of keywords'),
})


keywords_text_response = api.model('List of keywords', {
    'keywords': fields.List(fields.String(), description='List of keywords'),

})

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

languages_service = LanguagesServices()
languages_success_response = api.model('language_list', {
    'languages': fields.Raw(languages_service.list(), required=True)
})
