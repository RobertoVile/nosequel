import pymongo
import pymongo.errors
import config

def mostrar_seguidor():
    try:
        while True:
            # Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Usuários"]

            # Busca o usuário logado
            usuario = colecao.find_one({"Email": config.EM, "Senha": config.SE})
            
            if usuario:
                # Obtém a lista de seguidores
                retornar_seguidor = usuario.get("Seguidores", [])

                if not retornar_seguidor:
                    print("Você não tem seguidores.")
                    return

                # Exibe os seguidores
                for resultado in retornar_seguidor:
                    print(resultado)
            else:
                print("Usuário não encontrado!")
              
    except pymongo.errors.PyMongoError as e:
        print(f"Erro: {e}")
