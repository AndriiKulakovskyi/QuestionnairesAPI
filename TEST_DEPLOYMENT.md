# Deployment Testing Guide

## After Latest Deployment, Test These:

### 1. Check Python Backend Directly
```bash
# Replace YOUR-APP-URL with your Render URL
curl https://YOUR-APP-URL:8000/health
# Expected: Should fail (port 8000 not exposed externally)

# Try through the main port
curl https://YOUR-APP-URL/health
# Expected: Should return {"status": "healthy", ...}
```

### 2. Check if Next.js is Loading Config
Open browser console on https://YOUR-APP-URL and look for:
```
[API Client] Fetching from: /api/auto/questionnaires
```

If you see an empty string or wrong URL, the config isn't loading.

### 3. Check Network Tab
- Open browser DevTools → Network tab
- Visit your app
- Look for request to `/api/auto/questionnaires`
- Check:
  - Status code (should be 200)
  - Response (should be JSON array)
  - If it's hitting the right endpoint

### 4. Test API Endpoints Directly
```bash
# Test health endpoint
curl https://YOUR-APP-URL/health

# Test API endpoint
curl https://YOUR-APP-URL/api/auto/questionnaires

# Test docs
curl https://YOUR-APP-URL/docs
```

## Common Issues

### Issue: "fetch failed" 
**Cause**: Next.js rewrites not working
**Debug**: Check if TypeScript is installed (needed for next.config.ts)
**Fix**: Added `npm install typescript` after pruning

### Issue: API returns 404
**Cause**: Python backend not running
**Debug**: Check Render logs for "🚀 Questionnaires API started"
**Fix**: Should be running, check supervisord logs

### Issue: CORS errors
**Cause**: Backend not allowing frontend origin
**Debug**: Should not happen (CORS allows all origins)
**Fix**: Already configured

### Issue: Connection refused
**Cause**: Backend on wrong host/port
**Debug**: Check if Python is on 0.0.0.0:8000
**Fix**: Already configured in run_api.py

