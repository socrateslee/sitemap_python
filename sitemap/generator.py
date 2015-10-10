import urllib
import datetime

URLSET_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</urlset>'''

SITEMAPINDEX_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
%s
</sitemapindex>'''


def datetime_to_isoformat(d):
    if isinstance(d, datetime.datetime):
        return datetime.datetime(*d.timetuple()[:6]).isoformat()
    elif isinstance(d, datetime.date):
        return datetime.date(*d.timetuple()[:3]).isoformat()
    else:
        return None


class Sitemap(object):
    def __init__(self, type="xml"):
        self._type = type
        self.urls = []

    def add(self, loc, **kw):
        item = {'loc': loc,
                'lastmod': kw.get('lastmod'),
                'changefreq': kw.get('changefreq'),
                'priority': kw.get('priority')}
        if isinstance(item['lastmod'], (datetime.date, datetime.datetime)):
            item['lastmod'] = datetime_to_isoformat(item['lastmod'])
        self.urls.append(item)

    def reset(self):
        self.urls = []

    def _generate_xml(self):
        XML_FIELDS = ['loc', 'lastmod', 'changefreq', 'priority']
        ret = []
        for item in self.urls:
            url = ['<url>']
            for field in XML_FIELDS:
                if item[field]:
                    url.append('<%s>%s</%s>'\
                               % (field, item[field], field))
            url.append('</url>')
            ret.append('\n'.join(url))
        return URLSET_TEMPLATE % ('\n'.join(ret))

    def _generate_text(self):
        return '\n'.join(map(lambda x: x['loc'], self.urls))

    def _generate_sitemapindex(self):
        XML_FIELDS = ['loc', 'lastmod']
        ret = []
        for item in self.urls:
            url = ['<sitemap>']
            for field in XML_FIELDS:
                if item[field]:
                    url.append('<%s>%s</%s>'\
                               % (field, item[field], field))
            url.append('</sitemap>')
            ret.append('\n'.join(url))
        return SITEMAPINDEX_TEMPLATE % ('\n'.join(ret))

    def generate(self):
        if self._type == 'xml':
            return self._generate_xml()
        elif self._type == 'text':
            return self._generate_text()
        elif self._type == 'sitemapindex':
            return self._generate_sitemapindex()
        else:
            raise Exception("Unsupported sitemap type %s." % self._type)
