from icrawler.builtin import GreedyImageCrawler

storage = {'root_dir': '/Users/hugh/Documents/data/infant_iter3/'}

greedy_crawler = GreedyImageCrawler(storage=storage)
greedy_crawler.crawl(domains='https://pixabay.com/zh/images/search/baby/', 
                     )

# from icrawler.builtin import FlickrImageCrawler

# flickr_crawler = FlickrImageCrawler('4dbdf12c7146a085ea29ee2e8766f342',
#                                     storage={'root_dir': '/Users/hugh/Documents/data/infant_iter/'})
# flickr_crawler.crawl(tags='baby')