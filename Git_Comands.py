import subprocess
import os

def git_push ():   
    subprocess.run('git status', check=True, shell=True) 
    subprocess.run('git add .', check=True, shell=True)
    # Obtendo a escolha do usuário
    choice = input("Digite a Mensagem de Commit: ")
    subprocess.run(f'git commit -m "{choice}"', check=True, shell=True)
    subprocess.run('git pull origin main', check=True, shell=True)
    subprocess.run('git push origin main', check=True, shell=True)

def show_menu():
    while True:
        # Menu de opções
        print("\nEscolha uma opção:")
        print("1 - Git Push")
        print("2 - Sair")
        
        # Obtendo a escolha do usuário
        choice = input("Digite a opção desejada: ")
        
        if choice == '1':
            status = git_push()
        elif choice == '2':
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue
        
        # Espera o usuário pressionar uma tecla para sair
        input("\nPressione qualquer tecla para continuar")
        

if __name__ == "__main__":
    show_menu()
