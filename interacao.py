import pymongo
import pymongo.errors
def escolha_interacao():
    try:
        while True:
                # Conexão com o cluster, banco e coleção
                conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
                banco = conexao["Biblioteca_Sacramento"]
                colecao = banco["Livros"]
                colecaoU = banco["Usuários"]

                escolha = input("Digite o nome do livro que deseja escolher: ")
                consulta = colecao.find({"Título": escolha})

                print("\n--- Escolhas ---")
                print("1. Curtir livro")
                print("2. Comentar livro")
                print("3. Salvar livro")
                print("4. Marcar livro como lido")
                print("5. Marcar livro como favorito")
                print("5. Sair")
                
                op = input("Insira sua opção: ")
                
                if op == '1':
                    colecao.update_one({"Título": escolha},{"$inc":{"Avaliações.0":1}})
    except pymongo.errors.PyMongoError as e:
         print(e)

