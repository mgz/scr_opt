from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class OptlistRu(BasePortiaSpider):
    name = "optlist.ru"
    allowed_domains = [u'optlist.ru']
    start_urls = [u'https://optlist.ru/suppliers#/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.container-btm-space > div:nth-child(2) > .card__content > .row',
                [
                    Field(
                        u'img',
                        '.col-sm-4 > .image-pop > .img-responsive::attr(src)',
                        []),
                    Field(
                        u'title',
                        '.col-sm-8 > .h2 *::text',
                        []),
                    Field(
                        u'price',
                        '.col-sm-8 > p:nth-child(3) > strong *::text',
                        []),
                    Field(
                        u'description',
                        '.col-sm-8 > p:nth-child(6) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'body',
                [
                    Field(
                        u'logo',
                        'div:nth-child(4) > .header-box > .header-box--overlay > .row > .layout-main__col-content > .header-box__content > .media > .media-left > .header-box__logo > a > .media-object::attr(src)',
                        []),
                    Field(
                        u'title',
                        'div:nth-child(4) > .header-box > .header-box--overlay > .row > .layout-main__col-content > .header-box__content > .media > .media-body > .header-box__title *::text',
                        []),
                    Field(
                        u'website',
                        'div:nth-child(4) > .header-box > .header-box--overlay > .row > .layout-main__col-content > .header-box__content > .media > .media-body > .header-box__subtext > .named-list__content > a::attr(href)',
                        []),
                    Field(
                        u'about',
                        'div:nth-child(5) > .row > .layout-main__col-content > div:nth-child(1) > .card__content > .expander > p *::text',
                        [])])]]
