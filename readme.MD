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
Currently support ping Google and Bing.

```
import sitemap.ping as ping

ping.ping("google", "http://www.example.com/sitemap.xml")
ping.ping_urls("bing", ["http://www.example.com/sitemap.xml")
```

### Push url to Baidu
Related document available [at here](http://zhanzhang.baidu.com/college/courseinfo?id=267&page=2#h2_article_title14).

```
import sitemap.baidu as baidu
bp = baidu.BaiduPush("http://www.example.com", "<YOUR_KEY>")
bp.add("http://www.example.com/example.html")
bp.flush()
```
