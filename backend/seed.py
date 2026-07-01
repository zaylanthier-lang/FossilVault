from app import app
from config import db
from models import ReferenceFossil

with app.app_context():

    db.drop_all()
    db.create_all()

    fossils = [
        ReferenceFossil(
            common_name="Trilobite",
            scientific_name="Phacops rana",
            fossil_type="Arthropod",
            geological_period="Devonian",
            description="Marine arthropods with segmented bodies.",
            image_url="",
            characteristics="Segmented exoskeleton, compound eyes"
        ),
        ReferenceFossil(
            common_name="Ammonite",
            scientific_name="Ammonoidea",
            fossil_type="Mollusk",
            geological_period="Jurassic",
            description="Extinct marine mollusk with spiral shell.",
            image_url="",
            characteristics="Coiled shell, chambered structure"
        ),
        ReferenceFossil(
            common_name="T-Rex Tooth",
            scientific_name="Tyrannosaurus rex",
            fossil_type="Dinosaur",
            geological_period="Cretaceous",
            description="Large carnivorous dinosaur tooth.",
            image_url="",
            characteristics="Serrated edges, thick enamel"
        )
    ]

    db.session.add_all(fossils)
    db.session.commit()

    print("Database seeded!")