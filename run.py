import sys
from sahibinden_tracker.utils.command_line_utils import CommandLineUtils
import logging


def main():
    try:
        logging.basicConfig(level=logging.INFO)
        logging.info("Tracking started")
        if sys.argv[1] == '-u' and sys.argv[2]:
            CommandLineUtils.run_with_url(ad_url=sys.argv[2])
        elif sys.argv[1] == '-f' and sys.argv[2]:
            CommandLineUtils.run_with_file(file_path=sys.argv[2])
        logging.info("Tracking finished")
    except Exception as e:
        print('Usages: \npython run.py -u [url] or \npython run.py -f [file_path]')
        logging.error("main() | " + str(e))


if __name__ == '__main__':
    main()
