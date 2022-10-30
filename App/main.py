import fastapi
from Database.Interactions.Users.delete_user_profile import deleteUserProfile
from Database.Interactions.Users.get_user_profile import getUserProfile
from Database.Interactions.Users.login_user_profile import loginUserProfile
from Database.Interactions.Users.get_user_stats import getUserStats
from Database.Interactions.Users.get_user_visual_stats import getUserVisualStats
from Database.Interactions.Users.register_user import registerUser
from Database.Interactions.Users.update_user_profile import updateUserProfile
from Database.Interactions.Users.update_user_profile_password import updateUserProfilePassword
from Database.Interactions.Transactions.get_user_all_transactions import getUserAllTransactions
from Database.Interactions.Transactions.create_user_transaction import createUserTransaction
from Database.Interactions.Transactions.get_user_transaction import getUserTransaction
from Database.Interactions.Transactions.update_user_transaction import updateUserTransaction
from Database.Interactions.Transactions.delete_user_transaction import deleteUserTransaction
from Database.Models.users import UserModel
from Database.Models.transactions import TransactionModel
from Database.database import database
from fastapi.middleware.cors import CORSMiddleware
from Database.Migrations.create_tables import create_not_existence_tables

finance_tracker_api = fastapi.FastAPI()

origins = [
    "http://localhost:3000/",
]

finance_tracker_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@finance_tracker_api.on_event("startup")
def startup_event():
    create_not_existence_tables()
    if database.is_closed():
        database.connect()

@finance_tracker_api.on_event("shutdown")
def shutdown_event():
    if not database.is_closed():
        database.close()

@finance_tracker_api.get("/")
def root():
    version = "1.1.0"
    return {"Finance Tracker API" : version}



@finance_tracker_api.post("/users/create")
def createUser(user: UserModel):
    return registerUser(user)

@finance_tracker_api.post("/users/login")
def loginUser(login_object: dict):
    return loginUserProfile(login_object)

@finance_tracker_api.post("/users/get")
def getUser(get_object: dict):
    return getUserProfile(get_object)

@finance_tracker_api.post("/users/get/stats")
def getStats(get_user_stats_object: dict):
    return getUserStats(get_user_stats_object)

@finance_tracker_api.post("/users/get/stats/visual")
def getVisualStats(get_user_visual_stats_object: dict):
    return getUserVisualStats(get_user_visual_stats_object)

@finance_tracker_api.post("/users/update")
def updateUser(update_user_object: dict):
    return updateUserProfile(update_user_object)

@finance_tracker_api.post("/users/update/password")
def updateUserPassword(update_user_password_object: dict):
    return updateUserProfilePassword(update_user_password_object)

@finance_tracker_api.post("/users/delete")
def deleteUser(delete_user_object: dict):
    return deleteUserProfile(delete_user_object)


@finance_tracker_api.post("/transactions")
def getAllTransactions(get_all_transactions_object: dict):
    return getUserAllTransactions(get_all_transactions_object)

@finance_tracker_api.post("/transactions/create")
def createTransaction(create_transaction_object: TransactionModel):
    return createUserTransaction(create_transaction_object)

@finance_tracker_api.post("/transactions/get")
def getTransaction(get_transaction_object: dict):
    return getUserTransaction(get_transaction_object)

@finance_tracker_api.post("/transactions/update")
def updateTransaction(update_transaction_object: dict):
    return updateUserTransaction(update_transaction_object)

@finance_tracker_api.post("/transactions/delete")
def deleteTransaction(delete_transaction_object: dict):
    return deleteUserTransaction(delete_transaction_object)