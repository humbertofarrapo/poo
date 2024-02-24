#Interface - Conjunto de classes abstratas e métodos abstratos;
from abc import ABC, abstractmethod 

#Classe - Classe abstrata;
class Pessoa(ABC): 
    def __init__(self, nome): 
        self.nome = nome 
    @abstractmethod 
    def saudacao(self): 
        pass

#Abstração - Classe - Herança;
class Aluno(Pessoa):
    #Encapsulamento;
    def __init__(self, nome, nota, media_instituicao): 
        super().__init__(nome) 
        self.nota = nota 
        self.media_instituicao = media_instituicao
    def avaliar(self): 
        if self.nota >= self.media_instituicao: 
            print(self.nome + ' passou.') 
        else: 
            print(self.nome + ' reprovou.') 
    def saudacao(self): 
            print('Olá, sou o(a) aluno(a) ' + self.nome + ' e serei avaliado(a).') 

#Classe - Herança - Polimorfismo;
class AlunoPosGraduacao(Aluno): 
    def __init__(self, nome, nota, media_instituicao, area_pesquisa): 
        super().__init__(nome, nota, media_instituicao) 
        self.area_pesquisa = area_pesquisa
    def avaliar(self): 
        if self.nota >= self.media_instituicao: 
            print(self.nome + ' passou na pós-graduação.') 
        else: 
            print(self.nome + ' reprovou na pós-graduação.')
            
#Objetos;
aluno1 = Aluno('João', 5.5, 6) 
aluno2 = AlunoPosGraduacao('Maria', 7, 6, 'Inteligência Artificial') 

#Mensagem;
aluno1.saudacao()
aluno2.saudacao()

print("\nResultado após as avaliações finais: ")

#Mensagem;
aluno1.avaliar() 
aluno2.avaliar()
