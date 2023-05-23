# Team Roster Glossary

This glossary can be used for any data retrieved using this program stub, which retrieves player demographics for the Raptors members:

    # get player demographics for the Raptors
    from nba_api.stats.endpoints import commonteamroster
    roster = commonteamroster.CommonTeamRoster(team_id=1610612761)
    roster_df = roster.get_data_frames()[0]

To display the PLAYER and HEIGHT columns only, you need to pass the column names as a list. For example:

    roster_df[["PLAYER", "HEIGHT"]]

...would only print the PLAYER and HEIGHT data.

- **TeamID**: The unique identification number of each team in the NBA database.
- **SEASON**: The start year of a season. For example, 2022 means the season started in 2022 and ended in 2023.
- **LeagueID**: The identification code of the league that a player or team belongs to. For example, 00 means the NBA, 10 means the NBA G League, and 20 means the WNBA.
- **PLAYER**: The full name of the player.
- **NICKNAME**: The common or popular name of the player, if any.
- **PLAYER_SLUG**: The abbreviated name of the player used in URLs and other references. For example, lebron_james is the player slug for LeBron James.
- **NUM**: The jersey number of the player.
- **POSITION**: The primary position that the player plays on the court. For example, PG means point guard, SG means shooting guard, SF means small forward, PF means power forward, and C means center. Some players may play multiple positions or have no specific position.
- **HEIGHT**: The height of the player in feet and inches.
- **WEIGHT**: The weight of the player in pounds.
- **BIRTH_DATE**: The date of birth of the player in month/day/year format.
- **AGE**: The age of the player on February 1 of the given season.
- **EXP**: The years of experience that the player has in the NBA. Rookies have EXP value of 0. Players who have not played in the NBA but have played in other professional leagues have EXP value of R.
- **SCHOOL**: The college or university that the player attended before entering the NBA, if any.
- **PLAYER_ID**: The unique identification number of each player in the NBA database.
- **HOW_ACQUIRED**: The method by which a player joined a team. For example, Draft means the player was drafted by the team, Trade means the player was traded from another team, FA means the player was signed as a free agent, etc.

Source: Conversation with Bing, 2023-05-23 (Edited)
1. Stat Glossary | Stats | NBA.com. https://www.nba.com/stats/help/glossary.
2. Glossary | Basketball-Reference.com. https://www.basketball-reference.com/about/glossary.html.
3. ESPN.com - NBA - NBA Sortable Statistics Glossary. https://www.espn.com/editors/nba/glossary.html.
4. Basketball statistics - Wikipedia. https://en.wikipedia.org/wiki/Basketball_statistics.