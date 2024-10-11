import pymongo
import pymongo.errors

def deletar():
    try:
        #Conexão com o cluster, banco e coleção
        conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
        banco = conexao["Loja_Zé_Caveira"]
        colecao = banco["PRODUTOS"]
        
        op = input("Digite o nome do produto que deseja deletar: ")
        
        
        colecao.delete_one({"Nome": op})

    except pymongo.errors as e:
        print("Deu erro", e)

