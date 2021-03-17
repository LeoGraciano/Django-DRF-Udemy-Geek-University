import requests


urls_base_avaliacoes = "http://localhost:8000/api/v2/avaliacoes/"
urls_base_cursos = "http://localhost:8000/api/v2/cursos/"

# token admim 5efcdce34685689f616e3deb24cdc86be99ad897

# token user: 0a821e60af139ff4bffe887ae359c3d7a20eaed8

headers = {'Authorization': 'Token 5efcdce34685689f616e3deb24cdc86be99ad897'}


resultado = requests.delete(url=f'{urls_base_cursos}4/', headers=headers)

# resultado em código HTTP é 204
assert resultado.status_code == 204

# Testando ver ser a resultado voltou zerado
assert len(resultado.text) == 0
