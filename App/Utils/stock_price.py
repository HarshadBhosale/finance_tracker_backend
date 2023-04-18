from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import time


ssl._create_default_https_context = ssl._create_unverified_context
BASE_GOOGLE_FINANCE_URL = "https://www.google.com/finance/"
COMPANY_QUOTE_COMPONENT = "quote/"


def get_current_company_stock_price(company_code):
    req = Request(url=BASE_GOOGLE_FINANCE_URL + COMPANY_QUOTE_COMPONENT + company_code)
    webpage = urlopen(req).read().decode("UTF-8")
    soup = BeautifulSoup(webpage, "html.parser")
    t1 = time.time()
    data = {
        "code": "{}".format(company_code),
        "price": soup.find("div", class_="YMlKec fxKbKc").get_text().strip(),
    }
    x = time.time - t1
    data["website"] = "{0:.4f}".format(x)
    return data


def nse_formatter(x):
    try:
        return x.strip() + ":NSE"
    except:
        pass


def all_company_codes(file_path, column_name):
    return list(pd.read_excel(file_path)[column_name])


def get_all_nse_companies_current_prices():
    nse_codes = list(
        map(
            nse_formatter,
            all_company_codes(
                "/Users/cogoport/Desktop/finance_tracker_backend/MCAP31122022_3.xlsx",
                "Symbol",
            ),
        )
    )[:10]
    return nse_codes
