# Scrapy settings for freelancescrapper project

import os

from dotenv import load_dotenv

load_dotenv()

BOT_NAME = "freelancescrapper"

SPIDER_MODULES = ["freelancescrapper.spiders"]
NEWSPIDER_MODULE = "freelancescrapper.spiders"

# Set telegram bot token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', default='')

# Set telegram chat ID
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', default='')

# Set file name where jobs list to be stored
STORE_JOBS_FILE = 'jobs.json'

# Set refresh interval in seconds
REFRESH_INTERVAL = 60

# Uncomment sections needed for tracking
SEARCH_CONDITIONS = {
    # '577': '3D графика',
    # '696': 'Crypto/NFT',
    # '590': 'Арт / Иллюстрации / Анимация',
    # '580': 'Архитектура / предметы интерьера',
    # '133': 'Аутсорсинг / Консалтинг / Менеджмент',
    # '663': 'Бытовые услуги / Обучение',
    # '116': 'Веб разработка',
    # '565': 'Видео',
    # '40': 'Графический дизайн',
    # '186': 'Инженерия',
    # '673': 'Интернет продвижение и реклама',
    # '117': 'Классическая реклама и маркетинг',
    # '89': 'Музыка / Звук',
    # '716': 'Направления отраслевого Дизайна',
    # '29': 'Переводы',
    '4': 'Программирование и IT',
    # '124': 'Тексты',
    # '98': 'Фотография',
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
