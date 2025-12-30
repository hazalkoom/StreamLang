import pytest
import os
import glob
import io
import sys
from src.streamlang.main import run

CURRENT_DIR = os.path.dirname(__file__)
ERROR_DIR = os.path.join(CURRENT_DIR, "errors")
ERROR_FILES = glob.glob(os.path.join(ERROR_DIR, "*.stream"))

@pytest.mark.parametrize("file_path", ERROR_FILES)
def test_error_files(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        run(code)
    except (Exception, SystemExit): 
        # CATCH EVERYTHING. 
        # If the compiler crashes (Exception) or quits (SystemExit), that is GOOD.
        pass
    finally:
        sys.stdout = original_stdout

    actual_output = captured_output.getvalue()
    
    # Check 1: It must NOT say "Done"
    assert "✅ Done." not in actual_output, \
        f"\n❌ FAILED: {os.path.basename(file_path)}\nIt printed 'Done' but should have crashed!\nOutput:\n{actual_output}"

    # Check 2: It MUST say "Error" or "CRASH"
    error_keywords = ["Error", "Undefined", "mismatched input", "extraneous input", "CRASH", "Type Error"]
    found_error = any(k in actual_output for k in error_keywords)
    
    assert found_error, \
        f"\n❌ FAILED: {os.path.basename(file_path)}\nExpected error message, got nothing.\nOutput:\n{actual_output}"