import pytest
import os
import io
import sys
from streamlang.main import run

def discover_tests(base_path):
    """Recursively finds all .stream files in a directory."""
    test_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".stream"):
                # Return the full path so the runner can find it
                test_files.append(os.path.join(root, file))
    return sorted(test_files)

# Discover the two groups of tests
E2E_FILES = discover_tests("tests/e2e")
NEGATIVE_FILES = discover_tests("tests/negative")

@pytest.mark.parametrize("file_path", E2E_FILES)
def test_e2e_success(file_path):
    """Tests that must run to completion and print 'Done'."""
    with open(file_path, 'r') as f:
        code = f.read()
    
    captured_out = io.StringIO()
    sys.stdout = captured_out
    
    try:
        # These should NOT raise any exceptions
        run(code)
        output = captured_out.getvalue()
        assert "✅ Done." in output
    finally:
        sys.stdout = sys.__stdout__

@pytest.mark.parametrize("file_path", NEGATIVE_FILES)
def test_negative_failures(file_path):
    """Tests that must crash or call sys.exit(1)."""
    with open(file_path, 'r') as f:
        code = f.read()

    captured_out = io.StringIO()
    sys.stdout = captured_out

    try:
        # We EXPECT a crash or a SystemExit(1)
        with pytest.raises((SystemExit, Exception)):
            run(code)
        
        output = captured_out.getvalue()
        # Verify it didn't sneak through to the end
        assert "✅ Done." not in output
    finally:
        sys.stdout = sys.__stdout__