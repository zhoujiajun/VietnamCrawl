
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open('output.html', 'w', encoding="utf8")

        fout.write("<html>")
        # fout.write("<head>")
        # fout.write("<meta charset='utf-8'>")
        # fout.write("</head>")
        #fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>')
        fout.write('<head><meta charset="utf-8"></head>')
        fout.write("<body>")

        fout.write("<table>")
#.encode('utf-8') 这个没用，因为本来爬取到的数据就没有乱码的
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['body'])
            fout.write("<td>%s</td>" % data['time'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()