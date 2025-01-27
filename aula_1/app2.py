lista_usuarios = [
    { "nome": "Alberto", "email": "alberto@gmail.com", "assinante": False },
    { "nome": "Gustavo", "email": "gustavo@gmail.com", "assinante": True },
    { "nome": "Mario", "email": "mario@gmail.com", "assinante": True },
    { "nome": "Lucas", "email": "lucas@gmail.com", "assinante": False },
    { "nome": "Marcela", "email": "marcela@gmail.com", "assinante": True },
    { "nome": "Maria", "email": "maria@gmail.com", "assinante": True }
]

"""
Exibir todos os email's da lista_usuarios.
"""

for i in lista_usuarios:
    print(i['email'])
    
    
"""
Exibir o nome de todos os usuarios da lista_usuario, 
quando o assinante for igual a False.

Para todos os usuarios, verificar se é assinante.
Caso sim, exibir o nome e uma mensagem de saudação.
Caso não, exibir o nome e uma mensagem de convite a participar da empresa.
"""

for i in lista_usuarios:
    if i['assinante'] == False:
        print(i['nome'], "Seja bem vindo!")     
    else:
        print(i['nome'], "Não deseja se tornar membro?")