import pymongo
import pymongo.errors

def criar_livros():
    try:
        
        while True:
            #Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Livros"]

            #Pede as informações do produto
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            genero = input("Digite o gênero do livro: ")
            editora = input("Digite a editora do livro: ")
            avaliacoes = {"Curtidas": 0,
                "Comentarios": 0,
                "Salvamentos": 0}
            
            
            #Cria e insere as informações do do produto no documento
            documento_exemplo1 = {f"Título": titulo,"Autor": autor, "Gênero":genero, "Editora":editora,"Avaliações":avaliacoes}
            inserir = colecao.insert_one(documento_exemplo1).inserted_id
            print("Documento inserido!")
            
            #Verificação de coninuacão
            op = input("Deseja continuar? (Qualquer valor para sim e 0 para não: )")
            if op == '0':
                print("Saindo...")
                return


    except pymongo.errors as e:
        print("Deu erro:",e)
criar_livros()