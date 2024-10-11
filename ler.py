import pymongo
import pymongo.errors

def ler():
    try:
        while True:
            # Conexão com o cluster, banco e coleção
            conexao = pymongo.MongoClient("mongodb+srv://roberto:046345vile@cluster0.yjhg9.mongodb.net/")
            banco = conexao["Loja_Zé_Caveira"]
            colecao = banco["PRODUTOS"]
            #Prints
            print("1- Ver todos os documentos")
            print("2- Ver o documento com um preço especifico")

            #Pegando a Opção do Usuário
            op = input("Você deseja realizar qual tipo de consulta? ")

            #Verificação da opção 1
            if op == "1":
                ver_tudo = colecao.find()
                print("Documentos encontrados:")
                for documento in ver_tudo:
                    print(f"\n{documento}")  
            #Verificação para a opção 2    
            elif op == "2":
                op2 = input("Qual o preço do produto: ")
                ver_especifico = colecao.find({"Preço": op2})

                print(f"\nDocumentos encontrados com o preço:{op2}")

                for documento in ver_especifico:
                    print(documento)

            # Verificação de continuação
            op = input("Deseja continuar? (Qualquer valor para sim e 0 para não: )")
            if op == '0':
                print("Saindo...")
                return

                
    # Pega os erros
    except pymongo.errors.PyMongoError as e:  
        print("Deu erro:", e)
