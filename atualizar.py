import pymongo
import pymongo.errors

def atualizar():
    try:
        while True:
            # Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Loja_Zé_Caveira"]
            colecao = banco["PRODUTOS"]

            #Pergunta as informações necessárias para a alteração
            nome = input("Qual é o nome do produto que deseja consultar: ")
            alterar = input("O que você deseja alterar nesse produto (ex.: 'Nome', 'Preco' e etc.)? ")
            novo_valor = input(f"Qual o novo valor para '{alterar}'? ")

            #Realização da atualização
            resultado = colecao.update_one({"Nome": nome}, {"$set": {alterar: novo_valor}})
            print("Atualização concluída!")
            
            # Verificação do resultado da atualização
            if resultado.matched_count == 0:
                print(f"Nenhum produto com o nome '{nome}' foi encontrado.")
            elif resultado.modified_count == 0:
                print(f"O valor para '{alterar}' já era '{novo_valor}'. Nenhuma alteração foi feita.")
            else:
                print("Atualização concluída com sucesso!")

            
            op = input("Deseja continuar? (Qualquer valor para sim e 0 para não: )")
            if op == '0':
                print("Saindo...")
                return
            
    except pymongo.errors.PyMongoError as e:
        print("Deu erro:", e)