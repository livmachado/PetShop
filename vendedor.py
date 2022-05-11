from funcionario import Funcionario

class Vendedor (Funcionario):
    
    def __init__ (self, nome, CPF, email):
        Funcionario.__init__(self,nome,CPF,email)
        self.valorVendas=0
         
    def registraVenda(self,valorVenda):
        self.valorVendas=self.valorVendas+valorVenda
        
                    
    def calculaSalario(self):
        self.salario=(self.CHMensal*20)+(self.valorVendas*0.05)
