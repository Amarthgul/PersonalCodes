'''
Use to trace the nationality of artists on deviantArt
May not be available as the URL pattern of deviant art has changed 
'''


import urllib.request
import matplotlib.pyplot as plt
import numpy as np


def download(targeturl, numRetries = 2, user_agent = 'WHATEVER'):
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(targeturl, headers = headers)
    print('Downloading:', targeturl)  
    try:
        html = urllib.request.urlopen(targeturl).read()
    except urllib.request.URLError as err:
        print('Error!', err)
        html = None
        if numRetries:
            if hasattr(err, 'code') and 500 <= err.code < 600:
                return DownloadPage(targeturl, numRetries - 1)
    return html
    
    
def mlpPainterSta(tarURL = r'https://mlp-vectorclub.deviantart.com/', \
    readFromFile = True, writeFile = False):

    if not readFromFile:
        mvcHTML = download(tarURL)
        mvcHTML = mvcHTML.decode('utf-8').encode('cp850','replace').decode('cp850')
        if writeFile:
            with open('mvcHTML.txt', 'a') as file:
                file.write(mvcHTML)
    else:
        with open('mvcHTML.txt', 'r') as file:
            mvcHTML = file.read()

    artistList = re.findall(r'"https://(\w*).deviantart.com/"', mvcHTML)
    artistList = list(set(artistList))
    removeList = ['www', 'forum', 'welcome', 'help', 'about']
    for _ in removeList:
        if _ in artistList:
            artistList.remove(_)

    artistsURL = []
    for _ in artistList:
        artistsURL.append('https://' + _ + '.deviantart.com/')
    print(artistsURL)

    countries = []
    for _ in artistsURL:
        try:
            country = artCountry(_)[0]
            if len(str(country)) >= 2:
                countries.append(country)
        except: pass

    drawPlot(countries)
    if writeFile:
        with open('countrySta.txt', 'a') as file:
            for _ in countries:
                file.write(_); file.write('\n')


if __name__ == '__main__':
    mlpPainterSta(r'https://mlp-vectorclub.deviantart.com/modals/memberlist/')
    
    
