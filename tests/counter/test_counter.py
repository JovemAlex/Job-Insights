from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    Javascript_counter = 122
    python_counter = 1639

    assert (
        count_ocurrences("data/jobs.csv", "Javascript") == Javascript_counter
    )

    assert count_ocurrences("data/jobs.csv", "python") == python_counter

    with pytest.raises(
        AttributeError, match="'int' object has no attribute 'lower'"
    ):
        count_ocurrences("data/jobs.csv", 3)
