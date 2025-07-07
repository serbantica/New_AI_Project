"""
Test the Streamlit Charter Tool application
"""

import pytest
import sys
import os
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_streamlit_app_imports():
    """Test that the Streamlit app can be imported without errors"""
    # This test just checks if the file can be imported
    # Since streamlit apps are scripts, we can't easily import them
    # But we can check if the file exists and is valid Python
    
    app_path = Path("streamlit_app.py")
    assert app_path.exists(), "streamlit_app.py should exist"
    
    # Check if it's valid Python syntax
    with open(app_path, 'r') as f:
        content = f.read()
    
    # Compile the code to check for syntax errors
    try:
        compile(content, str(app_path), 'exec')
    except SyntaxError as e:
        pytest.fail(f"streamlit_app.py has syntax errors: {e}")

def test_required_files_exist():
    """Test that all required files for the charter tool exist"""
    required_files = [
        "streamlit_app.py",
        "run_streamlit.sh",
        "STREAMLIT_README.md",
        "example_usage.py",
        "demo_charter_tool.sh",
        "requirements.txt"
    ]
    
    for file_path in required_files:
        assert Path(file_path).exists(), f"{file_path} should exist"

def test_makefile_has_streamlit_command():
    """Test that the makefile includes the streamlit command"""
    makefile_path = Path("makefile")
    assert makefile_path.exists(), "makefile should exist"
    
    with open(makefile_path, 'r') as f:
        content = f.read()
    
    assert "streamlit:" in content, "makefile should contain streamlit command"

def test_requirements_has_streamlit():
    """Test that requirements.txt includes streamlit"""
    requirements_path = Path("requirements.txt")
    assert requirements_path.exists(), "requirements.txt should exist"
    
    with open(requirements_path, 'r') as f:
        content = f.read()
    
    assert "streamlit" in content.lower(), "requirements.txt should include streamlit"

def test_example_usage_file():
    """Test that example_usage.py can be imported"""
    example_path = Path("example_usage.py")
    assert example_path.exists(), "example_usage.py should exist"
    
    # Check if it's valid Python syntax
    with open(example_path, 'r') as f:
        content = f.read()
    
    try:
        compile(content, str(example_path), 'exec')
    except SyntaxError as e:
        pytest.fail(f"example_usage.py has syntax errors: {e}")

def test_shell_scripts_are_executable():
    """Test that shell scripts have executable permissions"""
    scripts = [
        "run_streamlit.sh",
        "demo_charter_tool.sh",
        "project_bootstrap.sh",
        "validate_bootstrap.sh"
    ]
    
    for script in scripts:
        script_path = Path(script)
        if script_path.exists():
            # Check if file has executable permissions
            stat = script_path.stat()
            is_executable = bool(stat.st_mode & 0o111)
            assert is_executable, f"{script} should be executable"

if __name__ == "__main__":
    # Run the tests
    test_streamlit_app_imports()
    test_required_files_exist()
    test_makefile_has_streamlit_command()
    test_requirements_has_streamlit()
    test_example_usage_file()
    test_shell_scripts_are_executable()
    
    print("✅ All charter tool tests passed!")
