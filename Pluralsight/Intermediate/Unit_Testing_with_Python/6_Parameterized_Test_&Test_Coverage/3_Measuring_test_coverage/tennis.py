
def score_tennis(player1_points, player2_points):
    score_name = ["Love", "Fifteen", "Thirty", "Forty"]
    if _end_game(player1_points, player2_points):
        leader = "Player 2"
        if player1_points > player2_ponts:
            leader = "Player 1"

        if abs(player2_points - player1_points) == 1:
            return f"Advantage {leader}"
        else:
            return f"Win for {leader}"

        player1_score = score_names[player1_points]
        if player1_poins == player2_points:
            return f"{player1_score}-All"

def _end_game(player1_points, player2_points):
    return player1_points > 3 or player2_points > 3
