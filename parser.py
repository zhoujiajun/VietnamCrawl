from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        #zhPattern = re.compile(r"[\u4e00-\u9fa5]")
        #if zhPattern.search(page_url):
        if re.findall(r"[\u4e00-\u9fa5]+", page_url):
            if re.findall(r"region", page_url) or re.findall(r"topic", page_url):
                urls = self._get_new_urls(page_url, soup)
                back_data = urls
            else:
                news_detail = self._get_news_detail(page_url, soup)
                back_data = news_detail
        else:
            urls = self._get_new_urls(page_url, soup)
            back_data = urls
        return back_data

# 爬取url列表
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 匹配类型（正则表达式）：/view/数字.html,\d+表示数字

        # links = soup.find_all('a', href=re.compile(r"/[\u4e00-\u9fa5]+/\d+\.vnp"))  只能匹配中文
        # 这个能匹配中文、数字、英文的随机组合
        links = soup.find_all('a', href=re.compile(r"/\w+/\d+\.vnp"))
        for link in links:
            new_url = link['href']
            # 把新的url按照旧的url的格式拼接
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        page_links = soup.find_all('a', href=re.compile(r"/page\d+\.vnp"))
        for page_link in page_links:
            new_url = page_link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)

        return new_urls


    def _get_news_detail(self, page_url, soup):
        news_data = {}

        news_data['url'] = page_url

        title_node = soup.find("header", class_="article-header").find("h1")
        news_data['title'] = title_node.get_text()

        body_node = soup.find("div", class_="article-contents")
        news_data['body'] = body_node.get_text()

        body_node = soup.find("div", class_="time")
        news_data['time'] = body_node.get_text()

        return news_data

