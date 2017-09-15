# coding: utf-8


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取
        self.old_urls = set()  # 已爬取

    def add_new_url(self, url):
        """
        向管理器中添加新的url
        :param root_url:
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        向管理器中添加批量的url
        :param new_urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        """
        判断管理器中是否有新的待爬取的url
        :return:
        """
        return len(self.new_urls) != 0  # return里可以写判断，返回True或者false

    def get_new_url(self):
        """
        从管理器中获取一个新的url
        :return:
        """
        new_url = self.new_urls.pop()  # pop方法会把url拿出来，注意是拿出
        self.old_urls.add(new_url)
        return new_url
