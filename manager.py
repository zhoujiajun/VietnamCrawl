#两个列单，待爬和未爬
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

# 对于一个url，先判断是否爬过，或是否在未爬列单中（防止循环爬取），若都否，把其放在待爬列单中
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

# 添加多个url：先判断是否为空，否则循环查询每个url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

# 若new_urls不为0，证明还有url在待爬状态，返回true
    def has_new_url(self):
        return len(self.new_urls) != 0

# 从new_urls（待爬列单）里面获取第一个url，然后返回它，并加到old_urls(已爬列单)中
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url