import scrapy


class AgentSpiderSpider(scrapy.Spider):
    name = "agent_spider"
    allowed_domains = ["www.bhhsamb.com"]
    start_urls = ["https://www.bhhsamb.com/roster/Agents"]

    def parse(self, response):
        pass
