from database import Users, Transactions

for table in [Users, Transactions]:
    table.create_table()
