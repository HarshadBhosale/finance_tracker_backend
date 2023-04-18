import peewee
import Database.Models.base_model


class Companies(Database.Models.base_model.BaseModel):
    code = peewee.CharField(unique=True)
    name = peewee.CharField(null=True)
    price = peewee.CharField(null=True)
    currency = peewee.CharField(null=True)
    market_capitalization = peewee.CharField(null=True)
    p_by_e_ratio = peewee.CharField(null=True)
    dividend_yield = peewee.CharField(null=True)
    website = peewee.CharField(null=True)


class CompaniesBalanceSheet(Database.Models.base_model.BaseModel):
    code = peewee.CharField(unique=True)
    price = peewee.CharField()
