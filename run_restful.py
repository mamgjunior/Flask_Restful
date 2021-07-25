from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {
        'id': 0,
        'nome': 'Marcos Maia',
        'habilidades': ['Python', 'Delphi', 'SQL', 'JavaScript', 'Django', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Deivide spinosa',
        'habilidades': ['C#', 'Unity', 'Adoby', 'Python']
    }
]


class Desenvolvedores(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Error', 'mensagem': 'Desenvolvedor de ID {id} inexistente.'.format(id=id)}
        except Exception:
            response = {'status': 'Error', 'mensagem': 'Erro desconhecido. Procure o administrador da API.'}        
        return response

    def put(self, id):
        desenvolvedores[id] = json.loads(request.data)
        return desenvolvedores[id]

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'mensagem': 'Registro excluído com sucesso.'}


class ListarDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        response = json.loads(request.data)
        contador = len(desenvolvedores)
        response['id'] = contador
        desenvolvedores.append(response)
        return desenvolvedores[contador]


api.add_resource(Desenvolvedores, '/dev/<int:id>/')
api.add_resource(ListarDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/dev/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
