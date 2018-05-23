import pytest

from hangman import Hanger

def test_indices():
    hanger = Hanger("tester")
    result = hanger.indices("e")
    expected = [1, 4]
    assert result == expected

def assert_intialisation():
    hanger = Hanger("tester")
    assert hanger.guessed == ["_"] * 6

def test_guess():
    hanger = Hanger("tester")

    indices = hanger.indices("e")
    hanger.insert_guess("e", indices)
    assert hanger.guessed_word == ["_", "e", "_", "_", "e", "_"]

def test_valid_guess_char_is_not_string():
    hanger = Hanger("tester")
    assert hanger.valid_guess(3) == False

def test_valid_guess_char_is_longer_than_one():
    hanger = Hanger("tester")
    assert hanger.valid_guess("12e") == False

def test_valid_guess_char_is_not_a_letter():
    hanger = Hanger("tester")
    assert hanger.valid_guess("1") == False

def test_valid_guess_char_is_valid():
    hanger = Hanger("tester")
    assert hanger.valid_guess("e")
