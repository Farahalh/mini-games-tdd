from mini_games import get_level_settings

def test_easy_level():
    max_number, max_attempts = get_level_settings("1")

    assert max_number == 10
    assert max_attempts == 10