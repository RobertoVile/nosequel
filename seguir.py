import pymongo
import pymongo.errors
import bson
import config

conexao = pymongo.MongoClient("mongodb://roberto:046345vile@cluster0.yjhg9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
banco = conexao["Biblioteca_Sacramento"]
colecao = banco["Usuários"]
               
def seguir_usuario():
    try:
            
        while True:
                #Conexão com o cluster, banco e coleção
                conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
                banco = conexao["Biblioteca_Sacramento"]
                colecao = banco["Usuários"]
               

                pessoa = input("Digite o nome de usuário da pessoa que deseja seguir: ")
                usuario = colecao.find_one({"Nome": pessoa})
                
                if usuario == None:
                     print("Usuário não encontrado!")
                     return                
                
                usuario_seguidor = colecao.find_one({"Email": config.EM, "Senha": config.SE})
                seguindo = colecao.update_one({"Email": config.EM, "Senha": config.SE},{"$addToSet": {"Seguindo": bson.ObjectId(usuario["_id"])}})
                
                
                # Verifica se o usuário já está seguindo a pessoa
                ja_seguindo = colecao.find_one({
                "Email": config.EM,
                "Senha": config.SE,
                "Seguindo": {"$in": [bson.ObjectId(usuario["_id"])]}
            })
                
                if ja_seguindo:
                     print(f"Você já segue {pessoa}")
                     return
                
                if seguindo:
                     print("Usuário seguido!")
                     seguidores = colecao.update_one({"Nome" : pessoa},{"$addToSet": {"Seguidores": bson.ObjectId(usuario_seguidor["_id"])}})
                     op = input("Deseja continuar?(0 para sim e qualquer valor para não) ")
                     if op == '0':
                          seguir_usuario()
                     else:
                          return
                else:
                     ("Nenhum usuário com esse nome!")
                
    except pymongo.errors.PyMongoError as e:
         print(e)
