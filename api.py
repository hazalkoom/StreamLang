from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import io
from src.streamlang.main import run

app = FastAPI()

class codeRequest(BaseModel):
    code: str

@app.post("/run")
async def run_streamlang(request: codeRequest):
    print(f"👉 Received Code: {request.code}", file=sys.stderr)
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        # pass the code string directly to the compiler's entry point
        run(request.code)
    except SystemExit:
        # If the compiler called sys.exit(1), it means there was an error
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        return {"status": "error", "output": output}
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        sys.stdout = sys.__stdout__

    return {"status": "success", "output": captured_output.getvalue()}