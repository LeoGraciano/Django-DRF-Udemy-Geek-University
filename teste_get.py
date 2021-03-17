import requests


urls_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"
urls_base_cursos = "http://localhost:8000/api/v2/cursos/"

headers = {'Authorization': 'Token 5efcdce34685689f616e3deb24cdc86be99ad897'}

# resultado = requests.get(url=urls_base_avaliacoes, headers=headers)
resultado = requests.get(url=urls_base_cursos, headers=headers)

print(resultado.json()['results'][0]['id'])
# Testando se o endpoint esta correto
assert resultado.status_code == 200

# testando elemento das lista pegar qualquer elemento do dicionárioe usar para teste
assert resultado.json()
# print(resultado.json())
