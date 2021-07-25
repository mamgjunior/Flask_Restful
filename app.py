from flask import Flask, json, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

from models import Pessoas, Atividades, Usuarios

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


@auth.verify_password
def validacao(login, senha) -> bool:
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    """
    Classe responsavel por obter as informações de uma pessoa pelo o nome da mesma, como também permite fazer uma edição ou deleção da mesma pelo nome.
    """
    @auth.login_required
    def get(self, nome) -> json:
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {'status': 'error', 'menssage': 'Pessoa nao encontrada!'}
        
        return response

    def put(self, nome) -> json:
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome) -> dict:
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'status': 'sucess', 'mensage': 'Pessoa excluida com sucesso.'}


class LitarPessoas(Resource):
    """
    Classe responsavél por inserir novas pessoas como também listar todas as pessoas.
    """
    @auth.login_required
    def get(self) -> json:
        pessoas = Pessoas.query.all()
        response = [{'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade} for pessoa in pessoas]
        if not response:
            response = {'status': 'Information', 'mensage': 'Nao existem pessoas cadastradas.'}

        return response
    
    def post(self) -> json:
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListarAtividade(Resource):
    """
    Classe responsavél por inserir novas atividades como também listar todas as atividades.
    """
    def get(self) -> json:
        atividades = Atividades.query.all()
        response = [{'id': atividade.id, 'nome': atividade.nome, 'pessoa': atividade.pessoa.nome} for atividade in atividades]
        return response

    def post(self) -> json:
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'id': atividade.id,
            'nome': atividade.nome,
            'pessoa': atividade.pessoa.nome
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(LitarPessoas, '/pessoas/')
api.add_resource(ListarAtividade, '/atividades/')


if __name__ == '__main__':
    app.run(debug=True)
