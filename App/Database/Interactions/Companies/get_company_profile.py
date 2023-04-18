from Database.Models.company import Companies
from Utils.company_finance import company_data


def hl(c):
    x = company_data(c)
    try:
        Companies.update(
            name=x["company_name"],
            currency=x["currency"],
            market_capitalization=x["market_capitalization"],
            p_by_e_ratio=x["p_by_e_ratio"],
            dividend_yield=x["dividend_yield"],
            website=x["website"],
        ).where(Companies.code == c).execute()
    except:
        print(c)


def get_company_profile():
    map(hl, list(map(lambda y: y.code, Companies.select(Companies.code))))
