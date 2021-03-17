import requests


urls_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"
urls_base_cursos = "http://localhost:8000/api/v2/cursos/"

# token admim 5efcdce34685689f616e3deb24cdc86be99ad897

# token user: 0a821e60af139ff4bffe887ae359c3d7a20eaed8

headers = {'Authorization': 'Token 0a821e60af139ff4bffe887ae359c3d7a20eaed8'}

new_data = {
    "titulo": "Gerencia de Ágil de projetos com Scrum",
    "url": "https://Tesfate.com.arroz"
}


# resultado = requests.get(url=urls_base_avaliacoes, headers=headers)
resultado = requests.post(url=urls_base_cursos, headers=headers, data=new_data)


# Testando se o endpoint esta correto na criação status_code 201
assert resultado.status_code == 201

# testando elemento das lista pegar qualquer elemento do dicionárioe usar para teste
assert resultado.json()

# Teste ver se o dados criado foram certo se o titulo é igual
assert resultado.json()['titulo'] == new_data['titulo']
