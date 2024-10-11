import pymongo
import pymongo.errors

def criar():
    try:
        
        while True:
            #Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Biblioteca_Sacramento"]
            colecao = banco["Usuários"]

            #Pede as informações do usuário
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            senha = input("Digite sua senha: ")
            livros_lidos = []
            livros_favoritos = []
            seguindo = []
            seguidores = []
            #Cria e insere as informações do usário no documento
            documento_usuario = {f"Nome": nome, "Email": email, "Senha": senha, "Livros_Lidos":livros_lidos, "Livros_Favoritos":livros_favoritos,"Seguindo:":seguindo, "Seguidores":seguidores}
            inserir = colecao.insert_one(documento_usuario).inserted_id
            print("Documento inserido!")
            
            #Verificação de coninuacão
            op = input("Deseja continuar? (Qualquer valor para sim e 0 para não: )")
            if op == '0':
                print("Saindo...")
                return


    except pymongo.errors as e:
        print("Deu erro:",e)

