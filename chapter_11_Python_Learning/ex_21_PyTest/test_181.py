# test_181.py
# Topic: pytest - intentionally failing test
#
# test_method2 asserts 1-1 == 2 -> 0 == 2 is FALSE, so this test
# FAILS on purpose (shows you what a failure looks like).
# test_login asserts 1+1 == 2 -> passes.
# Run:  pytest test_181.py  (pytest shows the exact failing assert)

import pytest

@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2      # ❌ 0 == 2 -> this test FAILS

@pytest.mark.regression
def test_login():
    print("test2")
    assert 1 + 1 == 2    # ✅ passes