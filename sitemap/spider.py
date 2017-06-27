'''
A toolkit for verifying the ip address of search engine spiders.
'''
import socket

HOST_NAME_MAP = {
    'baidu': ('.baidu.com', '.baidu.jp'),
    'sogou': '.crawl.sogou.com',
    'google': ('.googlebot.com', '.google.com'),
    'bing': '.search.msn.com',
    'yandex': ('.yandex.com', '.yandex.ru', '.yandex.net'),
    'ahrefs': '.ahrefs.com',
    'yahoo': '.yahoo.net',
}

UA_MAP = {
    'baidu': 'baiduspider',
    'sogou': 'sogou web spider',
    'google': 'googlebot',
    'bing': 'bingbot',
    'yandex': 'yandexbot',
    'ahrefs': 'ahrefsbot',
    'shenma': 'yisouspider',
    '360': '360spider',
    'yahoo': 'yahoo! slurp',
    'ddg': 'duckduckbot',
}

DUCKDUCKGO = ['72.94.249.34',
              '72.94.249.35',
              '72.94.249.36',
              '72.94.249.37',
              '72.94.249.38']


def get_verified_spider_name(ip, spider_name=None):
    '''
    Return verified spider name based on ip address.
    '''
    # check for duckduckgo
    if ip in DUCKDUCKGO:
        return 'ddg'
    hostnames = []
    try:
        (hostname, aliaslist, __) = socket.gethostbyaddr(ip)
        hostnames.append(hostname)
        hostnames.extend(aliaslist)
    except Exception as e:
        pass
    if not hostnames:
        return None
    for k, v in HOST_NAME_MAP.items():
        if spider_name and spider_name != k:
            continue
        for hostname in hostnames:
            if hostname.endswith(v):
                return k
    return None


def guess_spider_name_from_ua(ua):
    '''
    Guess spider name from browser user agent string.
    '''
    ua = (ua or '').lower()
    for k, v in UA_MAP.items():
        if v in ua:
            return k
    return None
