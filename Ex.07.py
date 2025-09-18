# 7. Login simples
# Peça um nome de usuário e uma senha. 
# Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.

usuario = input("digite o seu usuário: ")
senha = input("digite aqui a sua senha: ")
if usuario == "admin" and senha == "1234":
    print("usuario e senhas corretos")
else:
    print("usuário ou senha incorreto")