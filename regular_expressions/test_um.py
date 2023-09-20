import pytest
from um import count


def test_input():
    assert count("um") == 1
    assert count("yum") == 0
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1