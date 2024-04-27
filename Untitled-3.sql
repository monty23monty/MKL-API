
-- SQLite
INSERT INTO teams (name) VALUES ('Dragons'), ('Knights');
INSERT INTO roster (team_id) VALUES (1), (2);
INSERT INTO players (name, number, position, team_id) VALUES 
('Alex Carter', 8, 'Forward', 1),
('Jamie Lee', 16, 'Defense', 1),
('Chris Field', 9, 'Forward', 2),
('Morgan Sky', 23, 'Goalie', 2);
INSERT INTO stats (goals, assists, pim, faceoff_wins, faceoff_losses, faceoff_percentage, player_id) VALUES
(5, 3, 2, 10, 5, 66.7, 1),
(0, 2, 4, 0, 0, 0.0, 2),
(2, 1, 0, 7, 9, 43.8, 3),
(0, 0, 0, 0, 0, 0.0, 4);
INSERT INTO game (home_team_id, away_team_id, home_score, away_score, home_sog, away_sog, period, clock) VALUES 
(1, 2, 4, 3, 20, 18, 3, '00:00');
INSERT INTO goals (game_id, period, time, scorer_id, assist1_id, assist2_id) VALUES
(1, 1, '05:23', 1, 2, NULL),
(1, 2, '15:45', 3, NULL, NULL),
(1, 3, '07:30', 1, NULL, 3);
