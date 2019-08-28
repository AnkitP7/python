from bs4 import BeautifulSoup
import requests

"""
Author : Ankit Patel
Scraper class that parses through pages and fetches links
"""

class Scraper:
    def __init__(self, parser, url, page=1):
        self.parser = parser
        self.url = url
        self.page = page


    def scrape(self):
        if self.parser:
            html_links = {}
            for pages in range(0,page):
                temp_url  = url + "ics/advisories?page={}".format(pages)
                print("Fetching data from following url {}".format(temp_url))
                html_data = requests.get(temp_url)
                bs = BeautifulSoup(html_data.text,self.parser)
                main_content = bs.find_all("div",class_="view-content")
                links = main_content[0].find_all("a")
                for link in links:
                    html_links[link.get("href")] = link.get_text()
                
                print("Fetched the following links",html_links.items())
                for link,name in html_links.items():
                    article_link = self.url + link
                    self.fetch_link_content(article_link)

    
    def fetch_link_content(self, link):
        if link:
            link_content = requests.get(link)
            bs = BeautifulSoup(link_content.text, self.parser)
            main_content = bs.find_all("div",id="ncas-content")
            header_content = main_content[0].find_all("h2")
            main_header_content = main_content[0].find_all("p")
            print(header_content[0].get_text())
            print(main_header_content[0].get_text())
            #Export data or do something
            
                

    
if __name__ == "__main__":
    soup = "html.parser"
    url = "https://www.us-cert.gov/"
    page = 1                                   #Change the page according to your preference
    scrapy = Scraper(soup, url, page)
    scrapy.scrape()    
