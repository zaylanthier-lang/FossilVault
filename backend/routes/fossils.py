from flask import Blueprint, request, session
from config import db
from models import Fossil

fossils_bp = Blueprint("fossils", __name__)


# GET all fossils for logged-in user
@fossils_bp.get("/api/fossils")
def get_fossils():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    fossils = Fossil.query.filter_by(user_id=user_id).all()

    return [f.to_dict() for f in fossils], 200


# CREATE a fossil
@fossils_bp.post("/api/fossils")
def create_fossil():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    if not data:
        return {"error": "Request body required"}, 400

    fossil = Fossil(
        name=data.get("name"),
        fossil_type=data.get("fossil_type"),
        geological_period=data.get("geological_period"),
        location_found=data.get("location_found"),
        date_found=data.get("date_found"),
        description=data.get("description"),
        image_url=data.get("image_url"),
        user_id=user_id
    )

    db.session.add(fossil)
    db.session.commit()

    return fossil.to_dict(), 201


# UPDATE a fossil
@fossils_bp.patch("/api/fossils/<int:id>")
def update_fossil(id):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    fossil = Fossil.query.filter_by(id=id, user_id=user_id).first()

    if not fossil:
        return {"error": "Fossil not found"}, 404

    data = request.get_json()

    if not data:
        return {"error": "Request body required"}, 400

    for key, value in data.items():
        if hasattr(fossil, key):
            setattr(fossil, key, value)

    db.session.commit()

    return fossil.to_dict(), 200


# DELETE a fossil
@fossils_bp.delete("/api/fossils/<int:id>")
def delete_fossil(id):
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    fossil = Fossil.query.filter_by(id=id, user_id=user_id).first()

    if not fossil:
        return {"error": "Fossil not found"}, 404

    db.session.delete(fossil)
    db.session.commit()

    return {}, 204