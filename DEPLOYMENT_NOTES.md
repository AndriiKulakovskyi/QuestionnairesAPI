# Deployment Notes - Render Docker Configuration

## Issues Fixed

### 1. ✅ Next.js Build Dependencies
**Problem:** Using `npm ci --only=production` excluded devDependencies (TypeScript, Tailwind) needed for building.  
**Fix:** Changed to `npm ci` and added `npm prune --production` after build.

### 2. ✅ Python Version Compatibility
**Problem:** `pyproject.toml` required Python ^3.12, but Debian 12 ships with Python 3.11.  
**Fix:** Relaxed Python requirement to `>=3.11,<4.0` in `pyproject.toml`.

### 3. ✅ Deprecated Poetry Flag
**Problem:** `--no-dev` flag is deprecated in Poetry 2.x.  
**Fix:** Changed to `--only=main`.

### 4. ✅ Missing Lock Files
**Problem:** `poetry.lock` and `package-lock.json` were in `.gitignore`.  
**Fix:** Removed from `.gitignore` and committed to repository.

### 5. ✅ API Routing
**Problem:** Health check endpoint at `/health` needed to be proxied through Next.js.  
**Fix:** Added comprehensive rewrites in `next.config.ts` for `/health`, `/api/*`, `/docs`, and `/openapi.json`.

### 6. ✅ Build Dependencies
**Problem:** Python packages might need C compiler.  
**Fix:** Added `build-essential` to Dockerfile.

## Files Modified

1. **Dockerfile** - Fixed npm install, Python version, Poetry flags, added build tools
2. **pyproject.toml** - Relaxed Python version requirement
3. **.gitignore** - Allowed `poetry.lock` and `package-lock.json`
4. **app/next.config.ts** - Added API rewrites for backend proxying
5. **supervisord.conf** - Added NODE_ENV environment variable

## Deployment Checklist

Before deploying to Render:

- [ ] Commit all changes
- [ ] Push to your repository
- [ ] Verify `poetry.lock` and `app/package-lock.json` are in the repo
- [ ] Connect repository to Render
- [ ] Render will auto-detect `render.yaml`
- [ ] Monitor build logs for any issues

## Architecture

```
Render (Port 10000)
    ↓
Next.js Server (Port 3000) ← Supervisor
    ↓ (rewrites)
Python FastAPI (Port 8000) ← Supervisor
```

## Potential Issues to Watch

### 1. Memory Limits on Free Tier
**Symptom:** Build or runtime OOM errors  
**Solution:** Render free tier has 512MB RAM. If builds fail:
- Consider using Render's build caching
- Optimize dependencies
- Upgrade to paid tier

### 2. Build Timeouts
**Symptom:** Build exceeds time limit  
**Solution:** 
- Optimize Dockerfile layer caching
- Consider pre-building and using Docker registry

### 3. Health Check Failures
**Symptom:** Service shows as unhealthy  
**Solution:** 
- Verify both services start properly
- Check `/health` endpoint returns 200
- Increase health check timeout in Render dashboard

### 4. Port Binding Issues
**Symptom:** Next.js can't bind to PORT  
**Solution:** 
- Verify PORT env variable is set (render.yaml has it)
- Check supervisord passes environment correctly

### 5. Poetry Installation Slow
**Symptom:** Poetry installation takes 30+ seconds  
**Solution:** This is normal, Poetry downloads and installs itself

### 6. npm prune Warnings
**Symptom:** Warnings during `npm prune --production`  
**Solution:** These are usually harmless, Next.js might warn about missing dev deps

## Testing Locally

To test the Docker build locally:

```bash
# Build the image
docker build -t questionnaires-app .

# Run the container
docker run -p 10000:10000 -e PORT=10000 questionnaires-app

# Test endpoints
curl http://localhost:10000/health
curl http://localhost:10000/api/auto/questionnaires
```

## Environment Variables in Production

Render automatically sets:
- `PORT=10000` (from render.yaml)
- `NODE_ENV=production` (from render.yaml)

If you need additional environment variables:
1. Add them in Render dashboard
2. Or add to `render.yaml` under `envVars`

## Monitoring After Deployment

Watch for:
1. Both processes starting (check logs for "nextjs" and "python")
2. Next.js listening on port from $PORT
3. Python API listening on port 8000
4. Health check responding at `/health`
5. API routes working at `/api/auto/*` and `/api/hetero/*`

## Rollback Strategy

If deployment fails:
1. Check Render logs for specific errors
2. Revert problematic commits
3. Push to trigger new deployment
4. Consider deploying to a test service first

## Future Optimizations

Consider for production:
1. Multi-stage Docker build to reduce final image size
2. Add redis/postgres if needed for caching/persistence
3. Implement proper logging and monitoring
4. Add rate limiting
5. Configure CORS properly (currently allows all origins)
6. Set up CI/CD pipeline for automated testing before deployment

