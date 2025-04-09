from app import turmas, professores

class Turmas:
    def __init__(self, id, descricao, professor_id, ativo):
        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    @staticmethod
    def criar_turma(dados):
        for campo in ["id", "descricao", "professor_id", "ativo"]:
            if campo not in dados:
                raise ValueError(f"Campo {campo} é obrigatório!")

        id = dados["id"]
        if id in turmas:
            raise ValueError("Turma com esse ID já existe!")

        if dados["professor_id"] not in professores:
            raise ValueError("Professor não encontrado!")

        nova_turma = {
            "id": id,
            "descricao": dados["descricao"],
            "professor_id": dados["professor_id"],
            "ativo": dados["ativo"]
        }

        turmas[id] = nova_turma
        return nova_turma

    @staticmethod
    def listar_turmas():
        return list(turmas.values())

    @staticmethod
    def obter_turma(id):
        return turmas.get(id)

    @staticmethod
    def atualizar_turma(id, dados):
        if id not in turmas:
            raise ValueError("Turma não encontrada!")

        turma = turmas[id]

        if "descricao" in dados:
            turma["descricao"] = dados["descricao"]
        if "professor_id" in dados:
            if dados["professor_id"] not in professores:
                raise ValueError("Professor não encontrado!")
            turma["professor_id"] = dados["professor_id"]
        if "ativo" in dados:
            turma["ativo"] = dados["ativo"]

        return turma

    @staticmethod
    def deletar_turma(id):
        if id not in turmas:
            raise ValueError("Turma não encontrada!")
        del turmas[id]