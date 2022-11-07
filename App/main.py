import fastapi
from Database.Interactions.Users.disable_user_profile import disableUserProfile
from Database.Interactions.Users.user_profile import userProfile
from Database.Interactions.Users.user_signin import userSignIn
from Database.Interactions.Users.user_stats import userStats
from Database.Interactions.Users.user_graphics import userGraphics
from Database.Interactions.Users.user_signup import userSignUp
from Database.Interactions.Users.update_user_profile import updateUserProfile
from Database.Interactions.Users.update_user_password import updateUserPassword
from Database.Interactions.Transactions.get_user_transactions import getUserTransactions
from Database.Interactions.Transactions.create_user_transaction import createUserTransaction
from Database.Interactions.Transactions.get_user_transaction import getUserTransaction
from Database.Interactions.Transactions.get_user_transaction_years import getUserTransactionYears
from Database.Interactions.Transactions.update_user_transaction import updateUserTransaction
from Database.Interactions.Transactions.disable_user_transaction import disableUserTransaction
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
    version = "1.2.0"
    return {"Finance Tracker API" : version}



@finance_tracker_api.post("/signup")
def signUp(user: UserModel):
    return userSignUp(user)

@finance_tracker_api.post("/signin")
def signIn(signin_object: dict):
    return userSignIn(signin_object)

@finance_tracker_api.post("/profile")
def profile(profile_object: dict):
    return userProfile(profile_object)

@finance_tracker_api.post("/stats")
def stats(stats_object: dict):
    return userStats(stats_object)

@finance_tracker_api.post("/graphics")
def graphics(graphics_object: dict):
    return userGraphics(graphics_object)

@finance_tracker_api.post("/update/profile")
def updateProfile(update_profile_object: dict):
    return updateUserProfile(update_profile_object)

@finance_tracker_api.post("/update/password")
def updatePassword(update_password_object: dict):
    return updateUserPassword(update_password_object)

@finance_tracker_api.post("/disable/profile")
def disableProfile(disable_profile_object: dict):
    return disableUserProfile(disable_profile_object)


@finance_tracker_api.post("/transactions")
def getTransactions(get_transactions_object: dict):
    return getUserTransactions(get_transactions_object)

@finance_tracker_api.post("/create/transaction")
def createTransaction(transaction: TransactionModel):
    return createUserTransaction(transaction)

@finance_tracker_api.post("/get/transaction")
def getTransaction(get_transaction_object: dict):
    return getUserTransaction(get_transaction_object)

@finance_tracker_api.post("/get/transaction/years")
def getTransactionYears(get_transaction_years_object: dict):
    return getUserTransactionYears(get_transaction_years_object)

@finance_tracker_api.post("/update/transaction")
def updateTransaction(update_transaction_object: dict):
    return updateUserTransaction(update_transaction_object)

@finance_tracker_api.post("/disable/transaction")
def disableTransaction(disable_transaction_object: dict):
    return disableUserTransaction(disable_transaction_object)