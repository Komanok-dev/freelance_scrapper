import json
import os
from time import sleep

import requests

from freelancescrapper.settings import (REFRESH_INTERVAL, STORE_JOBS_FILE,
                                        TELEGRAM_CHAT_ID, TELEGRAM_TOKEN)


def send_message(message):
    requests.get(
        f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?'
        f'chat_id={TELEGRAM_CHAT_ID}&parse_mode=Markdown&text={message}'
    )


def read_latest_job():
    f = open(STORE_JOBS_FILE, encoding='utf-8')
    return json.load(f)


def crawl_new_jobs():
    os.system(f'scrapy crawl freelance -O {STORE_JOBS_FILE}')


def main():
    old = read_latest_job()

    while True:
        message = ''
        crawl_new_jobs()
        new = read_latest_job()
        if old != new:
            for job in new:
                if job not in old:
                    message += f'{job["name"]}\n---------------------------\n'
            old = new
        if message:
            send_message(message)
            print(message)
        print('\n\n\nLooking for new jobs...')
        sleep(REFRESH_INTERVAL)


if __name__ == '__main__':
    main()
