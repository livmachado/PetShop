from cliente import Cliente
from adocao import Adocao
class View(Cliente, Adocao):
    def __init__(self):
        Cliente.__init__(self)
        Adocao.__init__(self)
        self.position = ''
        
        

    
    
    def view(self):
        print('\n-Bem vindo a Pet Shop-\n')
        self.cli_fun()
        if self.position == 'Funcionário':
            # Função Funcionario entra aqui!!!
            pass
        if self.position == 'Cliente':
            self.verificaCadastro()
        if self.type_service == 'Serviços':
            # Função Serviços entra aqui!!!
            pass
        if self.type_service == 'Produtos':
            # Função Produtos entra aqui!!!
            pass
        if self.type_service == 'Adoção':
            self.menu()
            self.clien()
        if self.type_service == 'Encerrar':
            pass

    def cli_fun(self):
        while True:
            try:
                position = int(input('Voce é:\n 1-Funcionario \n 2-Cliente \nInforme o número da posição: '))
                if position == 1:
                    self.position= 'Funcionário'
                    break
                elif position == 2:
                    self.position = 'Cliente'
                    break
                else:
                    print('Número Invalido')
                
            except ValueError:
                print('Posição invalidada')

    def __str__(self):
        if self.position == 'funcionario':
            return f'Posição: {self.position} Cargo: {self.post}'
        else:
            return f'Posição: {self.position} Serviço: {self.type_service}'

a=View()
a.view()
                
