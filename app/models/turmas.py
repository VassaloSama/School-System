from config import db
from models.professores import Professores

class Turmas(db.Model):
    __tablename__ = 'turmas'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    professor = db.relationship('Professores', backref=db.backref('turmas', lazy=True))

    def serialize(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo,
            "professor": self.professor.serialize() if self.professor else None
        }

    @staticmethod
    def criar_turma(dados):
        for campo in ["id", "descricao", "professor_id", "ativo"]:
            if campo not in dados:
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)

        if Turmas.query.get(dados["id"]):
            raise ValueError(("Turma com esse ID já existe!"), 400)
        
        professor = Professores.query.get(dados["professor_id"])
        if not professor:
            raise ValueError(("Professor não encontrado!"), 404)

        nova_turma = Turmas(
            id=dados["id"],
            descricao=dados["descricao"],
            professor_id=dados["professor_id"],
            ativo=dados["ativo"]
        )

        db.session.add(nova_turma)
        db.session.commit()
        return nova_turma.serialize()

    @staticmethod
    def listar_turmas():
        return [turma.serialize() for turma in Turmas.query.all()]

    @staticmethod
    def obter_turma(id):
        turma = Turmas.query.get(id)
        return turma.serialize() if turma else None

    @staticmethod
    def atualizar_turma(id, dados):
        if not any(campo in dados for campo in ["descricao", "professor_id", "ativo"]):
            raise ValueError(("Dados Inválidos!"), 400)

        turma = Turmas.query.get(id)

        if not turma:
            raise ValueError(("Turma não encontrada!"), 404)

        if "descricao" in dados:
            turma.descricao = dados["descricao"]
        if "professor_id" in dados:
            if not Professores.query.get(dados["professor_id"]):
                raise ValueError(("Professor não encontrado!"), 404)
            turma.professor_id = dados["professor_id"]
        if "ativo" in dados:
            turma.ativo = dados["ativo"]

        db.session.commit()
        return turma

    @staticmethod
    def deletar_turma(id):
        turma = Turmas.query.get(id)
        if not turma:
            raise ValueError(("Turma não encontrada!"), 404)
        db.session.delete(turma)
        db.session.commit()