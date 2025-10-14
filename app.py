from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.database import init_db, db
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from sqlalchemy import text 
import os, json

load_dotenv()

app = Flask(__name__)

# === Configuration ===
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev_secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# === Initialize extensions ===
jwt = JWTManager(app)
init_db(app)

# === Temporary route for Vue form submissions ===
@app.route("/api/form", methods=["POST"])
def receive_form():
    """
    Quick endpoint to receive survey responses from the Vue frontend.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado recebido"}), 400

    # Validate expected fields
    expected_fields = {
        "ferias", "outraFerias", "ponto", "outraPonto",
        "gratificacoes", "outraGratificacoes",
        "atestados", "outraAtestados",
        "licencas", "outraLicencas",
        "servidorExtra", "duvidaServidorExtra",
        "desligarServidor", "duvidaDesligarServidor",
        "esperaGGDP", "justificativaGGDP", "melhorias",
        "aposentadoria",  # New field
        "folhaPagamento",  # New field
        "nome"
    }

    # Log received data with better formatting
    print("\n📋 Formulário recebido:")
    for k, v in data.items():
        if k in expected_fields:
            print(f"- {k}: {v}")
        else:
            print(f"⚠️ Campo não esperado: {k}")

    try:
        user_name = data.get("nome", "Sem nome")
        form_data = {k: v for k, v in data.items() if k != "nome"}

        db.session.execute(
            text("INSERT INTO form_responses (user_name, data_json) VALUES (:user_name, :data_json)"),
            {
                "user_name": user_name,
                "data_json": json.dumps(form_data, ensure_ascii=False),
            },
        )
        db.session.commit()
        print("✅ Dados salvos com sucesso no banco")
    except Exception as e:
        print("⚠️ Erro ao salvar no banco:", e)
        return jsonify({"error": "Erro ao salvar dados"}), 500

    return jsonify({"message": "Formulário recebido com sucesso!"}), 200


# === Root health check ===
@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "Flask backend running", "version": "1.0"})



def create_table():
    with app.app_context():
        try:
            db.session.execute(text("""
                CREATE TABLE IF NOT EXISTS form_responses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    data_json TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """))
            db.session.commit()
            print("✅ Tabela form_responses verificada/criada (MySQL, com user_name).")
        except Exception as e:
            print("⚠️ Erro ao criar tabela:", e)


# Run this once when the app starts
create_table()

@app.route("/api/form/all", methods=["GET"])
def get_all_responses():
    from sqlalchemy import text
    import json

    try:
        rows = db.session.execute(text("""
            SELECT id, user_name, data_json, created_at
            FROM form_responses
            ORDER BY created_at DESC
        """)).fetchall()

        responses = [
            {
                "id": row.id,
                "user_name": row.user_name,
                "data": json.loads(row.data_json),
                "created_at": row.created_at.isoformat() if row.created_at else None
            }
            for row in rows
        ]

        return jsonify(responses), 200

    except Exception as e:
        print("⚠️ Erro ao buscar respostas:", e)
        return jsonify({"error": "Erro ao buscar respostas"}), 500


# === Entry point ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
