# coding: utf-8


import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 爬虫调度程序

        cout = 1  # 统计爬取次数
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "now craw job : {0} url : {1}".format(cout, new_url)
                html_cont = self.downloader.download(new_url)  # 下载新url
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析新的url
                self.urls.add_new_urls(new_urls)  # 添加批量url
                self.outputer.collect_data(new_data)
                if cout == 1000:
                    break
                cout += 1
            except Exception as e:
                print "craw failed!!\n {0}".format(e)

        self.outputer.output_html()  # 输出html


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
