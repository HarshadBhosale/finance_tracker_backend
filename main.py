from fastapi import FastAPI

finance_tracker_api = FastAPI()

@finance_tracker_api.get("/")
def mainAPI():
    return {"Finance Tracker API": "0.0.1"}