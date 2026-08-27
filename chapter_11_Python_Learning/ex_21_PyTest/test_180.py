# test_180.py
# Topic: pytest - marking tests (smoke / reg)
#
# Run with:  pytest test_180.py
# -m "smoke" / -m "reg" filters by marker (only run that group).
# assert 3 == 3 is a passing check; pytest reports it as a pass.

import pytest

@pytest.mark.reg
def test_anwser1():
    assert 3 == 3

@pytest.mark.smoke
def test_anwser2():
    assert 3 == 3

