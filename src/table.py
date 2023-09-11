import json
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup

from utils.request import params


class Table:
    def __init__(self) -> None:
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        self.scraped_date = f"{day}_{month}_{year}"

    def __get_names(self) -> pd.DataFrame:
        page = requests.get(url="https://csgo.steamanalyst.com/markets")
        soup = BeautifulSoup(page.text, "lxml")
        data = soup.find("table", id="pricelist").get_text().split("\n")
        return pd.DataFrame([x for x in data if x != '']).T

    def __get_values(self) -> pd.DataFrame:
        headers = {
            'referer': 'https://csgo.steamanalyst.com/markets',
            'x-requested-with': 'XMLHttpRequest',
        }
        response = requests.get(
            'https://csgo.steamanalyst.com/list-markets.php',
            headers=headers, 
            params=params(),
        )
        soup = BeautifulSoup(response.text, "lxml")
        raw_data = soup.find("p").get_text()
        data = json.loads(raw_data)["data"]
        return pd.DataFrame(data)

    def get_table(self) -> pd.DataFrame:
        table = self.__get_values()
        table.columns = self.__get_names().iloc[0]
        return table.apply(lambda x: x.str.replace("</a>", ""))

    def save_to_csv(self, file_name: str) -> None:
        self.get_table().to_excel(
            f"{file_name}_{self.scraped_date}.xlsx",
            index=False,
        )

    def __str__(self) -> str:
        return self.get_table().to_string(index=False)
