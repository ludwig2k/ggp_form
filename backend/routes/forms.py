from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Form

forms_bp = Blueprint("forms", __name__)

@forms_bp.route("/", methods=["GET"])
def get_forms():
    forms = Form.query.all()
    return jsonify([{
        "id": f.id,
        "title": f.title,
        "description": f.description,
        "questions": f.questions
    } for f in forms])

@forms_bp.route("/", methods=["POST"])
def create_form():
    data = request.json
    form = Form(
        title=data["title"],
        description=data.get("description", ""),
        questions=data.get("questions", [])
    )
    db.session.add(form)
    db.session.commit()
    return jsonify({"message": "Form created", "id": form.id}), 201

@forms_bp.route("/<int:form_id>", methods=["GET"])
def get_form(form_id):
    form = Form.query.get_or_404(form_id)
    return jsonify({
        "id": form.id,
        "title": form.title,
        "description": form.description,
        "questions": form.questions
    })
