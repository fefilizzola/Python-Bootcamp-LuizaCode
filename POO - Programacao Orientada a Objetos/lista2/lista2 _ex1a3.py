# Dada as seguintes informações: Pessoa, cpf, nome e idade:
# crie uma classe onde teremos o retorno do documento, o retorno do nome e verificação de tipo de pessoa, onde um método irá receber como parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.

class Pessoa:
    def __init__(self,cpf,nome,idade):
        #self.pessoa=''
        self.cpf=cpf
        self.nome=nome
        self.idade=idade
        #self.pessoa=pessoa
        
    def smoker(self):
        fum=0
        while fum==0:
            smoker=input('Por favor informe "S" se a pessoa for fumante e "N" se não:')
            if smoker!='S' and smoker!='s' and smoker != 'n' and smoker !='N':
                print('Erro')
                continue
            fum=1
            
        if smoker == 'S' or smoker == 's':
            smoker='Fumante'
            
        smoker='Não Fumante'
        return f'Usuário: {self.nome} \nIdade:{self.idade} \n{smoker}'
                
# Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
# exclusivo para a classe e acesse-o

class PessoaFisica(Pessoa):
    def __init__(self,cpf,nome,idade,pessoa):
        super().__init__(cpf,nome,idade)
        self.pessoa=pessoa
    def fisica(self):
        if self.pessoa=='Física':
            return f'\nPessoa Física \nCPF:{self.cpf}'
 
# Escreva uma classe “PessoaJurica” e herde Pessoa, agora
# modificando o comportamento, retorne o cnpj. Crie uma instância e
# acesse os dados

def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper


class PessoaJuridica(Pessoa):
    def __init__(self,cpf,nome,idade,pessoa):
        super().__init__(cpf,nome,idade)
        self.pessoa=pessoa
    
    def decorator(foo):
        def magic(self):
            print('CNPJ:')
            foo(self)
            print('Fim')
        return magic
    
    @decorator
    def cnpj(self):
        if self.pessoa=='Jurídica':
            print(f'{self.cpf}')

       
pessoa=input('Insira o tipo de pessoa [Física/Jurídica]:')       
maria=Pessoa(11290,'Maria',10)
print(maria.smoker())
pf=PessoaFisica(1000,'Maria',10,pessoa)
print(pf.fisica())
pj=PessoaJuridica(10000,'Maria',10,pessoa)
print(pj.cnpj())