import requests


urls_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"
urls_base_cursos = "http://localhost:8000/api/v2/cursos/"

# token admim 5efcdce34685689f616e3deb24cdc86be99ad897

# token user: 0a821e60af139ff4bffe887ae359c3d7a20eaed8

headers = {'Authorization': 'Token 5efcdce34685689f616e3deb24cdc86be99ad897'}

update_data = {
    "titulo": "Gerencia de Ágil de projetos com Scrum",
    "url": "https://Testee.com.arroz"
}


resultado = requests.put(
    url=f'{urls_base_cursos}1/', headers=headers, data=update_data)

# resultado = requests.get(
#     url=f'{urls_base_cursos}1/', headers=headers, data=update_data)

print(resultado.json())

# Testando se o endpoint esta correto na criação status_code 200
assert resultado.status_code == 200

# Teste ver se o dados criado foram certo se o titulo é igual
assert resultado.json()['titulo'] == update_data['titulo']
