export DATABASE_NAME="db_name"
export DATABASE_USER_NAME="db_user"
export DATABASE_PASSWORD="db_pwd"
export DATABASE_HOST="localhost or db_host"
export DATABASE_PORT="5432 or db_port"

uvicorn main:finance_tracker_api --reload
# uvicorn main:finance_tracker_api --host 0.0.0.0 --port 80 --reload