# coding: utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        """
        抓取所有符合规则的url
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item'))
        for link in links:
            newurl = link['href']
            newurlfull = urlparse.urljoin(page_url, newurl)
            new_urls.add(newurlfull)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {'page_url': page_url}
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', attrs={'class': "lemma-summary", 'label-module': 'lemmaSummary'})  # 修改成字典的写法
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data


