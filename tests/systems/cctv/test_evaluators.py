import pytest
from oop_2026.systems.cctv.model import SimpleEvaluator, OneDVision


@pytest.fixture
def evaluator():
    """Fixture that provides a SimpleEvaluator instance for tests."""
    return SimpleEvaluator()


def test_threat_level_2_when_stars_in_first_four_chars(evaluator):
    """Test that threat level 2 is returned when '**' appears in first 4 characters."""
    # '**' at the beginning
    vision = OneDVision('**test')
    result = evaluator.evaluate(vision)
    assert result.get_level() == 2

    # '**' within first 4 characters
    vision2 = OneDVision('a**b')
    result2 = evaluator.evaluate(vision2)
    assert result2.get_level() == 2


def test_threat_level_1_when_stars_after_fourth_char(evaluator):
    """Test that threat level 1 is returned when '**' appears after 4th character."""
    # '**' appears after position 4
    vision = OneDVision('test**something')
    result = evaluator.evaluate(vision)
    assert result.get_level() == 1

    # '**' at the end of longer string
    vision2 = OneDVision('abcdefgh**')
    result2 = evaluator.evaluate(vision2)
    assert result2.get_level() == 1


def test_threat_level_0_when_no_stars_pattern(evaluator):
    """Test that threat level 0 is returned when no '**' pattern is found."""
    # No stars at all
    vision = OneDVision('normal text')
    result = evaluator.evaluate(vision)
    assert result.get_level() == 0

    # Single star only (not double)
    vision2 = OneDVision('single*star')
    result2 = evaluator.evaluate(vision2)
    assert result2.get_level() == 0


def test_edge_cases(evaluator):
    """Test edge cases like empty strings and boundary conditions."""
    # Empty string
    vision_empty = OneDVision('')
    result_empty = evaluator.evaluate(vision_empty)
    assert result_empty.get_level() == 0

    # String shorter than 4 characters with '**'
    vision_short = OneDVision('**')
    result_short = evaluator.evaluate(vision_short)
    assert result_short.get_level() == 2

    # Exactly 4 characters ending with '**'
    vision_four = OneDVision('ab**')
    result_four = evaluator.evaluate(vision_four)
    assert result_four.get_level() == 2