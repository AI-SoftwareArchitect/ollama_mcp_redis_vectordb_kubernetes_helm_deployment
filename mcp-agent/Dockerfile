# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install system dependencies (curl for Ollama installation)
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://ollama.com/install.sh | sh \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 8080

# Run Ollama and the app
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull deepseek-coder:latest && uvicorn main:app --host 0.0.0.0 --port 8080"]
