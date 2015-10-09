'''
Submit sitemap url to search engine.
'''
import sys
import urllib2

PING_MAP = {
    'google': 'http://www.google.com/webmasters/sitemaps/ping?sitemap=%s',
    'bing': 'http://www.bing.com/ping?sitemap=%s'
}


def ping(engine, url):
    base_url = PING_MAP.get(engine)
    if not base_url:
       print "Search engine %s not supported." % engine
       return
    url = base_url % url
    resp = urllib2.urlopen(url, timeout=60)
    return resp


def ping_urls(engine, urls):
    for url in urls:
        ping(engine, urls)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        ping_urls(sys.argv[1].lower(), sys.argv[2:])
