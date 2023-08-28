import json
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup


class Table:
    def __init__(self) -> None:
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        self.scraped_date = f"{day}_{month}_{year}"

    def __get_names(self) -> pd.DataFrame:
        """Names of columns"""
        page = requests.get(url="https://csgo.steamanalyst.com/markets")
        soup = BeautifulSoup(page.text, "lxml")
        data = soup.find("table", id="pricelist").get_text().split("\n")
        return pd.DataFrame([x for x in data if x != '']).T

    def __get_values(self) -> pd.DataFrame:
        """Table with items"""
        headers = {
            'referer': 'https://csgo.steamanalyst.com/markets',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'draw': '1'}
        for index in range(0, 17):
            params[f'columns[{index}][data]'] = str(index)
            params[f'columns[{index}][name]'] = ''
            params[f'columns[{index}][searchable]'] = 'true'
            params[f'columns[{index}][orderable]'] = 'true'
            params[f'columns[{index}][search][value]'] = ''
            params[f'columns[{index}][search][regex]'] = 'false'
        params['order[0][column]'] = '0'
        params['order[0][dir]'] = 'asc' 
        params['start'] = '0'           
        params['length'] = '25'         
        params['search[value]'] = ''    
        params['search[regex]'] = 'false'
        params['custom_order'] = 'popular'
        params['token'] = ''            
        params['___'] = 'default'       
        response = requests.get(
            'https://csgo.steamanalyst.com/list-markets.php',
              headers=headers, 
              params=params
        )
        soup = BeautifulSoup(response.text, "lxml")
        raw_data = soup.find("p").get_text()
        data = json.loads(raw_data)
        data = data["data"]
        return pd.DataFrame(data)

    def get_table(self) -> pd.DataFrame:
        df = pd.concat(
            [
                self.__get_names(),
                self.__get_values()
            ],
        )
        return df.apply(lambda x: x.str.replace("</a>", ""))

    def save_to_csv(self, file_name: str) -> None:
        return self.get_table().to_excel(
            f"{file_name}_{self.scraped_date}.xlsx",
            index=False
        )

    def __str__(self) -> str:
        return self.get_table().to_string(index=False)
