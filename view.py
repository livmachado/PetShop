from viewFuncionario import viewFuncionario


class view():
    def __init__(self):
        self.funcionarios=[]
        
    def menuPrincipal(self):
        while True:
            try:
                print("\n\n==== Escolha o Módulo ====\n\n")
                print("1-Funcionários")
                print("0-Sair")
                opt=int(input("Escolha a opção desejada:"))

                if(opt==1):
                    viewFuncionario().menuFuncionario()
                if(opt==0):
                    break
                if(opt>1 or opt<0):
                    print("Opção inválida")
            except ValueError:
                print("Opção inválida")

view().menuPrincipal()
