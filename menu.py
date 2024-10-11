import criar_usuario
import login
import deletar
#Menu chamando as funções
def menu():
    while True:
        print("\n--- Biblioteca Sacramento ---")
        print("1. Criar conta")
        print("2. Logar")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_usuario.criar()
        elif escolha == '2':
             login.logar()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()