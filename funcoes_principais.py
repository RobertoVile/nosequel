import pymongo
import pymongo.errors
import interacao
import seguir
import mostrar_seguidor
import deixar_de_seguir
def principal():
    try:
        while True:
            #Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Usuários"]

            print("\n--- Biblioteca Sacramento ---")
            print("1. Procurar Livro")
            print("2. Seguir outros usuários")
            print("3. Mostrar seguidores")
            print("4. Deixar de seguir")

            op = input("Escolha uma opção: ")

            if op == '1':
                interacao.escolha_interacao()
            elif op == '2':
                seguir.seguir_usuario()
            elif op == '3':
                mostrar_seguidor.mostrar_seguidor()
            elif op == '4':
                deixar_de_seguir.deixa_seguir()
            elif op == '5':
                print("Saindo...")
                return
            else:
                print("Opção inválida!")
                principal()

    except pymongo.errors.PyMongoError as e:
        print(e)
