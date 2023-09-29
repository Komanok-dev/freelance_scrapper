import scrapy

from freelancescrapper.settings import SEARCH_CONDITIONS


class FreelanceSpider(scrapy.Spider):
    name = 'freelance'

    conditions = ''
    for condition in SEARCH_CONDITIONS:
        conditions += '&c%5B%5D=' + condition
    start_urls = [f'https://freelance.ru/project/search/pro?c=&\
                  {conditions}&q=&m=or&e=&a=0&v=0&f=&t=&o=0&o=1&b=']

    def parse(self, response):
        for prj in response.css('div.project'):
            yield {
                'name': prj.css('h2.title').attrib['title'],
                'description': prj.css('a.description::text').get().strip(),
                'link': prj.css('h2.title').css('a').attrib.get('href'),
                'datetime': prj.css('time').attrib.get('datetime'),
            }
