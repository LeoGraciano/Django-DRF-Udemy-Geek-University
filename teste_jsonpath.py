import requests
import jsonpath as jp
from jsonpath import jsonpath


avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")


# Resultado de todos as avaliações
# resultados = jsonpath(avaliacoes.json(), 'results')

# pega a primeiro resultado
# primeiro = jsonpath(avaliacoes.json(), 'results[0]')

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')[0]

# Todas os nomes das pessoas que avaliram o curso
nomes = jsonpath(avaliacoes.json(), 'results[*].nome')

print(nomes)
