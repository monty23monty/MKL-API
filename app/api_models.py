from flask_restx import fields
from .extensions import api

games_model = api.model('Games', {
    'GameID': fields.Integer,
    'Date': fields.String,
    'Location': fields.String,
    'HomeTeamID': fields.Integer,
    'AwayTeamID': fields.Integer,
    'CurrentPeriod': fields.String,
    'TimeRemaining': fields.String,
    'HomeTeamName': fields.String,
    'AwayTeamName': fields.String
})

teams_model = api.model('Teams', {
    'TeamID': fields.Integer,
    'TeamName': fields.String,
    'Abbreviation': fields.String,
    'City': fields.String,
    'CoachName': fields.String,
    'AssistantCoachName': fields.String
})

gamestats_model = api.model('GameStats', {
    'StatID': fields.Integer,
    'GameID': fields.Integer,
    'PlayerID': fields.Integer,
    'Goals': fields.Integer,
    'Assists': fields.Integer,
    'Points': fields.Integer,
    'PIM': fields.Integer,
    'FaceOffWins': fields.Integer,
    'FaceOffLosses': fields.Integer,
    'FaceOffPercentage': fields.Float
})

goals_model = api.model('Goals', {
    'GoalID': fields.Integer,
    'GameID': fields.Integer,
    'PeriodNumber': fields.Integer,
    'Scorer': fields.Integer,
    'Assist1': fields.Integer,
    'Assist2': fields.Integer,
    'Type': fields.String,
    'Time': fields.String
})

goaltenderstats_model = api.model('GoaltenderStats', {
    'GoaltenderStatID': fields.Integer,
    'PlayerID': fields.Integer,
    'GameID': fields.Integer,
    'ShotsAgainst': fields.Integer,
    'GoalsAgainst': fields.Integer,
    'Saves': fields.Integer,
    'SavePercentage': fields.Float,
    'Shutout': fields.Boolean
})

leaguetable_model = api.model('LeagueTable', {
    'LeagueTableID': fields.Integer,
    'TeamID': fields.Integer,
    'SeasonYear': fields.String,
    'GP': fields.Integer,
    'W': fields.Integer,
    'L': fields.Integer,
    'OTL': fields.Integer,
    'TP': fields.Integer,
    'GF': fields.Integer,
    'GA': fields.Integer,
    'PIM': fields.Integer,
    'PP': fields.Integer,
    'PK': fields.Integer,
    'PPG': fields.Float,
    'PKP': fields.Float,
    'GD': fields.Integer
})

penalties_model = api.model('Penalties', {
    'PenaltyID': fields.Integer,
    'GameID': fields.Integer,
    'PlayerID': fields.Integer,
    'TeamID': fields.Integer,
    'Type': fields.String,
    'Duration': fields.Integer,
    'StartTime': fields.String,
    'EndTime': fields.String,
    'TimeRemaining': fields.String
})

periodstats_model = api.model('PeriodStats', {
    'PeriodStatID': fields.Integer,
    'GameID': fields.Integer,
    'PeriodNumber': fields.Integer,
    'HomeSOG': fields.Integer,
    'AwaySOG': fields.Integer,
    'HomeGoals': fields.Integer,
    'AwayGoals': fields.Integer,
    'HomePIM': fields.Integer,
    'AwayPIM': fields.Integer
})

players_model = api.model('Players', {
    'PlayerID': fields.Integer,
    'FirstName': fields.String,
    'LastName': fields.String,
    'TeamID': fields.Integer,
    'Position': fields.String,
    'Shoots': fields.String,
    'Height': fields.String,
    'Weight': fields.Integer,
    'BirthDate': fields.String,
    'BirthCity': fields.String,
    'BirthCountry': fields.String
})

seasongoaltenderstats_model = api.model('SeasonGoaltenderStats', {
    'SeasonGoaltenderStatID': fields.Integer,
    'PlayerID': fields.Integer,
    'SeasonYear': fields.String,
    'GP': fields.Integer,
    'W': fields.Integer,
    'L': fields.Integer,
    'OTL': fields.Integer,
    'Shutouts': fields.Integer,
    'Saves': fields.Integer,
    'ShotsAgainst': fields.Integer,
    'GoalsAgainst': fields.Integer,
    'SavePercentage': fields.Float
})

seasonstats_model = api.model('SeasonStats', {
    'SeasonStatID': fields.Integer,
    'PlayerID': fields.Integer,
    'SeasonYear': fields.String,
    'GP': fields.Integer,
    'Goals': fields.Integer,
    'Assists': fields.Integer,
    'Points': fields.Integer,
    'PIM': fields.Integer,
    'FaceOffWins': fields.Integer,
    'FaceOffLosses': fields.Integer,
    'FaceOffPercentage': fields.Float
})

shootoutattempts_model = api.model('ShootoutAttempts', {
    'ShootoutAttemptID': fields.Integer,
    'GameID': fields.Integer,
    'PlayerID': fields.Integer,
    'GoaltenderID': fields.Integer,
    'AttemptNumber': fields.Integer,
    'Goal': fields.Boolean
})

staff_model = api.model('Staff', {
    'StaffID': fields.Integer,
    'GameID': fields.Integer,
    'FirstName': fields.String,
    'LastName': fields.String,
    'Role': fields.String
})

