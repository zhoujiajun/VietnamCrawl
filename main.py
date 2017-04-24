from vietnam_crawler import manager, downloader, parser, output

class CrawlMain(object):
    def __init__(self):
        self.urls = manager.UrlManager()
        self.downloader = downloader.HtmlDownloader()
        self.parser = parser.HtmlParser()
        self.output = output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 如果有待爬取的url，就取出来
            try:
                new_url = self.urls.get_new_url()  # 从里面取出一个url

                print('craw %d:%s' % (count, new_url))
                html_content = self.downloader.download(new_url)  # 获取下载的页面内容
                back_data = self.parser.parse(new_url, html_content)  # 进行解析，获取新的url和数据

                if type(back_data) is dict:
                    self.output.collect_data(back_data)  # 收集数据
                elif type(back_data) is set:
                    self.urls.add_new_urls(back_data)  # 把这些新的url放回待访问区

                # count = count + 1
                if count == 100:
                    break
                count = count + 1
            except:
                print('craw failed')

        self.output.output_html()


if __name__ == "__main__":
    #root_url = "http://zh.vietnamplus.vn/"
    # root_urls = [""]
    root_urls = ["", "culture.vnp", "sports.vnp", "politics.vnp", "technology.vnp", "social.vnp", "world.vnp",
                 "business.vnp", "Travel.vnp", "environment.vnp"]
    obj_spider = CrawlMain()
    for root_url in root_urls:
        obj_spider.craw("http://zh.vietnamplus.vn/"+ root_url)
