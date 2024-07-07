from . import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    confederation = db.Column(db.String(100), nullable=False)
    badge_url = db.Column(db.String(255))

    players = db.relationship('Player', backref='team', lazy=True)

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50))
    current_team = db.Column(db.String(100))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    photo_url = db.Column(db.String(255))

# Métodos to_dict() para serialización
def team_to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'confederation': self.confederation,
        'badge_url': self.badge_url,
    }

def player_to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'position': self.position,
        'current_team': self.current_team,
        'team_id': self.team_id,
        'photo_url': self.photo_url,
    }

Team.to_dict = team_to_dict
Player.to_dict = player_to_dict
