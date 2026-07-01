from flask import Blueprint, request, session
from config import db
from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/signup")
def signup():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    if User.query.filter_by(username=data.get("username")).first():
        return {"error": "Username already exists"}, 400

    if User.query.filter_by(email=data.get("email")).first():
        return {"error": "Email already exists"}, 400

    user = User(
        username=data.get("username"),
        email=data.get("email")
    )

    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id

    return user.to_dict(), 201


@auth_bp.post("/login")
def login():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    user = User.query.filter_by(
        username=data.get("username")
    ).first()

    if not user or not user.check_password(data.get("password")):
        return {"error": "Invalid username or password"}, 401

    session["user_id"] = user.id

    return user.to_dict(), 200


@auth_bp.delete("/logout")
def logout():
    session.pop("user_id", None)
    return {}, 204


@auth_bp.get("/check_session")
def check_session():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    user = db.session.get(User, user_id)

    if not user:
        return {"error": "User not found"}, 404

    return user.to_dict(), 200