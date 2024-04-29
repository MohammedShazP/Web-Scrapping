import scrapy
from scrapy_splash import SplashRequest
from .. items import AgentsItem


class AgentSpiderSpider(scrapy.Spider):
    name = "agent_spider"
    start_urls = ["https://www.bhhsamb.com/roster/Agents"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse,
                                args={'wait': 5}
                                )

    def parse(self, response):
        agents = self.parse_agents(response)

        for agent in agents:
            yield agent


    def parse_agents(self,response):
        agent_urls =  response.xpath("//a[contains(@class, 'cms-int-roster-card-image-container') and contains(@class, 'site-roster-card-image-link')]/@href")
        for agent_url in agent_urls:
            yield response.follow(agent_url.get(),callback=self.parse_details)

    def parse_details(self,response):
        items = AgentsItem()
        details = response.xpath("//article[contains(@class, 'rng-agent-profile-main')]")
        for detail in details:
            Name = detail.xpath("//p[contains(@class,'rng-agent-profile-contact-name')]/text()").get().strip(),
            Job_Title = detail.xpath("//span[contains(@class,'rng-agent-profile-contact-title')]/text()").get().strip(),
            Image_url = detail.xpath("//img[contains(@class, 'rng-agent-profile-photo')]/@src").get(),
            Address = detail.xpath("//li[contains(@class,'rng-agent-profile-contact-address')]/strong/text()").get().strip(),
            Contact_Number = detail.xpath("//li[contains(@class,'rng-agent-profile-contact-phone')]/a/text()").get().strip(),
            Social = {"facebook": detail.xpath("//li[contains(@class, 'rng-agent-profile-contact-social')]//ul[contains(@class, 'rng-agent-profile-contact')]//li[contains(@class, 'social-facebook')]//a/@href").get(),
                               "Instagram": detail.xpath("//li[contains(@class, 'rng-agent-profile-contact-social')]//ul[contains(@class, 'rng-agent-profile-contact')]//li[contains(@class, 'social-instagram')]//a/@href").get()}

            items["Name"] = Name
            items["Job_Title"] = Job_Title
            items["Image_url"] = Image_url
            items["Address"] = Address
            items["Contact_Number"] = Contact_Number
            items["Social"] = Social

            yield items

