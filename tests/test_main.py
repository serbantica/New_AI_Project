"""Basic tests for the main module."""

import sys
import os
import pytest

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_main_function_exists():
    """Test that the main function exists and can be imported."""
    import main
    assert hasattr(main, 'main')
    assert callable(main.main)


def test_main_function_runs():
    """Test that the main function runs without errors."""
    import main
    # This should not raise an exception
    try:
        main.main()
    except SystemExit:
        # main() might call sys.exit(), which is fine
        pass


def test_project_structure():
    """Test that the project structure is in place."""
    # Check that key directories exist
    assert os.path.exists("src")
    assert os.path.exists("docs")
    assert os.path.exists("configs")
    assert os.path.exists("logs")
    
    # Check that main.py exists
    assert os.path.exists("main.py")
    
    # Check that pyproject.toml exists
    assert os.path.exists("pyproject.toml")
