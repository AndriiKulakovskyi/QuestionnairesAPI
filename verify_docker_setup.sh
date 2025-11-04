#!/bin/bash
# Verification script for Docker setup

echo "🔍 Verifying Docker Configuration..."
echo ""

# Check if required files exist
echo "📁 Checking required files..."

files=(
    "Dockerfile"
    "supervisord.conf"
    "render.yaml"
    ".dockerignore"
    "app/package.json"
    "app/package-lock.json"
    "pyproject.toml"
    "poetry.lock"
    "run_api.py"
    "api/main.py"
    "app/next.config.ts"
)

all_exist=true
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file - MISSING!"
        all_exist=false
    fi
done

echo ""
echo "📂 Checking directory structure..."

dirs=(
    "app/app"
    "app/app/lib"
    "questionnaires"
    "api"
)

for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✅ $dir/"
    else
        echo "  ❌ $dir/ - MISSING!"
        all_exist=false
    fi
done

echo ""
echo "🔧 Checking critical configurations..."

# Check if poetry.lock is NOT in .gitignore
if grep -q "^poetry.lock$" .gitignore 2>/dev/null; then
    echo "  ❌ poetry.lock is still ignored in .gitignore!"
    all_exist=false
else
    echo "  ✅ poetry.lock is not ignored"
fi

# Check if package-lock.json is NOT ignored
if grep -q "^!package-lock.json$" .gitignore 2>/dev/null; then
    echo "  ✅ package-lock.json is allowed in .gitignore"
else
    echo "  ⚠️  package-lock.json might be ignored"
fi

# Check Dockerfile has Node 20
if grep -q "FROM node:20" Dockerfile; then
    echo "  ✅ Dockerfile uses Node.js 20"
else
    echo "  ❌ Dockerfile doesn't use Node.js 20!"
    all_exist=false
fi

# Check supervisord paths
if grep -q "directory=/app/frontend" supervisord.conf; then
    echo "  ✅ Supervisord configured for /app/frontend"
else
    echo "  ❌ Supervisord nextjs directory incorrect!"
    all_exist=false
fi

if grep -q "directory=/app" supervisord.conf | tail -1; then
    echo "  ✅ Supervisord configured for /app (Python)"
else
    echo "  ❌ Supervisord python directory incorrect!"
    all_exist=false
fi

# Check Python version in pyproject.toml
if grep -q "requires-python.*3.11" pyproject.toml; then
    echo "  ✅ Python version allows 3.11"
else
    echo "  ⚠️  Python version might not allow 3.11"
fi

# Check Next.js rewrites
if grep -q "/health" app/next.config.ts && grep -q "/api/" app/next.config.ts; then
    echo "  ✅ Next.js rewrites configured"
else
    echo "  ❌ Next.js rewrites might be missing!"
    all_exist=false
fi

echo ""
if [ "$all_exist" = true ]; then
    echo "✅ All checks passed! Docker setup is ready."
    echo ""
    echo "📋 Next steps:"
    echo "  1. Commit all changes: git add -A"
    echo "  2. Commit: git commit -m 'Complete Docker configuration'"
    echo "  3. Push: git push origin main"
    echo "  4. Deploy on Render!"
    exit 0
else
    echo "❌ Some checks failed. Please fix the issues above."
    exit 1
fi

