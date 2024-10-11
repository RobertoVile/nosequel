import pymongo
import pymongo.errors
import funcoes_principais
import config

def logar():
    while True:
        try:
            # Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Usuários"]

            config.EM = input("Digite seu email: ")
            config.SE = input("Digite sua senha: ")

            log = colecao.find_one({"Email": config.EM, "Senha": config.SE})
 
            if log:
                print("Login Feito!")
                funcoes_principais.principal()
            else:
                print("Credenciais não encontradas. Verifique seu email e senha.")
                return
           
        except pymongo.errors.PyMongoError as e:
            print(e)




