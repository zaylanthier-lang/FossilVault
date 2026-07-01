from flask import Blueprint, request
from models import ReferenceFossil

reference_bp = Blueprint("reference", __name__)


@reference_bp.get("/api/reference-fossils")
def get_reference_fossils():
    query = request.args.get("q")

    fossils_query = ReferenceFossil.query

    if query:
        fossils_query = fossils_query.filter(
            ReferenceFossil.common_name.ilike(f"%{query}%") |
            ReferenceFossil.fossil_type.ilike(f"%{query}%") |
            ReferenceFossil.geological_period.ilike(f"%{query}%")
        )

    fossils = fossils_query.all()

    return [f.to_dict() for f in fossils], 200


@reference_bp.get("/api/reference-fossils/<int:id>")
def get_reference_fossil(id):
    fossil = ReferenceFossil.query.get(id)

    if not fossil:
        return {"error": "Not found"}, 404

    return fossil.to_dict(), 200