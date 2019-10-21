# -*- coding: utf-8 -*
from icrawler.builtin import GreedyImageCrawler

storage = {'root_dir': '/Users/hugh/Documents/data/animal/goat'}


# greedy_crawler = GreedyImageCrawler(storage=storage)
# greedy_crawler.crawl(domains='https://www.google.com.hk/search?safe=strict&hl=zh-CN&tbs=simg:CAESrwIJVxx0JVKN9JcaowILEKjU2AQaBggXCD0IGAwLELCMpwgaYgpgCAMSKLMP2BnXGdQZsg_1OGbgPnA_1SGdYZmS3KPPkrmC2WOqIylTryJfQl4isaMN-r6E8eQtDV0U6KmoGe2ihhkf8oW25xxEZZlDpJ-5GHtPNKOOda3Ma8VCPROprQWiAEDAsQjq7-CBoKCggIARIEFjQWsAwLEJ3twQkajAEKFgoEYmFiedqliPYDCgoIL20vMGpudnAKGgoHdG9kZGxlctqliPYDCwoJL20vMDFiZ3N3CiQKEG51ZGUgcGhvdG9ncmFwaHnapYj2AwwKCi9tLzAzY3IwdGcKFgoDYm952qWI9gMLCgkvbS8wMWJsN3YKGAoGZGlhcGVy2qWI9gMKCggvbS8wZjU3MQw&q=baby&tbm=isch&sa=X&ved=2ahUKEwisj_Kknp3lAhUFIIgKHQUABxgQsw56BAgAEAE&biw=1920&bih=969', 
#                      max_num=1000)

# from icrawler.builtin import FlickrImageCrawler

# flickr_crawler = FlickrImageCrawler('4dbdf12c7146a085ea29ee2e8766f342',
#                                     storage={'root_dir': '/Users/hugh/Documents/data/infant_iter/'})
# flickr_crawler.crawl(tags='baby')
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(feeder_threads=1, parser_threads=1, downloader_threads=4, storage=storage)
filters = dict(color='pink')
google_crawler.crawl(keyword='goat', filters=None, offset=0, max_num=100, min_size=(200, 200), max_size=None, file_idx_offset=0)

# bing_clawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': '/Users/hugh/Documents/data/body_painting/biying/'})

# bing_clawler.crawl(keyword='人体彩绘', filters=None, offset=0, max_num=10000)

# baidu_clawler = BaiduImageCrawler(downloader_threads=4, storage={'root_dir': '/Users/hugh/Documents/data/body_painting/baidu/'})
# baidu_clawler.crawl(keyword='人体彩绘', filters=None, offset=0, max_num=10000)


# import urllib
# import sys
# import chardet
# import re
 
 
# def get_html(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     # typeEncode = sys.getfilesystemencoding()
#     # infoencode = chardet.detect(content).get('encoding','utf-8')
#     # html = content.decode(infoencode,'ignore').encode(typeEncode)
#     return html   
 
# def get_img(html):
#     # reg = r'src="(.*?)"' 
#     # re.search('src="([^"]+)"',text) 
#     reg = r'src="([^"]+)"'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html) #表达式中只有一个括号时，findall只会返回括号的内容
#     i = 0
#     for imgurl in imglist:
#         print imgurl
#         urllib.urlretrieve(imgurl, '/Users/hugh/Documents/data/anime/%s.jpg'%i)
#         i+=1
        
# html = get_html('https://www.google.com.hk/search?safe=strict&sa=G&hl=zh-CN&tbs=simg:CAESoQIJKd--yRwo74galQILEKjU2AQaAgg9DAsQsIynCBpiCmAIAxIo4wPACaMJ3ALaAuQD4gOrCbUJ4QPuK_105jSyWLO0r1iOaMc4j7yvwKxowi8xB9zi8uEjo0cKq7qaDZSRZ9q4MC1_1zSTnwZmvh5I6SNqd4zo6hc5vwzUyqa5UsIAQMCxCOrv4IGgoKCAgBEgT3q_15eDAsQne3BCRqCAQoWCgVhbmltZdqliPYDCQoHL20vMGp4eQoZCgdjYXJ0b29u2qWI9gMKCggvbS8wMjE1bgobCghoaW1lIGN1dNqliPYDCwoJL20vMGdkd2t5ChcKBGdpcmzapYj2AwsKCS9tLzA1cjY1NQoXCgVtYW5nYdqliPYDCgoIL20vMDRzcG0M&q=anime&tbm=isch&ved=2ahUKEwiC9ZOWw5PlAhXMGKYKHVQfDycQsw56BAgBEAE&biw=1280&bih=689#imgrc=_')
# print html
# get_img(html)


# import re
# import urllib
 
# url = "https://www.google.com.hk/search?safe=strict&sa=G&hl=zh-CN&tbs=simg:CAESoQIJKd--yRwo74galQILEKjU2AQaAgg9DAsQsIynCBpiCmAIAxIo4wPACaMJ3ALaAuQD4gOrCbUJ4QPuK_105jSyWLO0r1iOaMc4j7yvwKxowi8xB9zi8uEjo0cKq7qaDZSRZ9q4MC1_1zSTnwZmvh5I6SNqd4zo6hc5vwzUyqa5UsIAQMCxCOrv4IGgoKCAgBEgT3q_15eDAsQne3BCRqCAQoWCgVhbmltZdqliPYDCQoHL20vMGp4eQoZCgdjYXJ0b29u2qWI9gMKCggvbS8wMjE1bgobCghoaW1lIGN1dNqliPYDCwoJL20vMGdkd2t5ChcKBGdpcmzapYj2AwsKCS9tLzA1cjY1NQoXCgVtYW5nYdqliPYDCgoIL20vMDRzcG0M&q=anime&tbm=isch&ved=2ahUKEwiC9ZOWw5PlAhXMGKYKHVQfDycQsw56BAgBEAE&biw=1280&bih=689"
# content = urllib.urlopen(url).read()
# urls = re.findall(r"<a.*?href=.*?<\/a>", content, re.I)
# for url in urls:
#     print unicode(url,'utf-8')
    
# link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", content)
# for url in link_list:  
#     print url 

