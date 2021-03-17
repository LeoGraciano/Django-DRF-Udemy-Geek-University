import requests

curso_id = ''


class TestCursos:
    headers = {'Authorization': 'Token 5efcdce34685689f616e3deb24cdc86be99ad897'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Novo Curso Teste",
            "url": "http://testedecriacao.com",
            'ativo': "True"
        }
        resposta = requests.post(
            url=self.url_base_cursos, headers=self.headers, data=novo)
        global curso_id
        curso_id = str(resposta.json()['id'])

        assert resposta.status_code == 201

    def test_put_curso(self):
        global curso_id
        new_data = {
            "titulo": "Atualização do Curso Teste",
            "url": "http://testedeupdate.com",
            'ativo': "True"
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}{curso_id}/', headers=self.headers, data=new_data)

        assert new_data['titulo'] == resposta.json()['titulo']

        assert resposta.status_code == 200

    def test_get_curso(self):
        global curso_id
        resposta = requests.get(
            url=f'{self.url_base_cursos}{curso_id}/', headers=self.headers)

        assert resposta.status_code == 200

    def test_delete_curso(self):
        global curso_id
        resposta = requests.delete(
            url=f'{self.url_base_cursos}{curso_id}/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
