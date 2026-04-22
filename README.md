# Single-Service Railway Drawback Starter

This is the clean reset version.

## What this is
- One app
- One Railway web service
- One Railway Postgres database
- Frontend and backend live together in the same container

## What you do
1. Make a **new GitHub repo**
2. Upload these files to that repo
3. Go to Railway
4. Create a new project
5. Add **PostgreSQL**
6. Add a new service from your GitHub repo
7. Railway will build from the `Dockerfile`
8. In the backend service variables, add nothing unless you want to change defaults
9. Deploy
10. Open the Railway public URL
11. Press **Load sample leads**

## Why this version is easier
You do **not** need:
- Render Blueprint
- Vercel
- frontend URL variables
- CORS setup
- n8n on day one

## Folder map
- `app/` = Python backend
- `frontend/` = React/Vite frontend
- `Dockerfile` = builds frontend, then runs backend
- `railway.json` = tells Railway how to health-check the app

## Local test
If you want to test on your computer first:

### 1. Build the frontend
```bash
cd frontend
npm install
npm run build
cd ..
```

### 2. Start the app
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Open
- http://127.0.0.1:8000

## Railway kid-simple steps
### Step 1
Make a new empty GitHub repo.

### Step 2
Upload everything from this zip into that repo.

### Step 3
Go to Railway and click **New Project**.

### Step 4
Click **Provision PostgreSQL**.

### Step 5
Click **New Service** → **GitHub Repo** → choose your repo.

### Step 6
Wait for deploy.

### Step 7
Open your app URL.

### Step 8
Press **Load sample leads**.

## What works right now
- health check
- create leads
- list leads
- queue leads
- sample data loader
- database auto-create

## What you can add later
- real importer/exporter leads
- email sending
- broker partner handoff
- auth/login
- file uploads
- automation

## Common Railway settings
Usually Railway will inject `DATABASE_URL` automatically after you connect Postgres in the same project.

If your app ever says database error:
- make sure the Postgres service exists
- make sure your web service is in the same Railway project
- redeploy once after adding Postgres

## If you get stuck
Send me:
- screenshot of Railway service error
- build log
- deploy log
- runtime log

Then I can fix the exact next problem.
