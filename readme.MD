# sitemap_python
A Python utility for building sitemaps.

## Usage

### Generate sitemap

```
import datetime
import sitemap.generator as generator

sitemap = generator.Sitemap()
sitemap.add("http://www.example.com",
            lastmod=datetime.datetime.now(),
            changefreq="monthly",
            priority="1.0")
sitemap_xml = sitemap.generate()


sitemap_index = generator.Sitemap(type='sitemapindex')
sitemap_index.add("http://www.example.com/sitemap01.xml",
                  lastmod=datetime.datetime.now(),
sitemap_index_xml = sitemap_index.generate()
```


### Ping search engine
Currently support ping Google and Bing with sitemap urls.

```
import sitemap.ping as ping

ping.ping("google", "http://www.example.com/sitemap.xml")
ping.ping_urls("bing", ["http://www.example.com/sitemap.xml"])
```

### Push url to Baidu
Push urls directly to Baidu. Related document available [at here](http://zhanzhang.baidu.com/college/courseinfo?id=267&page=2#h2_article_title14).

```
import sitemap.baidu as baidu
bp = baidu.BaiduPush("http://www.example.com", "<YOUR_KEY>")
bp.add("http://www.example.com/example.html")
bp.flush()
```

### Verify the spider ip address
__sitemap.spider__ can be use to verify whether the ip address of spider is genius.

Example:

```
from sitemap.spider import get_verified_spider_name

# spider_name will be None if no search engine is matched
spider_name = get_verified_spider_name("66.249.65.219")
```

The method __get\_verified\_spider\_name__ has uses _socket.gethostbyaddr_, which may be slow in some cases. So make __guess\_spider\_name\_from\_ua__ method may filter out several results via User-Agent.

```
from sitemap.spider import get_verified_spider_name, guess_spider_name_from_ua

spider_name = guess_spider_name_from_ua(spider_ua)
if spider_name:
    spider_name = get_verified_spider_name(spider_ip)
```