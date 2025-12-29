import pytest
import os
import glob
import io
import sys
from src.streamlang.main import run

# 1. Point to the new 'e2e' folder
# This finds tests/e2e/*.stream
CURRENT_DIR = os.path.dirname(__file__)
E2E_DIR = os.path.join(CURRENT_DIR, "e2e")
TEST_FILES = glob.glob(os.path.join(E2E_DIR, "*.stream"))

@pytest.mark.parametrize("file_path", TEST_FILES)
def test_stream_files(file_path):
    """
    Runs every .stream file in tests/e2e/
    """
    # A. Read the file
    with open(file_path, 'r') as f:
        code = f.read()

    # B. Parse EXPECT Header
    first_line = code.strip().split('\n')[0]
    
    # Skip files without EXPECT header (or fail them, your choice)
    if not first_line.startswith("// EXPECT:"):
        pytest.fail(f"File {os.path.basename(file_path)} missing // EXPECT header")
        
    expected_output = first_line.replace("// EXPECT:", "").strip()

    # C. Capture Output
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        run(code)
    except Exception as e:
        pytest.fail(f"Compiler Crashed: {e}")
    finally:
        sys.stdout = original_stdout

    # D. Assert
    actual_output = captured_output.getvalue()
    
    # Check if the expected output exists anywhere in the print log
    assert expected_output in actual_output, \
        f"\n❌ FAILED: {os.path.basename(file_path)}\nExpected: {expected_output}\nGot:\n{actual_output}"