from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from . import db
from .models import Team, Player

# Define the blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@bp.route('/teams/<int:id>', methods=['GET'])
def get_team(id):
    team = Team.query.get_or_404(id)
    return render_template('team_form.html', team=team)

@bp.route('/teams/add', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        name = request.form['name']
        confederation = request.form['confederation']
        badge_url = request.form['badge_url']
        new_team = Team(name=name, confederation=confederation, badge_url=badge_url)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('main.get_teams'))
    return render_template('team_form.html', team=None)

@bp.route('/teams/<int:id>/edit', methods=['GET', 'POST'])
def update_team(id):
    team = Team.query.get_or_404(id)
    if request.method == 'POST':
        team.name = request.form['name']
        team.confederation = request.form['confederation']
        team.badge_url = request.form['badge_url']
        db.session.commit()
        return redirect(url_for('main.get_teams'))
    return render_template('team_form.html', team=team)

@bp.route('/teams/<int:id>/delete', methods=['POST'])
def delete_team(id):
    team = Team.query.get_or_404(id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('main.get_teams'))

@bp.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])

@bp.route('/players/<int:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    return jsonify(player.to_dict())

@bp.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    new_player = Player(
        name=data['name'], age=data['age'], position=data['position'],
        current_team=data['current_team'], team_id=data['team_id'], photo_url=data['photo_url']
    )
    db.session.add(new_player)
    db.session.commit()
    return jsonify(new_player.to_dict()), 201

@bp.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    player = Player.query.get_or_404(id)
    data = request.get_json()
    player.name = data['name']
    player.age = data['age']
    player.position = data['position']
    player.current_team = data['current_team']
    player.team_id = data['team_id']
    player.photo_url = data['photo_url']
    db.session.commit()
    return jsonify(player.to_dict())

@bp.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = Player.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return '', 204
