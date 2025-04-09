from app import turmas, professores

class Turmas:
    def __init__(self, id, descricao, professor_id, ativo):
        if professor_id not in professores:
            raise ValueError("Professor não encontrado!")

        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

        turmas[id] = {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }
    
    def serialize(self):
        return turmas[self.id]