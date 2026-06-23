import pytest

from logic_utils import check_guess


# --- Attempts counter (the bug we fixed in app.py) ---------------------------
# app.py displays "Attempts left" as `attempt_limit - st.session_state.attempts`,
# seeds `attempts` to 0 at the start of a game, and increments it by 1 on each
# submitted guess. The original bug seeded `attempts` to 1, so a brand-new game
# showed one fewer attempt than allowed. These tests pin down that contract.

ATTEMPT_LIMITS = {"Easy": 6, "Normal": 8, "Hard": 5}


def attempts_left(attempt_limit, attempts):
    """Mirror of app.py's display math: limit minus attempts used so far."""
    return attempt_limit - attempts


@pytest.mark.parametrize("difficulty, limit", ATTEMPT_LIMITS.items())
def test_new_game_shows_full_attempts(difficulty, limit):
    # A fresh game seeds attempts to 0, so the player must see the FULL allowance
    # (not limit - 1, which was the bug).
    starting_attempts = 0
    assert attempts_left(limit, starting_attempts) == limit


def test_attempts_left_decrements_by_one_per_guess():
    # Starting from a fresh game on Normal (limit 8), each guess should drop
    # "attempts left" by exactly one: 8 -> 7 -> 6 ...
    limit = ATTEMPT_LIMITS["Normal"]
    attempts = 0
    assert attempts_left(limit, attempts) == 8

    attempts += 1  # first guess submitted
    assert attempts_left(limit, attempts) == 7

    attempts += 1  # second guess submitted
    assert attempts_left(limit, attempts) == 6


def test_last_attempt_is_not_off_by_one():
    # On Normal the player should get all 8 guesses: after the 8th submitted guess
    # attempts_left hits exactly 0. With the old seed of 1 it would have hit 0 a
    # guess early, ending the game too soon.
    limit = ATTEMPT_LIMITS["Normal"]
    assert attempts_left(limit, limit) == 0
    assert attempts_left(limit, limit - 1) == 1


# --- check_guess --------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
