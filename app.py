from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy, model
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    pim = db.Column(db.Integer, nullable=False)
    faceoff_wins = db.Column(db.Integer, nullable=False)
    faceoff_losses = db.Column(db.Integer, nullable=False)
    faceoff_percentage = db.Column(db.Float, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'goals': self.goals,
            'assists': self.assists,
            'pim': self.pim,
            'faceoff_wins': self.faceoff_wins,
            'faceoff_losses': self.faceoff_losses,
            'faceoff_percentage': self.faceoff_percentage,
            'player_id': self.player_id
        }

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    roster_id = db.Column(db.Integer, db.ForeignKey('roster.id'))  # Added line
    stats = db.relationship('Stats', backref='player', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'position': self.position,
            'team_id': self.team_id,
            'stats': [stat.to_dict() for stat in self.stats] if self.stats else []
        }

class Roster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))  # Ensuring team link
    players = db.relationship('Player', backref='roster', lazy=True)  # This should work now



    def to_dict(self):
        return {
            'id': self.id,
            'players': [player.to_dict() for player in self.players] if self.players else None
        }

class Teams(db.Model):
    __tablename__ = 'teams'  # Explicit table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    roster = db.relationship('Roster', uselist=False, backref='team', lazy=True)  # Added line

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'roster': [player.to_dict() for player in self.roster.players] if self.roster else None
        }

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    home_score = db.Column(db.Integer, nullable=False)
    away_score = db.Column(db.Integer, nullable=False)
    home_sog = db.Column(db.Integer, nullable=False)  # Shots on goal
    away_sog = db.Column(db.Integer, nullable=False)
    period = db.Column(db.Integer, nullable=False)
    clock = db.Column(db.String(50), nullable=False)

    # Relationship definitions
    goals = db.relationship('Goals', backref='game', lazy='dynamic')
    home_team = db.relationship('Teams', foreign_keys=[home_team_id], backref='home_games')
    away_team = db.relationship('Teams', foreign_keys=[away_team_id], backref='away_games')


    def to_dict(self):
        return {
            'id': self.id,
            'home_team': self.home_team.to_dict() if self.home_team else None,
            'away_team': self.away_team.to_dict() if self.away_team else None,
            'home_score': self.home_score,
            'away_score': self.away_score,
            'home_sog': self.home_sog,
            'away_sog': self.away_sog,
            'period': self.period,
            'clock': self.clock,
            'goals': [goal.to_dict() for goal in self.goals] if self.goals else []
        }



class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    period = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(50), nullable=False)
    scorer_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False) 
    scorer = db.relationship('Player', foreign_keys=[scorer_id], backref='goals_scored', lazy=True)
    assist1_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=True)  
    assist1 = db.relationship('Player', foreign_keys=[assist1_id], backref='assists1', lazy=True)
    assist2_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=True)
    assist2 = db.relationship('Player', foreign_keys=[assist2_id], backref='assists2', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'period': self.period,
            'time': self.time,
            'scorer': self.scorer.to_dict() if self.scorer else None,
            'assist1': self.assist1.to_dict() if self.assist1 else None,
            'assist2': self.assist2.to_dict() if self.assist2 else None
        }


    

#recources

class PlayerResource(Resource):
    def get(self, player_id):
        player = Player.query.get(player_id)
        if not player:
            return {'message': 'Player not found'}, 404
        return jsonify(player.to_dict())

    def put(self, player_id):
        player = Player.query.get(player_id)
        if not player:
            return {'message': 'Player not found'}, 404
        data = request.get_json()
        player.name = data.get('name', player.name)
        player.number = data.get('number', player.number)
        player.position = data.get('position', player.position)
        player.team_id = data.get('team_id', player.team_id)
        db.session.commit()
        return jsonify(player.to_dict())

    def delete(self, player_id):
        player = Player.query.get(player_id)
        if not player:
            return {'message': 'Player not found'}, 404
        db.session.delete(player)
        db.session.commit()
        return {'message': 'Player deleted'}

class TeamResource(Resource):
    def get(self, team_id):
        team = Teams.query.get(team_id)
        if not team:
            return {'message': 'Team not found'}, 404
        return jsonify(team.to_dict())

    def put(self, team_id):
        team = Teams.query.get(team_id)
        if not team:
            return {'message': 'Team not found'}, 404
        data = request.get_json()
        team.name = data.get('name', team.name)
        db.session.commit()
        return jsonify(team.to_dict())

    def delete(self, team_id):
        team = Teams.query.get(team_id)
        if not team:
            return {'message': 'Team not found'}, 404
        db.session.delete(team)
        db.session.commit()
        return {'message': 'Team deleted'}

class GameResource(Resource):
    def get(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {'message': 'Game not found'}, 404
        return jsonify(game.to_dict())

    def put(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {'message': 'Game not found'}, 404
        data = request.get_json()
        game.home_team_id = data.get('home_team_id', game.home_team_id)
        game.away_team_id = data.get('away_team_id', game.away_team_id)
        game.home_score = data.get('home_score', game.home_score)
        game.away_score = data.get('away_score', game.away_score)
        game.home_sog = data.get('home_sog', game.home_sog)
        game.away_sog = data.get('away_sog', game.away_sog)
        game.period = data.get('period', game.period)
        game.clock = data.get('clock', game.clock)
        db.session.commit()
        return jsonify(game.to_dict())

    def delete(self, game_id):
        game = Game.query.get(game_id)
        if not game:
            return {'message': 'Game not found'}, 404
        db.session.delete(game)
        db.session.commit()
        return {'message': 'Game deleted'}

class RosterResource(Resource):
    def get(self, roster_id):
        roster = Roster.query.get(roster_id)
        if not roster:
            return {'message': 'Roster not found'}, 404
        return jsonify(roster.to_dict())

    def put(self, roster_id):
        roster = Roster.query.get(roster_id)
        if not roster:
            return {'message': 'Roster not found'}, 404
        data = request.get_json()
        roster.team_id = data.get('team_id', roster.team_id)
        db.session.commit()
        return jsonify(roster.to_dict())

    def delete(self, roster_id):
        roster = Roster.query.get(roster_id)
        if not roster:
            return {'message': 'Roster not found'}, 404
        db.session.delete(roster)
        db.session.commit()
        return {'message': 'Roster deleted'}

class StatsResource(Resource):
    def get(self, stat_id):
        stat = Stats.query.get(stat_id)
        if not stat:
            return {'message': 'Stat not found'}, 404
        return jsonify(stat.to_dict())

    def put(self, stat_id):
        stat = Stats.query.get(stat_id)
        if not stat:
            return {'message': 'Stat not found'}, 404
        data = request.get_json()
        stat.goals = data.get('goals', stat.goals)
        stat.assists = data.get('assists', stat.assists)
        stat.pim = data.get('pim', stat.pim)
        stat.faceoff_wins = data.get('faceoff_wins', stat.faceoff_wins)
        stat.faceoff_losses = data.get('faceoff_losses', stat.faceoff_losses)
        stat.faceoff_percentage = data.get('faceoff_percentage', stat.faceoff_percentage)
        db.session.commit()
        return jsonify(stat.to_dict())

    def delete(self, stat_id):
        stat = Stats.query.get(stat_id)
        if not stat:
            return {'message': 'Stat not found'}, 404
        db.session.delete(stat)
        db.session.commit()
        return {'message': 'Stat deleted'}

class GoalsResource(Resource):
    def get(self, goal_id):
        goal = Goals.query.get(goal_id)
        if not goal:
            return {'message': 'Goal not found'}, 404
        return jsonify(goal.to_dict())

    def put(self, goal_id):
        goal = Goals.query.get(goal_id)
        if not goal:
            return {'message': 'Goal not found'}, 404
        data = request.get_json()
        goal.game_id = data.get('game_id', goal.game_id)
        goal.period = data.get('period', goal.period)
        goal.time = data.get('time', goal.time)
        goal.scorer_id = data.get('scorer', goal.scorer_id)
        goal.assist1_id = data.get('assist1', goal.assist1_id)
        goal.assist2_id = data.get('assist2', goal.assist2_id)
        db.session.commit()
        return jsonify(goal.to_dict())

    def delete(self, goal_id):
        goal = Goals.query.get(goal_id)
        if not goal:
            return {'message': 'Goal not found'}, 404
        db.session.delete(goal)
        db.session.commit()
        return {'message': 'Goal deleted'}


class TeamsResource(Resource):
    def get(self):
        teams = Teams.query.all()
        return jsonify([team.to_dict() for team in teams])
    
    def post(self):
        data = request.get_json()
        new_team = Teams(
            name=data.get('name')
        )
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team.to_dict()), 201
    
class PlayersResource(Resource):
    def get(self):
        players = Player.query.all()
        return jsonify([player.to_dict() for player in players])
    
    def post(self):
        data = request.get_json()
        new_player = Player(
            name=data.get('name'),
            number=data.get('number'),
            position=data.get('position'),
            team_id=data.get('team_id'),
            roster_id=data.get('roster_id')
        )
        db.session.add(new_player)
        db.session.commit()
        return jsonify([new_player.to_dict()]), 201

class GamesResource(Resource):
    def get(self):
        games = Game.query.all()
        return jsonify([game.to_dict() for game in games])
    
    def post(self):
        data = request.get_json()
        new_game = Game(
            home_team_id=data.get('home_team_id'),
            away_team_id=data.get('away_team_id'),
            home_score=data.get('home_score'),
            away_score=data.get('away_score'),
            home_sog=data.get('home_sog'),
            away_sog=data.get('away_sog'),
            period=data.get('period'),
            clock=data.get('clock')
        )
        db.session.add(new_game)
        db.session.commit()
        return jsonify(new_game.to_dict()), 201

class RostersResource(Resource):
    def get(self):
        rosters = Roster.query.all()
        return jsonify([roster.to_dict() for roster in rosters])
    
    def post(self):
        data = request.get_json()
        new_roster = Roster(
            team_id=data.get('team_id')
        )
        db.session.add(new_roster)
        db.session.commit()
        return jsonify(new_roster.to_dict()), 201

class GoalsAllResource(Resource):
    def get(self):
        goals = Goals.query.all()
        return jsonify([goal.to_dict() for goal in goals])

    def post(self):
        data = request.get_json()
        new_goal = Goals(
            game_id=data.get('game_id'),
            period=data.get('period'),
            time=data.get('time'),
            scorer_id=data.get('scorer'),  # Assuming `scorer` is the ID
            assist1_id=data.get('assist1'),  # Assuming these are IDs
            assist2_id=data.get('assist2')
        )

        db.session.add(new_goal)
        db.session.commit()
        try:
            return jsonify([new_goal.todict()]), 201
        except Exception as e:
            return {'Content Posted': 'null'}, 201

class StatsAllResource(Resource):
    def get(self):
        stats = Stats.query.all()
        return jsonify([stat.to_dict() for stat in stats])
    
    def post(self):
        data = request.get_json()
        new_stat = Stats(
            goals=data.get('goals'),
            assists=data.get('assists'),
            pim=data.get('pim'),
            faceoff_wins=data.get('faceoff_wins'),
            faceoff_losses=data.get('faceoff_losses'),
            faceoff_percentage=data.get('faceoff_percentage'),
            player_id=data.get('player_id')
        )
        db.session.add(new_stat)
        db.session.commit()
        return jsonify(new_stat.to_dict()), 201


    
api.add_resource(PlayerResource, '/players/<int:player_id>')
api.add_resource(TeamResource, '/teams/<int:team_id>')
api.add_resource(GameResource, '/games/<int:game_id>')
api.add_resource(RosterResource, '/rosters/<int:roster_id>')
api.add_resource(StatsResource, '/stats/<int:stat_id>')
api.add_resource(GoalsResource, '/goals/<int:goal_id>')
api.add_resource(TeamsResource, '/teams')
api.add_resource(PlayersResource, '/players')
api.add_resource(GamesResource, '/games')
api.add_resource(RostersResource, '/rosters')
api.add_resource(GoalsAllResource, '/goals')
api.add_resource(StatsAllResource, '/stats')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="192.168.86.61")