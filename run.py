# coding: utf-8

from flask import Flask, jsonify, request
import json

from werkzeug.wrappers import response


app = Flask(__name__)


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


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def crud(id) -> json:
    """
      Retorna um desenvolvedor pelo seu id, como também altera ou deleta o mesmo pelo id informado.
    """
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'Error', 'mensagem': 'Desenvolvedor de ID {id} inexistente.'.format(id=id)}
        except Exception:
            response = {'status': 'Error', 'mensagem': 'Erro desconhecido. Procure o administrador da API.'}        
        return jsonify(response)
    elif request.method == 'PUT':
        desenvolvedores[id] = json.loads(request.data)
        return jsonify(desenvolvedores[id])
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro excluído com sucesso.'})


@app.route('/dev/', methods=['POST', 'GET'])
def listar() -> json:
    """
      Listar desenvolvedores e também permite inserir um novo desenvolvedor.
    """
    if request.method == 'POST':
        response = json.loads(request.data)
        contador = len(desenvolvedores)
        response['id'] = contador
        desenvolvedores.append(response)
        return jsonify(desenvolvedores[contador])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)
