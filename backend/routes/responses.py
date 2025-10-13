from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Response

responses_bp = Blueprint("responses", __name__)

@responses_bp.route("/", methods=["POST"])
def submit_response():
    data = request.json
    response = Response(form_id=data["form_id"], answers=data["answers"])
    db.session.add(response)
    db.session.commit()
    return jsonify({"message": "Response saved"}), 201

@responses_bp.route("/<int:form_id>", methods=["GET"])
def get_responses(form_id):
    responses = Response.query.filter_by(form_id=form_id).all()
    return jsonify([{
        "id": r.id,
        "answers": r.answers,
        "submitted_at": r.submitted_at.isoformat()
    } for r in responses])
