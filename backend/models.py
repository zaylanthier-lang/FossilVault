from config import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    fossils = db.relationship(
        "Fossil",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Fossil(db.Model):
    __tablename__ = "fossils"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    fossil_type = db.Column(db.String(100), nullable=False)
    geological_period = db.Column(db.String(100), nullable=False)
    location_found = db.Column(db.String(150), nullable=False)
    date_found = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="fossils"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fossil_type": self.fossil_type,
            "geological_period": self.geological_period,
            "location_found": self.location_found,
            "date_found": self.date_found,
            "description": self.description,
            "image_url": self.image_url,
            "user_id": self.user_id
        }