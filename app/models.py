from .extensions import db, ForeignKey

class Games(db.Model):
    __tablename__ = 'Games'
    GameID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String(50))
    Location = db.Column(db.String(50))
    HomeTeamID = db.Column(db.Integer, ForeignKey('Teams.TeamID'))
    AwayTeamID = db.Column(db.Integer, ForeignKey('Teams.TeamID'))
    CurrentPeriod = db.Column(db.String(50))
    TimeRemaining = db.Column(db.String(50))
    home_team = db.relationship('Teams', foreign_keys=[HomeTeamID])
    away_team = db.relationship('Teams', foreign_keys=[AwayTeamID])

    def __repr__(self):
        return '<Game %r>' % self.GameID
    
    def to_json(self):
        return {
            'GameID': self.GameID,
            'Date': self.Date,
            'Location': self.Location,
            'HomeTeamID': self.HomeTeamID,
            'AwayTeamID': self.AwayTeamID,
            'CurrentPeriod': self.CurrentPeriod,
            'TimeRemaining': self.TimeRemaining
        }

class Teams(db.Model):
    __tablename__ = 'Teams'
    TeamID = db.Column(db.Integer, primary_key=True)
    TeamName = db.Column(db.String(50))
    Abbreviation = db.Column(db.String(50))
    City = db.Column(db.String(50))
    CoachName = db.Column(db.String(50))
    AssistantCoachName = db.Column(db.String(50))

    def __repr__(self):
        return str(self.TeamName)
    
    def to_json(self):
        return {
            'TeamID': self.TeamID,
            'TeamName': self.TeamName,
            'Abbreviation': self.Abbreviation,
            'City': self.City,
            'CoachName': self.CoachName,
            'AssistantCoachName': self.AssistantCoachName
        }

class GameStats(db.Model):
    __tablename__ = 'GameStats'
    StatID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    Goals = db.Column(db.Integer)
    Assists = db.Column(db.Integer)
    Points = db.Column(db.Integer)
    PIM = db.Column(db.Integer)
    FaceOffWins = db.Column(db.Integer)
    FaceOffLosses = db.Column(db.Integer)
    FaceOffPercentage = db.Column(db.Float)

    def __repr__(self):
        return '<GameStat %r>' % self.StatID
    
    def to_json(self):
        return {
            'StatID': self.StatID,
            'GameID': self.GameID,
            'PlayerID': self.PlayerID,
            'Goals': self.Goals,
            'Assists': self.Assists,
            'Points': self.Points,
            'PIM': self.PIM,
            'FaceOffWins': self.FaceOffWins,
            'FaceOffLosses': self.FaceOffLosses,
            'FaceOffPercentage': self.FaceOffPercentage
        }

class Goals(db.Model):
    __tablename__ = 'Goals'
    GoalID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    PeriodNumber = db.Column(db.Integer)
    Scorer = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    Assist1 = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    Assist2 = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    Type = db.Column(db.String(50))
    Time = db.Column(db.String(50))

    def __repr__(self):
        return '<Goal %r>' % self.GoalID
    
    def to_json(self):
        return {
            'GoalID': self.GoalID,
            'GameID': self.GameID,
            'PeriodNumber': self.PeriodNumber,
            'Scorer': self.Scorer,
            'Assist1': self.Assist1,
            'Assist2': self.Assist2,
            'Type': self.Type,
            'Time': self.Time
        }

class GoaltenderStats(db.Model):
    __tablename__ = 'GoaltenderStats'
    GoaltenderStatID = db.Column(db.Integer, primary_key=True)
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    ShotsAgainst = db.Column(db.Integer)
    GoalsAgainst = db.Column(db.Integer)
    Saves = db.Column(db.Integer)
    SavePercentage = db.Column(db.Float)
    Shutout = db.Column(db.Boolean)

    def __repr__(self):
        return '<GoaltenderStat %r>' % self.GoaltenderStatID
    
    def to_json(self):
        return {
            'GoaltenderStatID': self.GoaltenderStatID,
            'PlayerID': self.PlayerID,
            'GameID': self.GameID,
            'ShotsAgainst': self.ShotsAgainst,
            'GoalsAgainst': self.GoalsAgainst,
            'Saves': self.Saves,
            'SavePercentage': self.SavePercentage,
            'Shutout': self.Shutout
        }

class LeagueTable(db.Model):
    __tablename__ = 'LeagueTable'
    LeagueTableID = db.Column(db.Integer, primary_key=True)
    TeamID = db.Column(db.Integer, ForeignKey('Teams.TeamID'))
    SeasonYear = db.Column(db.String(50))
    GP = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    OTL = db.Column(db.Integer)
    TP = db.Column(db.Integer)
    GF = db.Column(db.Integer)
    GA = db.Column(db.Integer)
    PIM = db.Column(db.Integer)
    PP = db.Column(db.Integer)
    PK = db.Column(db.Integer)
    PPG = db.Column(db.Float)
    PKP = db.Column(db.Float)
    GD = db.Column(db.Integer)

    def __repr__(self):
        return '<LeagueTable %r>' % self.LeagueTableID
    
    def to_json(self):
        return {
            'LeagueTableID': self.LeagueTableID,
            'TeamID': self.TeamID,
            'SeasonYear': self.SeasonYear,
            'GP': self.GP,
            'W': self.W,
            'L': self.L,
            'OTL': self.OTL,
            'TP': self.TP,
            'GF': self.GF,
            'GA': self.GA,
            'PIM': self.PIM,
            'PP': self.PP,
            'PK': self.PK,
            'PPG': self.PPG,
            'PKP': self.PKP,
            'GD': self.GD
        }

class Penalties(db.Model):
    __tablename__ = 'Penalties'
    PenaltyID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    TeamID = db.Column(db.Integer, ForeignKey('Teams.TeamID'))
    Type = db.Column(db.String(50))
    Duration = db.Column(db.Integer)
    StartTime = db.Column(db.String(50))
    EndTime = db.Column(db.String(50))
    TimeRemaining = db.Column(db.String(50))

    def __repr__(self):
        return '<Penalty %r>' % self.PenaltyID
    
    def to_json(self):
        return {
            'PenaltyID': self.PenaltyID,
            'GameID': self.GameID,
            'PlayerID': self.PlayerID,
            'TeamID': self.TeamID,
            'Type': self.Type,
            'Duration': self.Duration,
            'StartTime': self.StartTime,
            'EndTime': self.EndTime,
            'TimeRemaining': self.TimeRemaining
        }

class PeriodStats(db.Model):
    __tablename__ = 'PeriodStats'
    PeriodStatID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    PeriodNumber = db.Column(db.Integer)
    HomeSOG = db.Column(db.Integer)
    AwaySOG = db.Column(db.Integer)
    HomeGoals = db.Column(db.Integer)
    AwayGoals = db.Column(db.Integer)
    HomePIM = db.Column(db.Integer)
    AwayPIM = db.Column(db.Integer)

    def __repr__(self):
        return '<PeriodStat %r>' % self.PeriodStatID
    
    def to_json(self):
        return {
            'PeriodStatID': self.PeriodStatID,
            'GameID': self.GameID,
            'PeriodNumber': self.PeriodNumber,
            'HomeSOG': self.HomeSOG,
            'AwaySOG': self.AwaySOG,
            'HomeGoals': self.HomeGoals,
            'AwayGoals': self.AwayGoals,
            'HomePIM': self.HomePIM,
            'AwayPIM': self.AwayPIM
        }

class Players(db.Model):
    __tablename__ = 'Players'
    PlayerID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    TeamID = db.Column(db.Integer, ForeignKey('Teams.TeamID'))
    Position = db.Column(db.String(50))
    Shoots = db.Column(db.String(50))
    Height = db.Column(db.String(50))
    Weight = db.Column(db.Integer)
    BirthDate = db.Column(db.String(50))
    BirthCity = db.Column(db.String(50))
    BirthCountry = db.Column(db.String(50))

    def __repr__(self):
        return '<Player %r>' % self.PlayerID
    
    def to_json(self):
        return {
            'PlayerID': self.PlayerID,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'TeamID': self.TeamID,
            'Position': self.Position,
            'Shoots': self.Shoots,
            'Height': self.Height,
            'Weight': self.Weight,
            'BirthDate': self.BirthDate,
            'BirthCity': self.BirthCity,
            'BirthCountry': self.BirthCountry
        }

class SeasonGoaltenderStats(db.Model):
    __tablename__ = 'SeasonGoaltenderStats'
    SeasonGoaltenderStatID = db.Column(db.Integer, primary_key=True)
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    SeasonYear = db.Column(db.String(50))
    GP = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    OTL = db.Column(db.Integer)
    Shutouts = db.Column(db.Integer)
    Saves = db.Column(db.Integer)
    ShotsAgainst = db.Column(db.Integer)
    GoalsAgainst = db.Column(db.Integer)
    SavePercentage = db.Column(db.Float)

    def __repr__(self):
        return '<SeasonGoaltenderStat %r>' % self.SeasonGoaltenderStatID
    
    def to_json(self):
        return {
            'SeasonGoaltenderStatID': self.SeasonGoaltenderStatID,
            'PlayerID': self.PlayerID,
            'SeasonYear': self.SeasonYear,
            'GP': self.GP,
            'W': self.W,
            'L': self.L,
            'OTL': self.OTL,
            'Shutouts': self.Shutouts,
            'Saves': self.Saves,
            'ShotsAgainst': self.ShotsAgainst,
            'GoalsAgainst': self.GoalsAgainst,
            'SavePercentage': self.SavePercentage
        }

class SeasonStats(db.Model):
    __tablename__ = 'SeasonStats'
    SeasonStatID = db.Column(db.Integer, primary_key=True)
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    SeasonYear = db.Column(db.String(50))
    GP = db.Column(db.Integer)
    Goals = db.Column(db.Integer)
    Assists = db.Column(db.Integer)
    Points = db.Column(db.Integer)
    PIM = db.Column(db.Integer)
    FaceOffWins = db.Column(db.Integer)
    FaceOffLosses = db.Column(db.Integer)
    FaceOffPercentage = db.Column(db.Float)

    def __repr__(self):
        return '<SeasonStat %r>' % self.SeasonStatID
    
    def to_json(self):
        return {
            'SeasonStatID': self.SeasonStatID,
            'PlayerID': self.PlayerID,
            'SeasonYear': self.SeasonYear,
            'GP': self.GP,
            'Goals': self.Goals,
            'Assists': self.Assists,
            'Points': self.Points,
            'PIM': self.PIM,
            'FaceOffWins': self.FaceOffWins,
            'FaceOffLosses': self.FaceOffLosses,
            'FaceOffPercentage': self.FaceOffPercentage
        }

class ShootoutAttempts(db.Model):
    __tablename__ = 'ShootoutAttempts'
    ShootoutAttemptID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    PlayerID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    GoaltenderID = db.Column(db.Integer, ForeignKey('Players.PlayerID'))
    AttemptNumber = db.Column(db.Integer)
    Goal = db.Column(db.Boolean)

    def __repr__(self):
        return '<ShootoutAttempt %r>' % self.ShootoutAttemptID
    
    def to_json(self):
        return {
            'ShootoutAttemptID': self.ShootoutAttemptID,
            'GameID': self.GameID,
            'PlayerID': self.PlayerID,
            'GoaltenderID': self.GoaltenderID,
            'AttemptNumber': self.AttemptNumber,
            'Goal': self.Goal
        }
    
class Staff(db.Model):
    __tablename__ = 'Staff'
    StaffID = db.Column(db.Integer, primary_key=True)
    GameID = db.Column(db.Integer, ForeignKey('Games.GameID'))
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Role = db.Column(db.String(50))

    def __repr__(self):
        return '<Staff %r>' % self.StaffID
    
    def to_json(self):
        return {
            'StaffID': self.StaffID,
            'GameID': self.GameID,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Role': self.Role
        }



    def __repr__(self):
        return '<Team %r>' % self.TeamID
    
    def to_json(self):
        return {
            'TeamID': self.TeamID,
            'TeamName': self.TeamName,
            'Abbreviation': self.Abbreviation,
            'City': self.City,
            'CoachName': self.CoachName,
            'AssistantCoachName': self.AssistantCoachName
        }
    
class ScoreboardData(db.Model):
    __tablename__ = 'ScoreboardData'
    ScoreboardDataID = db.Column(db.Integer, primary_key=True)
    Clock = db.Column(db.String(10))
    AwayScore = db.Column(db.Integer)
    HomeScore = db.Column(db.Integer)
    Period = db.Column(db.Integer)
    awaypenplayer1 = db.Column(db.Integer, nullable=True)
    awaypenplayer2 = db.Column(db.Integer, nullable=True)
    awaypentiime1 = db.Column(db.String(10), nullable=True)
    awaypentiime2 = db.Column(db.String(10), nullable=True)
    homepenplayer1 = db.Column(db.Integer, nullable=True)
    homepenplayer2 = db.Column(db.Integer, nullable=True)
    homepentiime1 = db.Column(db.String(10), nullable=True)
    homepentiime2 = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<ScoreboardData %r>' % self.ScoreboardDataID
    
    def to_json(self):
        return {
            'ScoreboardDataID': self.ScoreboardDataID,
            'Clock': self.Clock,
            'AwayScore': self.AwayScore,
            'HomeScore': self.HomeScore,
            'Period': self.Period,
            'awaypenplayer1': self.awaypenplayer1,
            'awaypenplayer2': self.awaypenplayer2,
            'awaypentiime1': self.awaypentiime1,
            'awaypentiime2': self.awaypentiime2,
            'homepenplayer1': self.homepenplayer1,
            'homepenplayer2': self.homepenplayer2,
            'homepentiime1': self.homepentiime1,
            'homepentiime2': self.homepentiime2
        }