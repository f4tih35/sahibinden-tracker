import logging
from sahibinden_tracker.utils.advert_utils import AdvertUtils
from sahibinden_tracker.utils.file_utils import FileUtils


def sahibinden_tracker(ad_url):
    try:
        advert_html = AdvertUtils.fetch_advert(ad_url)
        parsed_advert_info = AdvertUtils.parse_advert_to_list(advert_html)
        ready_to_csv = AdvertUtils.adv_list_to_csv(parsed_advert_info)
        FileUtils.write_to_csv(ready_to_csv)
    except Exception as e:
        logging.error("sahibinden_tracker() | " + str(e))
