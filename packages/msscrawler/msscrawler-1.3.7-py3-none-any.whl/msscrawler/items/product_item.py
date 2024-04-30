import scrapy

from .base import BaseItem


class ProductItem(BaseItem):
    product_id = scrapy.Field()
    competitor = scrapy.Field()
    good_nm = scrapy.Field()
    normal_price = scrapy.Field()
    sale_price = scrapy.Field()
    shipping_price = scrapy.Field()
    shipping_type = scrapy.Field()
    shipping_condition = scrapy.Field()
    options = scrapy.Field()
    total_options = scrapy.Field()
    currency = scrapy.Field()
    category_id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    wish_count = scrapy.Field()
    review_count = scrapy.Field()
    promotion_price = scrapy.Field()
    outdate = scrapy.Field()
    platform_category_name = scrapy.Field()
    platform_category_url = scrapy.Field()
    platform_category_breadcrumb = scrapy.Field()
    platform_category_id = scrapy.Field()
