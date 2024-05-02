from flask_restx import Namespace, Resource, fields
from .api_models import games_model, teams_model, gamestats_model, goals_model, goaltenderstats_model, leaguetable_model, penalties_model, periodstats_model, players_model, seasongoaltenderstats_model, seasonstats_model, shootoutattempts_model, staff_model
from .extensions import db, require_apikey
from .models import Games, Teams, GameStats, Goals, GoaltenderStats, LeagueTable, Penalties, PeriodStats, Players, SeasonGoaltenderStats, SeasonStats, ShootoutAttempts, Staff, ScoreboardData
from flask import request

ns = Namespace('api')

from flask import jsonify

@ns.route('/games')
class GamesAPI(Resource):
    @require_apikey
    @ns.marshal_with(games_model)
    @ns.doc(security='apikey')
    @ns.doc(headers={'X-API-KEY': {'description': 'An API key is required to access this endpoint', 'type': 'string', 'in': 'header', 'required': True}})
    def get(self):
        try:
            games = Games.query.all()
            #print(games)
            print([game.to_json() for game in games])
            for game in games:
                game.HomeTeamName = game.home_team.TeamName
                game.AwayTeamName = game.away_team.TeamName
            
            print([game.to_json() for game in games])
            return games
        except Exception as e:
            # Log the error and return a JSON error message
            ns.logger.error(f"Failed to fetch games: {e}")
            return jsonify({"error": "Failed to process request"}), 500

    @ns.expect(games_model)
    @require_apikey
    def post(self):
        game = Games(**request.json)
        db.session.add(game)
        db.session.commit()
        return game.to_json(), 201
    
    
@ns.route('/teams')
class TeamsAPI(Resource):
    @ns.marshal_with(teams_model)
    @require_apikey
    def get(self):
        teams = Teams.query.all()
        return [team.to_json() for team in teams]

    @ns.expect(teams_model)
    @require_apikey
    def post(self):
        team = Teams(**request.json)
        db.session.add(team)
        db.session.commit()
        return 200

@ns.route('/gamestats')
class GameStatsAPI(Resource):
    @ns.marshal_with(gamestats_model)
    @require_apikey
    def get(self):
        gamestats = GameStats.query.all()
        return [gamestat.to_json() for gamestat in gamestats]

    @ns.expect(gamestats_model)
    @require_apikey
    def post(self):
        gamestat = GameStats(**request.json)
        db.session.add(gamestat)
        db.session.commit()
        return gamestat.to_json()

@ns.route('/goals')
class GoalsAPI(Resource):
    @ns.marshal_with(goals_model)
    @require_apikey
    def get(self):
        goals = Goals.query.all()
        return [goal.to_json() for goal in goals]

    @ns.expect(goals_model)
    @require_apikey
    def post(self):
        goal = Goals(**request.json)
        db.session.add(goal)
        db.session.commit()
        return goal.to_json()

@ns.route('/goaltenderstats')
class GoaltenderStatsAPI(Resource):
    @ns.marshal_with(goaltenderstats_model)
    @require_apikey
    def get(self):
        goaltenderstats = GoaltenderStats.query.all()
        return [goaltenderstat.to_json() for goaltenderstat in goaltenderstats]

    @ns.expect(goaltenderstats_model)
    @require_apikey
    def post(self):
        goaltenderstat = GoaltenderStats(**request.json)
        db.session.add(goaltenderstat)
        db.session.commit()
        return goaltenderstat.to_json()

@ns.route('/leaguetable')
class LeagueTableAPI(Resource):
    @ns.marshal_with(leaguetable_model)
    @require_apikey
    def get(self):
        leaguetable = LeagueTable.query.all()
        return [leaguetable.to_json() for leaguetable in leaguetable]

    @ns.expect(leaguetable_model)
    @require_apikey
    def post(self):
        leaguetable = LeagueTable(**request.json)
        db.session.add(leaguetable)
        db.session.commit()
        return leaguetable.to_json()

@ns.route('/penalties')
class PenaltiesAPI(Resource):
    @ns.marshal_with(penalties_model)
    def get(self):
        penalties = Penalties.query.all()
        return [penalty.to_json() for penalty in penalties]

    @ns.expect(penalties_model)
    def post(self):
        penalty = Penalties(**request.json)
        db.session.add(penalty)
        db.session.commit()
        return penalty.to_json()

@ns.route('/periodstats')
class PeriodStatsAPI(Resource):
    @ns.marshal_with(periodstats_model)
    @require_apikey
    def get(self):
        periodstats = PeriodStats.query.all()
        return [periodstat.to_json() for periodstat in periodstats]

    @ns.expect(periodstats_model)
    @require_apikey
    def post(self):
        periodstat = PeriodStats(**request.json)
        db.session.add(periodstat)
        db.session.commit()
        return periodstat.to_json()

@ns.route('/players')
class PlayersAPI(Resource):
    @ns.marshal_with(players_model)
    @require_apikey
    def get(self):
        players = Players.query.all()
        return [player.to_json() for player in players]

    @ns.expect(players_model)
    @require_apikey
    def post(self):
        player = Players(**request.json)
        db.session.add(player)
        db.session.commit()
        return player.to_json()

@ns.route('/seasongoaltenderstats')
class SeasonGoaltenderStatsAPI(Resource):
    @ns.marshal_with(seasongoaltenderstats_model)
    @require_apikey
    def get(self):
        seasongoaltenderstats = SeasonGoaltenderStats.query.all()
        return [seasongoaltenderstat.to_json() for seasongoaltenderstat in seasongoaltenderstats]

    @ns.expect(seasongoaltenderstats_model)
    @require_apikey
    def post(self):
        seasongoaltenderstat = SeasonGoaltenderStats(**request.json)
        db.session.add(seasongoaltenderstat)
        db.session.commit()
        return seasongoaltenderstat.to_json()

@ns.route('/seasonstats')
class SeasonStatsAPI(Resource):
    @ns.marshal_with(seasonstats_model)
    @require_apikey
    def get(self):
        seasonstats = SeasonStats.query.all()
        return [seasonstat.to_json() for seasonstat in seasonstats]

    @ns.expect(seasonstats_model)
    @require_apikey
    def post(self):
        seasonstat = SeasonStats(**request.json)
        db.session.add(seasonstat)
        db.session.commit()
        return seasonstat.to_json()
    
@ns.route('/shootoutattempts')
class ShootoutAttemptsAPI(Resource):
    @ns.marshal_with(shootoutattempts_model)
    @require_apikey
    def get(self):
        shootoutattempts = ShootoutAttempts.query.all()
        return [shootoutattempt.to_json() for shootoutattempt in shootoutattempts]

    @ns.expect(shootoutattempts_model)
    @require_apikey
    def post(self):
        shootoutattempt = ShootoutAttempts(**request.json)
        db.session.add(shootoutattempt)
        db.session.commit()
        return shootoutattempt.to_json()

@ns.route('/staff')
class StaffAPI(Resource):
    @require_apikey
    @ns.marshal_with(staff_model)
    def get(self):
        staff = Staff.query.all()
        return [staff.to_json() for staff in staff]
    @require_apikey
    @ns.expect(staff_model)
    def post(self):
        staff = Staff(**request.json)
        db.session.add(staff)
        db.session.commit()
        return staff.to_json()
    
@ns.route('/games/<int:id>')
class GameAPI(Resource):
    @ns.marshal_with(games_model)
    @require_apikey
    def get(self, id):
        game = Games.query.get(id)
        return game.to_json()

    @ns.expect(games_model)
    @require_apikey
    def put(self, id):
        game = Games.query.get(id)
        for key, value in request.json.items():
            setattr(game, key, value)
        db.session.commit()
        return game.to_json()
    
    @require_apikey
    def delete(self, id):
        game = Games.query.get(id)
        db.session.delete(game)
        db.session.commit()
        return '', 204

@ns.route('/teams/<int:id>')
class TeamAPI(Resource):
    @ns.marshal_with(teams_model)
    @require_apikey
    def get(self, id):
        team = Teams.query.get(id)
        return team.to_json()

    @ns.expect(teams_model)
    @require_apikey
    def put(self, id):
        team = Teams.query.get(id)
        for key, value in request.json.items():
            setattr(team, key, value)
        db.session.commit()
        return team.to_json()

    @require_apikey
    def delete(self, id):
        team = Teams.query.get(id)
        db.session.delete(team)
        db.session.commit()
        return '', 204
    
@ns.route('/gamestats/<int:id>')
class GameStatAPI(Resource):
    @ns.marshal_with(gamestats_model)
    @require_apikey
    def get(self, id):
        gamestat = GameStats.query.get(id)
        return gamestat.to_json()

    @ns.expect(gamestats_model)
    @require_apikey
    def put(self, id):
        gamestat = GameStats.query.get(id)
        for key, value in request.json.items():
            setattr(gamestat, key, value)
        db.session.commit()
        return gamestat.to_json()
    
    @require_apikey
    def delete(self, id):
        gamestat = GameStats.query.get(id)
        db.session.delete(gamestat)
        db.session.commit()
        return '', 204

@ns.route('/goals/<int:id>')
class GoalAPI(Resource):
    @ns.marshal_with(goals_model)
    @require_apikey
    def get(self, id):
        goal = Goals.query.get(id)
        return goal.to_json()

    @ns.expect(goals_model)
    @require_apikey
    def put(self, id):
        goal = Goals.query.get(id)
        for key, value in request.json.items():
            setattr(goal, key, value)
        db.session.commit()
        return goal.to_json()

    @require_apikey
    def delete(self, id):
        goal = Goals.query.get(id)
        db.session.delete(goal)
        db.session.commit()
        return '', 204
    
@ns.route('/goaltenderstats/<int:id>')
class GoaltenderStatAPI(Resource):
    @require_apikey
    @ns.marshal_with(goaltenderstats_model)
    def get(self, id):
        goaltenderstat = GoaltenderStats.query.get(id)
        return goaltenderstat.to_json()

    @ns.expect(goaltenderstats_model)
    @require_apikey
    def put(self, id):
        goaltenderstat = GoaltenderStats.query.get(id)
        for key, value in request.json.items():
            setattr(goaltenderstat, key, value)
        db.session.commit()
        return goaltenderstat.to_json()

    @require_apikey
    def delete(self, id):
        goaltenderstat = GoaltenderStats.query.get(id)
        db.session.delete(goaltenderstat)
        db.session.commit()
        return '', 204
    
@ns.route('/leaguetable/<int:id>')
class LeagueTableAPI(Resource):
    @ns.marshal_with(leaguetable_model)
    @require_apikey
    def get(self, id):
        leaguetable = LeagueTable.query.get(id)
        return leaguetable.to_json()

    @ns.expect(leaguetable_model)
    @require_apikey
    def put(self, id):
        leaguetable = LeagueTable.query.get(id)
        for key, value in request.json.items():
            setattr(leaguetable, key, value)
        db.session.commit()
        return leaguetable.to_json()

    @require_apikey
    def delete(self, id):
        leaguetable = LeagueTable.query.get(id)
        db.session.delete(leaguetable)
        db.session.commit()
        return '', 204

@ns.route('/penalties/<int:id>')
class PenaltyAPI(Resource):
    @ns.marshal_with(penalties_model)
    def get(self, id):
        penalty = Penalties.query.get(id)
        return penalty.to_json()

    @ns.expect(penalties_model)
    def put(self, id):
        penalty = Penalties.query.get(id)
        for key, value in request.json.items():
            setattr(penalty, key, value)
        db.session.commit()
        return penalty.to_json()

    def delete(self, id):
        penalty = Penalties.query.get(id)
        db.session.delete(penalty)
        db.session.commit()
        return '', 204

@ns.route('/periodstats/<int:id>')
class PeriodStatAPI(Resource):
    @ns.marshal_with(periodstats_model)
    def get(self, id):
        periodstat = PeriodStats.query.get(id)
        return periodstat.to_json()

    @ns.expect(periodstats_model)
    def put(self, id):
        periodstat = PeriodStats.query.get(id)
        for key, value in request.json.items():
            setattr(periodstat, key, value)
        db.session.commit()
        return periodstat.to_json()

    def delete(self, id):
        periodstat = PeriodStats.query.get(id)
        db.session.delete(periodstat)
        db.session.commit()
        return '', 204

@ns.route('/players/<int:id>')
class PlayerAPI(Resource):
    @ns.marshal_with(players_model)
    def get(self, id):
        player = Players.query.get(id)
        return player.to_json()

    @ns.expect(players_model)
    def put(self, id):
        player = Players.query.get(id)
        for key, value in request.json.items():
            setattr(player, key, value)
        db.session.commit()
        return player.to_json()

    def delete(self, id):
        player = Players.query.get(id)
        db.session.delete(player)
        db.session.commit()
        return '', 204

@ns.route('/seasongoaltenderstats/<int:id>')
class SeasonGoaltenderStatAPI(Resource):
    @ns.marshal_with(seasongoaltenderstats_model)
    def get(self, id):
        seasongoaltenderstat = SeasonGoaltenderStats.query.get(id)
        return seasongoaltenderstat.to_json()

    @ns.expect(seasongoaltenderstats_model)
    def put(self, id):
        seasongoaltenderstat = SeasonGoaltenderStats.query.get(id)
        for key, value in request.json.items():
            setattr(seasongoaltenderstat, key, value)
        db.session.commit()
        return seasongoaltenderstat.to_json()

    def delete(self, id):
        seasongoaltenderstat = SeasonGoaltenderStats.query.get(id)
        db.session.delete(seasongoaltenderstat)
        db.session.commit()
        return '', 204

@ns.route('/seasonstats/<int:id>')
class SeasonStatAPI(Resource):
    @ns.marshal_with(seasonstats_model)
    def get(self, id):
        seasonstat = SeasonStats.query.get(id)
        return seasonstat.to_json()

    @ns.expect(seasonstats_model)
    def put(self, id):
        seasonstat = SeasonStats.query.get(id)
        for key, value in request.json.items():
            setattr(seasonstat, key, value)
        db.session.commit()
        return seasonstat.to_json()

    def delete(self, id):
        seasonstat = SeasonStats.query.get(id)
        db.session.delete(seasonstat)
        db.session.commit()
        return '', 204

@ns.route('/shootoutattempts/<int:id>')
class ShootoutAttemptAPI(Resource):
    @ns.marshal_with(shootoutattempts_model)
    def get(self, id):
        shootoutattempt = ShootoutAttempts.query.get(id)
        return shootoutattempt.to_json()

    @ns.expect(shootoutattempts_model)
    def put(self, id):
        shootoutattempt = ShootoutAttempts.query.get(id)
        for key, value in request.json.items():
            setattr(shootoutattempt, key, value)
        db.session.commit()
        return shootoutattempt.to_json()

    def delete(self, id):
        shootoutattempt = ShootoutAttempts.query.get(id)
        db.session.delete(shootoutattempt)
        db.session.commit()
        return '', 204

@ns.route('/staff/<int:id>')
class StaffAPI(Resource):
    @ns.marshal_with(staff_model)
    def get(self, id):
        staff = Staff.query.get(id)
        return staff.to_json()

    @ns.expect(staff_model)
    def put(self, id):
        staff = Staff.query.get(id)
        for key, value in request.json.items():
            setattr(staff, key, value)
        db.session.commit()
        return staff.to_json()
    
    @require_apikey
    def delete(self, id):
        staff = Staff.query.get(id)
        db.session.delete(staff)
        db.session.commit()
        return '', 204


#lookup team by name (get)

@ns.route('/teams/<string:teamname>')
class TeamAPI(Resource):
    @ns.marshal_with(teams_model)
    def get(self, teamname):
        team = Teams.query.filter_by(TeamName=teamname).first()
        return team.to_json()
    

#recive scoreboard data (post)

@ns.route('/scoreboard')
class Scoreboard(Resource):
    def post(self):
        data = request.json   
        try:
            away_score = int(data.get('Away Score.Text', 0)) 
            home_score = int(data.get('Home score.Text', 0))
            period = data.get('Period.Text', '').strip('stndrh').strip() 
            clock = data.get('clock.Text', '')

            # Assuming there's only ever one scoreboard data record
            scoreboard = ScoreboardData.query.first() or ScoreboardData()
            scoreboard.Clock = clock
            scoreboard.AwayScore = away_score
            scoreboard.HomeScore = home_score
            scoreboard.Period = period
            
            scoreboard.awaypenplayer1 = data.get('awaypenplayer1.Text', '')
            scoreboard.awaypenplayer2 = data.get('awaypenplayer2.Text', '')
            scoreboard.awaypentiime1 = data.get('awaypentime1.Text', '')
            scoreboard.awaypentiime2 = data.get('awaypentime2.Text', '')
            scoreboard.homepenplayer1 = data.get('homepenplayer1.Text', '')
            scoreboard.homepenplayer2 = data.get('homepenplayer2.Text', '')
            scoreboard.homepentiime1 = data.get('homepentime1.Text', '')
            scoreboard.homepentiime2 = data.get('homepentime2.Text', '')

            db.session.add(scoreboard)
            db.session.commit()

            return jsonify({"message": "Scoreboard updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400