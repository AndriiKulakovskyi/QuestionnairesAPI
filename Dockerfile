# Start from Node.js 20 slim image (required by Next.js 16+)
FROM node:20-slim

# Set working directory
WORKDIR /app

# Install Python 3.11 (available in Debian 12), pip, supervisor, and build dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    supervisor \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy frontend package files and install dependencies
WORKDIR /app/frontend
COPY app/package*.json ./
RUN npm ci

# Copy all Next.js source files
COPY app/ .

# Build Next.js application
RUN npm run build

# Remove devDependencies to reduce image size
RUN npm prune --production

# Switch to app root directory
WORKDIR /app

# Copy Python project files
COPY pyproject.toml poetry.lock ./
COPY questionnaires/ ./questionnaires/
COPY api/ ./api/
COPY run_api.py ./

# Configure Poetry to not create virtual environment (since we're in a container)
RUN poetry config virtualenvs.create false

# Install Python dependencies (only main/production dependencies)
# Use --no-root to skip installing the project package itself
RUN poetry install --only=main --no-interaction --no-ansi --no-root

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 10000 (Render's default port)
EXPOSE 10000

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

