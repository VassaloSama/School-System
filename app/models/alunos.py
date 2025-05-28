from config import db
from models.turmas import Turmas
from datetime import datetime

class Alunos(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento.strftime('%d/%m/%Y'),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

    @staticmethod
    def criar_aluno(dados):
        campos = [
            "id", "nome", "idade", "turma_id",
            "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre"
        ]
        for campo in campos:
            if campo not in dados:
                raise ValueError((f"Campo {campo} é obrigatório!"), 400)

        if Alunos.query.get(dados["id"]):
            raise ValueError(("Aluno com esse ID já existe!"), 400)

        if not Turmas.query.get(dados["turma_id"]):
            raise ValueError(("Turma não encontrada!"), 400)

        nota1 = float(dados["nota_primeiro_semestre"])
        nota2 = float(dados["nota_segundo_semestre"])
        media = (nota1 + nota2) / 2

        try:
            data_nasc = datetime.strptime(dados["data_nascimento"], "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Formato de data inválido! Use dd-mm-aaaa", 400)

        novo_aluno = Alunos(
            id=dados["id"],
            nome=dados["nome"],
            idade=dados["idade"],
            turma_id=dados["turma_id"],
            data_nascimento=data_nasc,
            nota_primeiro_semestre=nota1,
            nota_segundo_semestre=nota2,
            media_final=media
        )

        db.session.add(novo_aluno)
        db.session.commit()
        return novo_aluno.serialize()

    @staticmethod
    def listar_alunos():
        return [aluno.serialize() for aluno in Alunos.query.all()]

    @staticmethod
    def obter_aluno(id):
        aluno = Alunos.query.get(id)
        return aluno.serialize() if aluno else None

    @staticmethod
    def atualizar_aluno(id, dados):
        aluno = Alunos.query.get(id)
        if not aluno:
            raise ValueError(("Aluno não encontrado!"), 404)

        if "nome" in dados:
            aluno.nome = dados["nome"]
        if "idade" in dados:
            aluno.idade = dados["idade"]
        if "turma_id" in dados:
            if not Turmas.query.get(dados["turma_id"]):
                raise ValueError("Turma não encontrada!", 400)
            aluno.turma_id = dados["turma_id"]
        if "data_nascimento" in dados:
            try:
                aluno.data_nascimento = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Formato de data inválido! Use dd/mm/aaaa", 400)
        if "nota_primeiro_semestre" in dados:
            aluno.nota_primeiro_semestre = float(dados["nota_primeiro_semestre"])
        if "nota_segundo_semestre" in dados:
            aluno.nota_segundo_semestre = float(dados["nota_segundo_semestre"])

        # Recalcular média
        nota1 = Alunos.nota_primeiro_semestre or 0
        nota2 = Alunos.nota_segundo_semestre or 0
        Alunos.media_final = (nota1 + nota2) / 2

        db.session.commit()
        return Alunos.serialize()

    @staticmethod
    def deletar_aluno(id):
        aluno = Alunos.query.get(id)
        if not aluno:
            raise ValueError(("Aluno não encontrado!"), 404)
        db.session.delete(aluno)
        db.session.commit()
