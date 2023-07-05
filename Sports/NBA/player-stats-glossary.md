# NBA Player Statistics Glossary

This glossary can be used for any data retrieved using this program stub, which retrieves player statistics for the Raptors members:

    # get player stats for the Raptors
    from nba_api.stats.endpoints import teamplayerdashboard
    player_stats = teamplayerdashboard.TeamPlayerDashboard(team_id=1610612761)
    player_stats_df = player_stats.get_data_frames()[1]

- **AST**: Assists; the total number of passes that a player or team has made that directly led to a made field goal by a teammate in a game or a season.
- **BLK**: Blocks (available since the 1973-74 season in the NBA); the total number of times that a player or team has prevented an opponent from making a field goal attempt by deflecting the ball with their hand(s) in a game or a season.
- **BLKA**: Blocked Field Goal Attempts (available since the 1996-97 season in the NBA); the total number of times that a player's or team's own field goal attempts have been blocked by an opponent in a game or a season. 
- **DD2**: Double Doubles; the total number of games where a player recorded at least 10 units (points, rebounds, assists, steals, or blocks) in two different categories. For example, if a player had 15 points and 10 rebounds in one game, they would have one double double.
- **DREB**: Defensive Rebounds (available since the 1973-74 season in the NBA); the total number of rebounds that a player or team has grabbed on their own defensive end in a game or a season.
- **FG3A**: 3-Point Field Goals Attempted (available since the 1979-80 season in the NBA); the total number of 3-point field goals that a player or team has attempted in a game or a season.
- **FG3M**: 3-Point Field Goals Made (available since the 1979-80 season in the NBA); the total number of 3-point field goals that a player or team has made in a game or a season.
- **FG3_PCT**: 3-Point Field Goal Percentage (available since the 1979-80 season in the NBA); the formula is FG3M / FG3A.
- **FGA**: Field Goals Attempted; the total number of field goals (both 2-point and 3-point) that a player or team has attempted in a game or a season.
- **FGM** (or **FG**): Field Goals Made; the total number of field goals (both 2-point and 3-point) that a player or team has made in a game or a season.
- **FG_PCT**: Field Goal Percentage; the formula is FGM / FGA.
- **FTA**: Free Throws Attempted; the total number of free throws that a player or team has attempted in a game or a season.
- **FTM**: Free Throws Made; the total number of free throws that a player or team has made in a game or a season.
- **FT_PCT**: Free Throw Percentage; the formula is FTM / FTA.
- **GP**: Games Played; the number of games that a player or team has played in a season or a specific period of time.
- **GP_RANK**: Games Played Rank; the rank order among all players based on their games played statistic.
- **GROUP_SET**: The name of the group of players being displayed, such as All Players, Rookies, Sophomores, etc.
- **L**: Losses; the number of games that a player or team has lost in a season or a specific period of time.
- **MIN**: Minutes Played; the total number of minutes that a player or team has played in a game or a season.
- **NBA_FANTASY_PTS**: NBA Fantasy Points; the total number of fantasy points earned by a player based on their statistical performance in real games. Fantasy points are calculated using different scoring systems depending on different fantasy leagues and platforms. However, one common scoring system used by NBA.com is: one point for each point scored, rebound, assist, steal and block; minus one point for each turnover; and half point for each made three-pointer. Fantasy points can be used to measure how valuable players are for fantasy basketball purposes.
- **NICKNAME**: The common or popular name of the player, if any.
- **OREB**: Offensive Rebounds (available since the 1973-74 season in the NBA); the total number of rebounds that a player or team has grabbed on their own offensive end in a game or a season.
- **PF**: Personal Fouls; the total number of fouls that a player or team has committed in a game or a season. A personal foul is an infraction of the rules involving illegal physical contact with an opponent. There are different types of personal fouls, such as shooting fouls, loose ball fouls, offensive fouls, etc. Each personal foul counts as one team foul, and players may be disqualified from playing after committing six personal fouls (five in some leagues). Some personal fouls also result in free throw attempts for the opposing team. 
- **PFD**: Personal Fouls Drawn; the total number of fouls that a player or team has drawn from an opponent in a game or a season. A personal foul drawn is when an opponent commits an illegal physical contact with a player, resulting in either free throw attempts, a change of possession, or both. Some personal fouls drawn also count as assists for the player who drew them. 
- **PLAYER_ID**: The unique identification number of each player in the NBA database.
- **PLAYER_NAME**: The full name of the player.
- **PLUS_MINUS**: Plus-Minus; the point differential when a player or group of players is on the court. It is calculated by subtracting the points scored by opponents from the points scored by teammates while they are playing. A positive plus-minus indicates that their team outscored their opponents while they were on the court, while a negative plus-minus indicates that their opponents outscored their team while they were on the court. A plus-minus value can be calculated for individual players, groups of players (such as starters, bench players, lineups), teams, and games. Plus-minus can be used to measure how much impact players have on their team's performance beyond their individual statistics. However, plus-minus can also be influenced by factors such as teammates' quality, opponents' quality, coaching decisions, luck, and sample size. Therefore, plus-minus should not be used as an isolated metric but rather as one piece of information among others to evaluate players and teams.
- **PTS**: Points; the total number of points scored by a player or team in a game or a season. Points are scored by making field goals (worth two points each, unless made behind the three-point line, which are worth three points each) and free throws (worth one point each). Some leagues also award bonus points for certain achievements, such as scoring more than 100 points in a game. The team with more points at the end of the game wins. If both teams have equal points at the end of regulation time, overtime periods are played until one team has more points than the other.
- **REB**: Rebounds; the total number of rebounds (both offensive and defensive) that a player or team has grabbed in a game or a season.
- **STL**: Steals (available since the 1973-74 season in the NBA); the total number of times that a player or team has taken possession of the ball from an opponent without committing a foul in a game or a season.
- **TD3**: Triple Doubles; the total number of games where a player recorded at least 10 units (points, rebounds, assists, steals, or blocks) in three different categories. For example, if a player had 10 points, 10 rebounds, and 10 assists in one game, they would have one triple double.
- **TOV**: Turnovers; the total number of times that a player or team has lost possession of the ball to the opposing team in a game or a season.
- **W**: Wins; the number of games that a player or team has won in a season or a specific period of time.
- **WNBA_FANTASY_PTS**: WNBA Fantasy Points; the total number of fantasy points earned by a WNBA player based on their statistical performance in real games. Fantasy points are calculated using different scoring systems depending on different fantasy leagues and platforms. However, one common scoring system used by WNBA.com is: one point for each point scored, rebound, assist, steal and block; minus one point for each turnover; and half point for each made three-pointer. Fantasy points can be used to measure how valuable players are for fantasy basketball purposes.
- **W_PCT**: Win Percentage; the formula is W / (W + L).
- **W_RANK**: Wins Rank; the rank order among all players based on their wins

Source: Conversation with Bing, 2023-05-23
1. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
2. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
3. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
4. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.
5. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
6. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
7. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
8. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.
9. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
10. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
11. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
12. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.
13. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
14. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
15. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
16. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.
17. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
18. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
19. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
20. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.
