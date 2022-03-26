import TTScraperB as scraper
import ConcatFiles as concatenator 
import VidInfoGen as info 
from time import time

EMAIL = []
PASSWORD = []


def concatProcess(fname, cond):
    concatenator.resizeAll(directory='/Users/teoscomputer/src/python/Scrapy/TikTokScraper/', ffmpeg_location='/Users/teoscomputer/bin/ffmpeg', waste_dir='/Users/teoscomputer/Desktop/PyTrash/', reconcatDir='/Users/teoscomputer/Desktop/ReConcReady/', o_cond=cond)
    
    concatenator.concatenate(file_name=fname, directory='/Users/teoscomputer/Desktop/ReConcReady/', ffmpeg='/Users/teoscomputer/bin/ffmpeg', outDir='/Users/teoscomputer/Desktop/ConcatenatedFiles/')    

    
def scrapeProcess(scrapeList, vidsPerProf):
    vNum = 0
    for prof in scrapeList:
        for vidNum in range(vidsPerProf):
            vNum += 1
            scraper.profScrape(prof, 1363, 172, 'old', vNum, vidNum+1)

            
def uploadProcess(email=EMAIL[0], password=PASSWORD[0], file='foodOutput.mp4', title=info.title('Food')
                  , description=info.description('Food', EMAIL[0]), promotion=False, public=True):
    import YoutubeUploader as uploader
    uploader.logIn('https://studio.youtube.com/channel/UC-Vpcs3DXBBB2fJn80Jq-8A', email, password)
    uploader.upload(file, title, description, promotion, public)

    
    
def food():
    scrapeList = ['beautylicious', 'tastemade', 'inchinesefood', 'becky1381', 'tastebud', 'tasty'
                  , 'soyummy', 'joyoffood', 'vishalthakor63155', 'tinykitchentm', 'foodporn'
                  , 'foodielab', 'melinasfood']

    premiumList = []#Better accounts list for more scrapes from these

    scrapeProcess(scrapeList, 2)

    concatProcess('foodOutput.mp4', 'food')
    
    
def satisfying():
    scrapeList = ['sosatisfying', 'amosmunteanu', 'relax1ngggg', 'vishalthakor63155'
                  , 'talisatossell', 'insider', '_powervision_']

    premiumList = []#Better accounts list for more scrapes from these

    scrapeProcess(scrapeList, 5)

    concatProcess('satisfyingOutput.mp4', 'satisfying')    
    
    
    
def memes():
    scrapeList = [ 'pubity', 'seemore', 'ladbible', 'kalesalad', 'zenci'
                  , 'ponciklendin', 'bred', 'lesspressure', 'majesticgrime']

    premiumList = []#Better accounts list for more scrapes from these

    scrapeProcess(scrapeList, 4)

    concatProcess('memesOutput.mp4', 'meme')    
    
    
    
def popular():
    scrapeList = ['addisonre', 'dameliofamilyofficial', 'thehypehouse', 'itstaylerholder', 'jamescharles'
                  , 'savv.labrant', 'sofiedossi', 'brentrivera', 'charlidamelio', 'lorengray'
                  , 'leaelui', 'lilhuddy', 'zachking', 'babyariel']

    premiumList = []#Better accounts list for more scrapes from these

    scrapeProcess(scrapeList, 3)

    concatProcess('popularOutput.mp4', 'popular')    
    
    
    
def crafts():
    scrapeList = ['thecrafty', 'tricklife', '5.crafty.minutes', 'lesspressure'
                  , 'melinasfood', 'etfunnychannel', 'smartlifestyle01']

    premiumList = []#Better accounts list for more scrapes from these

    scrapeProcess(scrapeList, 4)

    concatProcess('craftsOutput.mp4', 'crafts')
    

    
def tag(tag):
    for vidNum in range(35):
        scraper.tagScrape(tag, 1363, 172, 'old', vidNum+1)

    concatProcess('tagOutput.mp4')
    
    
def music(song):
    for vidNum in range(35):
        scraper.musicScrape(song, 1363, 172, 'old', vidNum+1)
        
    concatProcess('musicOutput.mp4', 'music')
    
    
def trendng():
    for vidNum in range(35):
        scraper.trendingScrape(1363, 172, 'old', vidNum+1)
    
    concatProcess('trendingOutput.mp4', 'trending')
