from models import Usuarios, Pessoas


def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consultar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


def inserir_pessoa(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()


def consultar_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)


if __name__ == '__main__':
    # inserir_usuario('marcos', '@Senha3231')
    # inserir_usuario('maia', '637485tfs')
    consultar_usuarios()
