import logging
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class AdvertUtils:
    @staticmethod
    def fetch_advert(url):
        try:
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
            response = requests.get(url, headers=header)
            if response.status_code != 200:
                raise Exception("AdvertUtils.fetch_advert() | Response status code is not 200")
            return response.text
        except Exception as e:
            logging.error("AdvertUtils.fetch_advert() | " + str(e))

    @staticmethod
    def parse_advert_to_list(html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find("div", {"class": "classifiedInfo"}).find('h3').next.strip()
            parsed_advert_info = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), price]
            for rows in soup.find_all("ul", {"class": "classifiedInfoList"}):
                for item in rows.find_all("span"):
                    parsed_advert_info.append(item.text.strip())
            return parsed_advert_info
        except Exception as e:
            logging.error("AdvertUtils.parse_advert_to_list() | " + str(e))

    @staticmethod
    def adv_list_to_csv(parsed_advert_info):
        try:
            header = ['update_date', 'price', 'ad_num', 'ad_date', 'make', 'series',
                      'model', 'year', 'fuel', 'gear', 'km', 'body_type', 'engine_power',
                      'engine_capacity', 'wheel_drive', 'color', 'warranty', 'plate',
                      'from', 'visible_via_video_call', 'exchangeable', 'condition']
            file_name = f'sahibinden_tracking_items/{parsed_advert_info[4]}-{parsed_advert_info[5]}-{parsed_advert_info[6]}-{parsed_advert_info[2]}.csv'
            return {'header': header, 'file_name': file_name, 'parsed_advert_info': parsed_advert_info}
        except Exception as e:
            logging.error("AdvertUtils.adv_list_to_csv() | " + str(e))
