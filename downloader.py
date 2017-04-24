import urllib.request
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        b = b'/:?='
        request = urllib.request.Request(urllib.request.quote(url, b))
        request.add_header('User-Agent', 'Mozilla/5.0')  # 提交http头信息
        response = urllib.request.urlopen(request)

        if response.getcode() != 200:
            return None
        return response.read()
