# 1. Use Python 3.10
FROM python:3.10-slim

# 2. Create a non-root user 'user' with ID 1000
RUN useradd -m -u 1000 user

# 3. Set working directory
WORKDIR /app

# 4. Copy project files
COPY pyproject.toml .
COPY src/ src/

# 5. Copy the static frontend files (Owned by 'user')
COPY --chown=user ./static /app/static

# 6. Install dependencies
RUN pip install --no-cache-dir .
RUN pip install --no-cache-dir fastapi uvicorn requests

# 7. Copy the API entry point
COPY api.py .

# 8. Switch to the non-root user
USER user

# 9. Set PATH so we can run uvicorn
ENV PATH="/home/user/.local/bin:$PATH"

# 10. Expose port and run
EXPOSE 7860
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]