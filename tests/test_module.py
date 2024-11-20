"""Example test module
"""
from ansible_deploy_service import main

def test_example_function():
    """Tests that the example function completes successfully
    """
    main.example_function()
    assert True

def test_example_return():
    """Tests that the function returns something
    """
    retval = main.example_returning_function()
    assert retval is not None
