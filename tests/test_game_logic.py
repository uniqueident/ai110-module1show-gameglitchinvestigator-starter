from logic_utils import check_guess, get_range_for_difficulty, parse_guess


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_never_receives_string_secret():
    # Regression: app previously cast secret to str on even attempts,
    # causing int vs str comparison to misbehave.
    # check_guess should work correctly when both values are ints.
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"
    outcome, _ = check_guess(10, 42)
    assert outcome == "Too Low"
    outcome, _ = check_guess(99, 42)
    assert outcome == "Too High"


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("???") == (1, 100)


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_float_string_truncates():
    # e.g. "3.9" should parse to 3, not round up
    ok, value, _ = parse_guess("3.9")
    assert ok is True
    assert value == 3

def test_parse_empty_string():
    ok, value, _ = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_non_numeric():
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_none_input():
    ok, value, _ = parse_guess(None)
    assert ok is False
    assert value is None
