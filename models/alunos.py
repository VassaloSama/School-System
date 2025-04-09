from app import alunos, turmas

class Alunos:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = float(nota_primeiro_semestre)
        self.nota_segundo_semestre = float(nota_segundo_semestre)
        self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    @staticmethod
    def criar_aluno(dados):
        campos_obrigatorios = [
            "id", "nome", "idade", "turma_id",
            "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre"
        ]
        for campo in campos_obrigatorios:
            if campo not in dados:
                raise ValueError(f"Campo {campo} é obrigatório!")

        id = dados["id"]
        if id in alunos:
            raise ValueError("Aluno com esse ID já existe!")

        if dados["turma_id"] not in turmas:
            raise ValueError("Turma não encontrada!")

        nota1 = float(dados["nota_primeiro_semestre"])
        nota2 = float(dados["nota_segundo_semestre"])
        media_final = (nota1 + nota2) / 2

        novo_aluno = {
            "id": id,
            "nome": dados["nome"],
            "idade": dados["idade"],
            "turma_id": dados["turma_id"],
            "data_nascimento": dados["data_nascimento"],
            "nota_primeiro_semestre": nota1,
            "nota_segundo_semestre": nota2,
            "media_final": media_final
        }

        alunos[id] = novo_aluno
        return novo_aluno

    @staticmethod
    def listar_alunos():
        return list(alunos.values())

    @staticmethod
    def obter_aluno(id):
        return alunos.get(id)

    @staticmethod
    def atualizar_aluno(id, dados):
        if id not in alunos:
            raise ValueError("Aluno não encontrado!")

        aluno = alunos[id]

        if "nome" in dados:
            aluno["nome"] = dados["nome"]
        if "idade" in dados:
            aluno["idade"] = dados["idade"]
        if "turma_id" in dados:
            if dados["turma_id"] not in turmas:
                raise ValueError("Turma não encontrada!")
            aluno["turma_id"] = dados["turma_id"]
        if "data_nascimento" in dados:
            aluno["data_nascimento"] = dados["data_nascimento"]
        if "nota_primeiro_semestre" in dados:
            aluno["nota_primeiro_semestre"] = float(dados["nota_primeiro_semestre"])
        if "nota_segundo_semestre" in dados:
            aluno["nota_segundo_semestre"] = float(dados["nota_segundo_semestre"])

        # Recalcula a média final
        nota1 = aluno.get("nota_primeiro_semestre", 0)
        nota2 = aluno.get("nota_segundo_semestre", 0)
        aluno["media_final"] = (nota1 + nota2) / 2

        return aluno

    @staticmethod
    def deletar_aluno(id):
        if id not in alunos:
            raise ValueError("Aluno não encontrado!")
        del alunos[id]
