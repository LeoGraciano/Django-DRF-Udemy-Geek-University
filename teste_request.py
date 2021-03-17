import requests

headers = {'Authorization': 'Token 5efcdce34685689f616e3deb24cdc86be99ad897'}

# GET AVALIAÇÕES
avaliacoes = requests.get(
    url="http://localhost:8000/api/v2/avaliacoes/")

# Acessando os dados da resposta
# print(avaliacoes.json())

# # Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# # # acessando a proxima pagina de resultados
# print(avaliacoes.json()['next'])

# # # acessand oo resultado das paginas
# print(avaliacoes.json()['results'])

# # # acessando o primeiro item da lista
# print(avaliacoes.json()['results'][0])


cursos = requests.get(
    url="http://localhost:8000/api/v2/cursos/", headers=headers)


print(cursos.json())
