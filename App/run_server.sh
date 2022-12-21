export DATABASE_NAME="finance_tracker"
export DATABASE_USER_NAME="postgres"
export DATABASE_PASSWORD="cogoport"
export DATABASE_HOST="localhost"
export DATABASE_PORT=5432

uvicorn main:finance_tracker_api --reload
# uvicorn main:finance_tracker_api --host 0.0.0.0 --port 80 --reload