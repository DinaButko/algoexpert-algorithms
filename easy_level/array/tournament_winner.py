HOME_TEAM_WON = 1  # Constant to represent the home team winning

# O(n) time | O(k) space, where:
# - n is the number of competitions
# - k is the number of teams
def tournamentWinner(competitions, results):
    currentBestTeam = ""  # Initialize with an empty string (no best team yet)
    scores = {currentBestTeam: 0}  # Dictionary to keep track of scores, starting with the initial team (empty string)

    # Loop over each competition to determine the winner
    for idx, competition in enumerate(competitions):
        result = results[idx]  # Get the result for the current competition
        homeTeam, awayTeam = competition  # Unpack the home and away teams

        # Determine the winning team based on the result
        # If result == 1, home team won; otherwise, away team won
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # Update the scores for the winning team
        updateScores(winningTeam, 3, scores)  # Winning team earns 3 points

        # If the winning team has a higher score than the current best team, update the best team
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam  # Update the current best team

    return currentBestTeam  # Return the team with the highest score

# Helper function to update the score of a team
def updateScores(team, points, scores):
    # If the team is not in the scores dictionary, initialize their score to 0
    if team not in scores:
        scores[team] = 0
    # Add the points (3 for a win) to the team's current score
    scores[team] += points
