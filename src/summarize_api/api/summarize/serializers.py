from flask_restplus import fields

from api.restplus import api

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

# ----------------------------

detect_text_request = api.model('detect_text_request', {
    'text': fields.String(description='Text to detect'),
})

detect_text_response = api.model('detect_text_response', {
    'language': fields.String(description='Guessed language'),
    'confidence': fields.Float(description="Degree of confindence")
})

summarize_text_request = api.model('Translate text', {
    'from_language': fields.String(description='Translate to'),
    'to_language': fields.String(description='Translate to'),
    'text': fields.String(description='Text to translate'),
})

summarized_text_response = api.model('Translated text', {
    'original': fields.String(description='Original text'),
    'translated': fields.String(description='Translated text'),

})
