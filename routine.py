ROUTINE = [
    # /authenticator/apptoken
    # Chamada de AppToken, deve retornar 400 devido à falta do parâmetro do app_token
    {'verb': 'GET', 'path': 'authenticator', 'method': 'apptoken', 'headers': { 'Content-type': 'application/json'},
     'return_code': 400, 'description': 'Faltando parâmetros.'},
    # Chamada de AppToken, deve retornar 401 devido app_token estar inválido
    {'verb': 'GET', 'path': 'authenticator', 'method': 'apptoken', 'headers': { 'Content-type': 'application/json',
    'app_token': 'abcdefghijklmnopqrstuvwxyz'}, 'return_code': 401, 'description': 'app_token Inválido.'},
    # Chamada de AppToken, deve retornar 200 devido app_token estar válido
    {'verb': 'GET', 'path': 'authenticator', 'method': 'apptoken', 'headers': { 'Content-type': 'application/json',
    'app_token': 'Yl{WVff@7GQ5eD])PTz#V2w8pM5B59'}, 'return_code': 200, 'description': 'app_token válido.'},

    # Chamada de Login, deve retornar 400 devido à falta do parâmetro do app_token
    {'verb': 'POST', 'path': 'authenticator', 'method': 'login', 'headers': { 'Content-type': 'application/json'},
    'body': {'username': 'test', 'email': 'test@test.com', 'password': '1234'}, 'return_code': 400,
    'description': 'Faltando parâmetros.'},
    # Chamada de Login, deve retornar 401 devido app_token estar inválido
    {'verb': 'POST', 'path': 'authenticator', 'method': 'login', 'headers': { 'Content-type': 'application/json',
    'app_token': 'abcdefghijklmnopqrstuvwxyz'}, 'body': {'username': 'test', 'email': 'test@test.com',
    'password': '1234'}, 'return_code': 401, 'description': 'app_token Inválido.'},
    # Chamada de Login, deve retornar 200 e o auth_token
    {'verb': 'POST', 'path': 'authenticator', 'method': 'login', 'headers': { 'Content-type': 'application/json'},
    'body': {'username': 'test', 'email': 'test@test.com', 'password': '1234'}, 'return_code': 200,
    'description': 'Sucesso no login.'},
    # Chamada com Login que não existe, deve retornar 404
     {'verb': 'POST', 'path': 'authenticator', 'method': 'login', 'headers': { 'Content-type': 'application/json'},
     'body': {'username': 'test', 'email': 'test@test.com', 'password': '1234'}, 'return_code': 404,
     'description': 'Usuário não encontrado.'}
]
