professores = {}

class Professores:
    def __init__(self, id, nome, idade, materia):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia

    @staticmethod
    def criar_professor(dados):
        for campo in ["id", "nome", "idade", "materia"]:
            if campo not in dados:
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)

        id = dados["id"]
        if id in professores:
            raise ValueError(("Professor com esse ID já existe!"), 400)

        novo_professor = {
            "id": id,
            "nome": dados["nome"],
            "idade": dados["idade"],
            "materia": dados["materia"]
        }
        professores[id] = novo_professor
        return novo_professor

    @staticmethod
    def listar_professores():
        return list(professores.values())

    @staticmethod
    def obter_professor(id):
        return professores.get(id)

    @staticmethod
    def atualizar_professor(id, dados):
        if not any(campo in dados for campo in ["nome", "idade", "materia"]):
            raise ValueError(("Dados Inválidos!"), 400)

        if id not in professores:
            raise ValueError(("Professor não encontrado!"), 404)

        professor = professores[id]
        if "nome" in dados:
            professor["nome"] = dados["nome"]
        if "idade" in dados:
            professor["idade"] = dados["idade"]
        if "materia" in dados:
            professor["materia"] = dados["materia"]

        return professor

    @staticmethod
    def deletar_professor(id):
        if id not in professores:
            raise ValueError(("Professor não encontrado!"), 404)
        del professores[id]