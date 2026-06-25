from main import app
from src.infra.database.connection import conection_db


@app.route("/nasa", methods=["GET"])
def nasa():
    if conection_db():
        print("Conexão feita com sucesso!")
    else:
        print("Erro ao conectar com o banco de dados!")

    return "API GET NASA"