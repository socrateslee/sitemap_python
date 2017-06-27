'''
A toolkit for baidu url push.
Document:
http://zhanzhang.baidu.com/college/courseinfo?id=267&page=2#h2_article_title14
'''
import sys
import json
import urllib2
import six

API_BASE = "http://data.zz.baidu.com/urls?site=%s&token=%s"


class BaiduPush(object):
    def __init__(self, domain, key, chunk_size=100):
        '''
        chunk_size: int, threshold of number of urls
                    triggering a api request.
        '''
        self._api = API_BASE % (domain, key)
        self._chunk_size = chunk_size
        self._urls = []
        self._last_result = None

    def add(self, urls):
        if isinstance(urls, basestring):
            if urls not in self._urls:
                self._urls.append(urls)
        else:
            self._urls.extend(filter(lambda x: x not in self._urls, urls))
        if len(self._urls) >= self._chunk_size:
            self.flush()

    def flush(self):
        urls = '\n'.join(self._urls)
        if isinstance(urls, six.text_type):
            urls = urls.encode('utf-8')
        self._urls = []
        req = urllib2.Request(url=self._api, data=urls,
                              headers={'Content-Type': 'text/plain'})
        resp = urllib2.urlopen(req, timeout=60)
        self._last_result = json.loads(resp.read())

    def __del__(self):
        if self._urls:
            self.flush()

    def get_result(self):
        return self._last_result


if __name__ == '__main__':
    if len(sys.argv) > 3:
        bp = BaiduPush(sys.argv[1], sys.argv[2])
        bp.add(sys.argv[3:])
        bp.flush()
        print bp.get_result()

