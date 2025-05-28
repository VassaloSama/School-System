# School-System
Estudo de API RESTful para gestão de escolas


# API School-System

API desenvolvida com Flask e SQLAlchemy para gerenciamento de professores, turmas e alunos, seguindo o padrão MVC. Ideal para instituições que desejam controlar o cadastro de professores, alunos e suas turmas

## 🛠️ Tecnologias

- Python 3
- Flask
- SQLAlchemy
- MySQL
- Flasgger (Swagger UI)

## 📁 Estrutura

```
app/
├── app.py #Ponto de entrada da aplicação Flask
├── config.py #Configurações de ambiente e banco de dados
├── models/
│ ├── alunos.py # Model de Alunos
│ ├── turmas.py # Model de Turmas
| └── professores.py # Model de Professores
├── controller/
│ ├── sala.py # Controller de Alunos
│ ├── turma.py # Controller de Turmas
│ └── reserva.py # Controller de Professores
```

## ⚙️ Configuração

### Banco de Dados

A aplicação utiliza MySQL. O arquivo `config.py` já possui um exemplo de conexão via `pymysql`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:SenhaForte123@db:3306/school-system"
```
⚠️ Altere as credenciais e host conforme seu ambiente.

## 🔌 Endpoints
### ALUNOS
GET /alunos - Lista todos os alunos.

GET /alunos/<span style="color:blue">{id}</span> - Retorna os dados de um aluno.

POST /alunos - Cria um novo aluno.

PUT /alunos/<span style="color:blue">{id}</span> - Atualizar um aluno existente.

DELETE /alunos/<span style="color:blue">{id}</span> - Deletar um aluno existente.

### TURMAS
GET /turmas - Lista todas as turmas.

GET /turmas/<span style="color:blue">{id}</span> - Retorna os dados de uma turma.

POST /turmas - Cria uma nova turma.

PUT /turmas/<span style="color:blue">{id}</span> - Atualizar uma turma existente.

DELETE /turmas/<span style="color:blue">{id}</span> - Deletar uma turma existente.


### PROFESORES
GET /professores - Lista todos os professores.

GET /professores/<span style="color:blue">{id}</span> - Retorna os dados de um professor.

POST /professores - Cria um novo professor.

PUT /professores/<span style="color:blue">{id}</span> - Atualizar um professor existente.

DELETE /professores/<span style="color:blue">{id}</span> - Deletar um professor existente.

### RESETAR
POST /resetar
Reseta todos os dados de alunos, turmas e professores do banco


📌 Observações
Swagger UI está disponível em /apidocs (habilitado por padrão com Flasgger).


# 🛜 Integrações
#### API Reservation-System
repositório: https://github.com/GabrielCecconi25/Reservation-System

#### API Activity-System
repositório: https://github.com/VassaloSama/Activity_system