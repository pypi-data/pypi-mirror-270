"""
Test main module
"""

from mesogate_router.main import run


def test_main():
    """
    Ensure that main starts
    """
    result = run()
    assert result
