from app import alunos, turmas

class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        if turma_id not in turmas:
            raise ValueError("Turma não encontrada!")

        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = float(nota_primeiro_semestre)
        self.nota_segundo_semestre = float(nota_segundo_semestre)
        self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

        alunos[id] = {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final
        }
    
    def serialize(self):
        return alunos[self.id]