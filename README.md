# Freelance Scrapper
Get notifications of new job offers as soon as they appear at website https://freelance.ru directly to your telegram chat.
You can tune which sections you want to track.

![Language](https://img.shields.io/badge/language-Python-green.svg)&nbsp;

## Technology stack: 
* Python3
* Scrapy
* Json
* Telegram


## How to launch project:


**Clone repository by command:**
```
git clone
```

**Install and activate virtual environment:**
```
python -m venv venv
source venv/Scripts/activate 
```

**Install modules from requirements.txt:**
```
pip install -r requirements.txt
```

**Create .env file in directory freelancescrapper and define following variables in it:**
```
TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=
```

**Last steps:**

``` 
- Uncomment SEARCH_CONDITIONS sections needed to be tracked in settings
- Launch tracking by command:
python parcing.py
```
