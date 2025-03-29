class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print (obj)

aluno_1 = Estudante("Guilherme", 56451)
aluno_2 = Estudante("Giovanna", 17323)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_1.matricula = 22222
aluno_3 = Estudante("Chappie", 33333)
mostrar_valores(aluno_1, aluno_2, aluno_3)