from flask_restful import Resource

lista_habilidades = [
    'Python', 'Delphi', 'Java', 'PHP', 'JavaScript', 'C#', 'Ruby', 'Sql', 'Git', 'HTML5', 'CSS3'
]

class Habilidades(Resource):
    def get(self) -> list:
        return lista_habilidades