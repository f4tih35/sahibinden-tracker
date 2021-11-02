import logging
import time
from sahibinden_tracker.app import sahibinden_tracker
from sahibinden_tracker.utils.file_utils import FileUtils


class CommandLineUtils:
    @staticmethod
    def run_with_url(ad_url):
        try:
            logging.info(f'getting info started for: {ad_url}')
            sahibinden_tracker(ad_url)
            logging.info(f'getting info finished for: {ad_url}')
        except Exception as e:
            logging.error("CommandLineUtils.run_with_url() | " + str(e))

    @staticmethod
    def run_with_file(file_path):
        try:
            url_list = FileUtils.read_urls_from_file(file_path)
            for ad_url in url_list:
                logging.info(f'getting info started for: {ad_url}')
                sahibinden_tracker(ad_url)
                logging.info(f'getting info finished for: {ad_url}')
                time.sleep(10)
        except Exception as e:
            logging.error("CommandLineUtils.run_with_file() | " + str(e))
