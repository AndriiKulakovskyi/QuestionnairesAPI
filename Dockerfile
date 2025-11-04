# Start from Node.js 18 slim image
FROM node:18-slim

# Set working directory
WORKDIR /app

# Install Python 3.12, pip, supervisor, and other dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    supervisor \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy frontend package files
COPY app/package*.json ./app/

# Install frontend dependencies
WORKDIR /app/app
RUN npm ci --only=production

# Copy frontend source
COPY app/ ./

# Build Next.js application
RUN npm run build

# Switch back to root directory for backend
WORKDIR /app

# Copy Python project files
COPY pyproject.toml poetry.lock ./
COPY questionnaires/ ./questionnaires/
COPY api/ ./api/
COPY run_api.py ./

# Configure Poetry to not create virtual environment (since we're in a container)
RUN poetry config virtualenvs.create false

# Install Python dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 10000 (Render's default port)
EXPOSE 10000

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

