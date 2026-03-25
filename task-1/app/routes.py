from flask import Blueprint, request, jsonify
from flask import render_template
from .models import Student
from .db import db
import logging

student_bp = Blueprint("students", __name__)
logger = logging.getLogger(__name__)

# CREATE
@student_bp.route("/", methods=["POST"])
def create_student():
    data = request.json
    student = Student(**data)
    db.session.add(student)
    db.session.commit()
    logger.info("Student created")
    return jsonify(student.to_dict()), 201

# READ ALL
@student_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])

# READ ONE
@student_bp.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

# UPDATE
@student_bp.route("/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json

    student.name = data.get("name", student.name)
    student.age = data.get("age", student.age)
    student.email = data.get("email", student.email)

    db.session.commit()
    logger.info(f"Student {id} updated")
    return jsonify(student.to_dict())

# DELETE
@student_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    logger.warning(f"Student {id} deleted")
    return "", 204

# Healthcheck
@student_bp.route("/healthcheck")
def healthcheck():
    return {"status": "ok"}, 200

@student_bp.route("/ui", methods=["GET"])
def ui():
    return render_template("index.html")