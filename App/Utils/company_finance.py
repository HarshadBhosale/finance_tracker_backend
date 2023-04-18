from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
BASE_GOOGLE_FINANCE_URL = "https://www.google.com/finance/"
COMPANY_QUOTE_COMPONENT = "quote/"

month_in_num = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "june": 6,
    "jul": 7,
    "aug": 8,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}

primary_properties = {
    "Dividend yield": "dividend_yield",
    "P/E ratio": "p_by_e_ratio",
    "Website": "website",
    "Market cap": "market_capitalization",
}


def value_handler(arr, ind, len):
    if len >= (ind + 1) and arr[ind]:
        return "{}".format(float(arr[ind]))
    else:
        return float(0)


def get_company_data(rawData):
    l = len(rawData)
    i = 0
    data = {}

    while i < (l - 2):
        first, second, third = rawData[i], rawData[i + 1], rawData[i + 2]
        l1 = len(first)
        l2 = len(second)
        if first[0] == second[0]:
            if (
                (int(second[0]) == 1 + int(third[0]))
                and second[1] == third[1]
                and second[2] == third[2]
                and l1 >= 18
                and l2 >= 21
            ):

                data["{}-{}".format(int(first[0]) - 1, int(first[0]))] = data.get(
                    "{}-{}".format(int(first[0]) - 1, int(first[0])), {}
                ) | {
                    "revenue": value_handler(first, 1, l1),
                    "net_income": value_handler(first, 2, l1),
                    "net_profit_margin": value_handler(first, 4, l1),
                    "net_change_in_cash": value_handler(first, 6, l1),
                    "earnings_per_share": value_handler(first, 10, l1),
                    "currency": "{}".format(first[17]),
                    "return_on_capital": value_handler(second, 3, l2),
                    "operating_expense": value_handler(second, 4, l2),
                    "ebitda": value_handler(second, 5, l2),
                    "effective_tax_rate": value_handler(second, 6, l2),
                    "cash_and_short_term_investments": value_handler(second, 7, l2),
                    "total_assets": value_handler(second, 8, l2),
                    "total_equity": value_handler(second, 10, l2),
                    "total_liabilities": value_handler(second, 11, l2),
                    "shares_outstanding": value_handler(second, 12, l2),
                    "cash_from_operations": value_handler(second, 13, l2),
                    "cash_from_investing": value_handler(second, 14, l2),
                    "cash_from_financing": value_handler(second, 15, l2),
                    "free_cash_flow": value_handler(second, 16, l2),
                    "return_on_assets": value_handler(second, 19, l2),
                    "price_to_book": value_handler(second, 20, l2),
                }
        i += 1
    return data


def company_data(company_code):
    req = Request(url=BASE_GOOGLE_FINANCE_URL + COMPANY_QUOTE_COMPONENT + company_code)
    webpage = urlopen(req).read().decode("UTF-8")
    soup = BeautifulSoup(webpage, "html.parser")
    data = {"google_symbol": company_code}
    data["company_name"] = soup.find("div", class_="zzDege").get_text().strip()
    for i in soup.find_all("div", class_="gyFHrc"):
        prop_val = i.get_text(">").split(">")
        prop, val = prop_val[0].strip(), prop_val[-1].strip()
        if prop in primary_properties:
            if prop == "Market cap":
                val, data["currency"] = val.split()
            data[primary_properties[prop]] = val

    script = soup.find(
        lambda tag: tag.name == "script" and "key: 'ds:13'" in tag.get_text()
    )
    prev_ind = -1
    rawData = []
    st = (
        script.get_text()[
            script.get_text().index("data:")
            + 5 : script.get_text().index("sideChannel")
            - 3
        ]
        .replace('"', "")
        .split(",")
    )
    for ind, elem in enumerate(st):
        st[ind] = elem.strip("]").strip("[").strip("null")
        if len(st[ind]) == 4 and "." not in st[ind]:
            if prev_ind != -1:
                rawData.append(st[prev_ind:ind])
            prev_ind = ind

    # data["financial_data"] = get_company_data(rawData)
    return data
