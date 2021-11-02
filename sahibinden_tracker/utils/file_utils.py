import csv
import logging
from pathlib import Path


class FileUtils:
    @staticmethod
    def read_urls_from_file(file_path):
        try:
            url_list = []
            with open(file_path, 'r', encoding='UTF-8') as file:
                while line := file.readline().rstrip():
                    url_list.append(line)
            return url_list
        except Exception as e:
            logging.error("FileUtils.read_urls_from_file() | " + str(e))

    @staticmethod
    def write_to_csv(ready_to_csv):
        try:
            header = ready_to_csv.get('header', '')
            file_name = ready_to_csv.get('file_name', '')
            parsed_advert_info = ready_to_csv.get('parsed_advert_info', '')
            csv_file = Path(file_name)
            if csv_file.is_file():
                with open(file_name, 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(parsed_advert_info)
            else:
                with open(file_name, 'w', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerow(parsed_advert_info)
        except Exception as e:
            logging.error("FileUtils.write_to_csv() | " + str(e))
