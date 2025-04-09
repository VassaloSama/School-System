from models.professores import professores

turmas = {}

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
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)

        id = dados["id"]
        if id in turmas:
            raise ValueError(("Turma com esse ID já existe!"), 400)

        if dados["professor_id"] not in professores:
            raise ValueError(("Professor não encontrado!"), 404)

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
        if not any(campo in dados for campo in ["descricao", "professor_id", "ativo"]):
            raise ValueError(("Dados Inválidos!"), 400)

        if id not in turmas:
            raise ValueError(("Turma não encontrada!"), 404)

        turma = turmas[id]

        if "descricao" in dados:
            turma["descricao"] = dados["descricao"]
        if "professor_id" in dados:
            if dados["professor_id"] not in professores:
                raise ValueError(("Professor não encontrado!"), 404)
            turma["professor_id"] = dados["professor_id"]
        if "ativo" in dados:
            turma["ativo"] = dados["ativo"]

        return turma

    @staticmethod
    def deletar_turma(id):
        if id not in turmas:
            raise ValueError(("Turma não encontrada!"), 404)
        del turmas[id]