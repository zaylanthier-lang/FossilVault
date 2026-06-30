from config import create_app
from routes.auth import auth_bp
from routes.fossils import fossils_bp
from routes.reference import reference_bp

app = create_app()

app.register_blueprint(auth_bp)
app.register_blueprint(fossils_bp)
app.register_blueprint(reference_bp)

if __name__ == "__main__":
    app.run(port=5555, debug=True)