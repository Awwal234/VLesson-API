from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
info_namespace = Namespace('info', description='get track information')

course = ['FrontEnd', 'BackEnd', 'Product Design']

@info_namespace.route('/info')
class GETTRACK(Resource):
    def get(self):
        '''
            Get Track Names
        '''

        response = {
            'track': course
        }

        return response, HTTPStatus.OK 