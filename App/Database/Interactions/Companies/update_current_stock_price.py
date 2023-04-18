from Database.Models.company import Companies
from Utils.stock_price import (
    get_all_nse_companies_current_prices,
    get_current_company_stock_price,
)
from concurrent.futures import ThreadPoolExecutor
import time


def hl(c):
    time.sleep(0.1)
    i = get_current_company_stock_price(c)
    Companies.create(**i)


def update_current_stock_price():
    with ThreadPoolExecutor(100) as executor:
        executor.map(hl, get_all_nse_companies_current_prices())
