import bson.objectid
import pymongo
import pymongo.errors
import config
import bson
def deixa_seguir():
    try:
        while True:
            # Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Usuários"]

            pessoa = input("Digite o nome de usuário da pessoa que deseja parar de seguir: ")

            usuario = colecao.find_one({"Email": config.EM, "Senha": config.SE})

            usuario_para_deixar_de_seguir = colecao.find_one({"Nome": pessoa})

            if not usuario_para_deixar_de_seguir:
                print("Você não está seguindo este usuário ou ele não existe!")
                return    
            
            remover_seguindo =  colecao.update_one({"_id": usuario["_id"]},{"$pull":{"Seguindo":bson.ObjectId(usuario["_id"])}})

            if remover_seguindo:
                print("Usuário removido de sua lista de seguidores!")
                remover_seguidor =  colecao.update_one({"_id": usuario_para_deixar_de_seguir["_id"]},{"$pull":{"Seguidores":bson.ObjectId(usuario_para_deixar_de_seguir["_id"])}})
                return

    except pymongo.errors.PyMongoError as e:
        print(f"Erro: {e}")
