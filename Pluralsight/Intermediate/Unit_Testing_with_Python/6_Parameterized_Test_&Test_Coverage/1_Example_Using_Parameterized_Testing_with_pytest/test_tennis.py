from tennis import score_tennis
####
# Parameterise

@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [(0,0, "Love-All"),
                          (1,1, "Fifteen-All"),
                          (2,2, "Thirty-All"),
                           ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points)== expected_score

#____________________________________________
    """
def test_0_0_love_all():
    assert score_tennis(0,0) == "Love-All"

def test_1_1_fifteen_all():
    assert score_tennis(1,1) == "Fifteen-All"

def test_2_2_thirty_all():
    assert score_tennis(2,2) == "thirty-All"
    """
