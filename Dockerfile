FROM python:3.11-slim

WORKDIR /app

# Set environment variable to indicate container environment
ENV IS_DEVCONTAINER=true

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Command to run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]