from health import *
def make_player(health=100, max_health=100, alive=True):
    return {"health": health, "max_health": max_health, "alive": alive}

def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] == 70


def test_heal_increases_health():
    player = make_player(health=60)
    result = heal(player, 20)
    assert result["health"] == 80

def test_is_alive_returns_true_when_healthy():
    player = make_player()
    assert is_alive(player) == True