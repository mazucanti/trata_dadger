#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:42:38 2020

@author: mazucanti
"""


import scrapy
import datetime as dt
from scrapy.loader import ItemLoader
from ccee_crawl.items import CceeCrawlItem

hoje = dt.date.today()
prox_sexta = hoje - dt.timedelta(days=(5 - int(hoje.isoweekday())))
INFOS = (prox_sexta.year, '0'+str(hoje.month) if hoje.month < 10 else str(hoje.month))


class Ccee_Spider(scrapy.Spider):

    name = "ccee_spider"

    allowed_domains = "ccee.org.br"
    def start_requests(self):

        urls = ["https://www.ccee.org.br/portal/faces/pages_publico/o-que-fazemos/como_ccee_atua/precos/deck_de_precos?_afrLoop=325477022574389&_adf.ctrl-state=6dywfo3d4_62#!%40%40%3F_afrLoop%3D325477022574389%26_adf.ctrl-state%3D6dywfo3d4_66"]
        
        for url in urls:
            yield scrapy.Request(url, self.parse)
    
def parse(self, response):
    loader = ItemLoader(CceeCrawlItem())
    urls = ["https://www.ccee.org.br/ccee/documentos/DC%d%s" % INFOS,
            "https://www.ccee.org.br/ccee/documentos/NW%d%s" % INFOS]
    for url in urls:
        loader.add_value("file_urls", url)
        yield loader.load_item()