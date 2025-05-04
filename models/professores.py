from config import db

class Professores(db.Model):
    __tablename__ = 'professores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia
        }

    @staticmethod
    def criar_professor(dados):
        for campo in ["id", "nome", "idade", "materia"]:
            if campo not in dados:
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)

        if Professores.query.get(dados["id"]):
            raise ValueError(("Professor com esse ID já existe!"), 400)

        novo_professor = Professores(
            id=dados["id"],
            nome=dados["nome"],
            idade=dados["idade"],
            materia=dados["materia"]
        )
        db.session.add(novo_professor)
        db.session.commit()

        return novo_professor.serialize()

    @staticmethod
    def listar_professores():
        return [professor.serialize() for professor in Professores.query.all()]

    @staticmethod
    def obter_professor(id):
        professor = Professores.query.get(id)
        return professor.serialize() if professor else None

    @staticmethod
    def atualizar_professor(id, dados):
        if not any(campo in dados for campo in ["nome", "idade", "materia"]):
            raise ValueError(("Dados Inválidos!"), 400)

        professor = Professores.query.get(id)
        if not professor:
            raise ValueError(("Professor não encontrado!"), 404)

        if "nome" in dados:
            professor.nome = dados["nome"]
        if "idade" in dados:
            professor.idade = dados["idade"]
        if "materia" in dados:
            professor.materia = dados["materia"]

        db.session.commit()
        return professor.serialize()

    @staticmethod
    def deletar_professor(id):
        professor = Professores.query.get(id)
        if not professor:
            raise ValueError(("Professor não encontrado!"), 404)
        db.session.delete(professor)
        db.session.commit()