from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import sys
import io
import contextlib
import traceback

# Import your engine
try:
    from src.streamlang.main import run
except ImportError:
    # Fallback if import fails (so API doesn't crash on startup)
    def run(code): raise ImportError("Could not import src.streamlang.main.run")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/run")
async def run_streamlang(request: CodeRequest):
    # Capture output safely
    output_buffer = io.StringIO()
    
    try:
        # redirect_stdout automatically restores stdout when done or if error occurs
        with contextlib.redirect_stdout(output_buffer):
            run(request.code)
            
        # If we get here, it worked
        return {"status": "success", "output": output_buffer.getvalue()}

    except Exception as e:
        # Captures language errors (e.g. "Function 'add' not found")
        # We return 200 OK so the frontend gets the JSON error message
        return {
            "status": "error", 
            "output": f"{str(e)}"
        }
        
    except BaseException as e:
        # Captures SystemExit or KeyboardInterrupt
        return {
            "status": "error", 
            "output": f"Critical Failure: {str(e)}"
        }

# Serve frontend
if os.path.isdir("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")