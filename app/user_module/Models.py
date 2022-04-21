from app import db

class User(db.Model):
    __tablename__ = 'userstest'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)

    #representation
    def __repr__(self):
        return f"User(firstname={firstname}, lastname={lastname}, email={email})"