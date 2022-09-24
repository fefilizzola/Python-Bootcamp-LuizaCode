# 4. Crie um professor de classe com atributos nome, idade e salário, onde
# o salário deve ter um método privado que não pode ser acessado fora da classe.
# a. Crie um método para acessar o método privado, onde é passada a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self,nome,idade,salario):
        self.nome=nome
        self.idade=idade
        self.__salario=salario
        
    def __retorna_salario(self):
        return self.__salario
    
    def acessa_salario(self,cargo):
        if cargo=='Diretor':
            return self.__retorna_salario()
        return "Usuário não autorizado"
        
proff=Professor("Ze",40,1000)
print("Diretor: ",proff.acessa_salario("Diretor"))
print("Colega de trabalho: ", proff.acessa_salario("Colega"))

