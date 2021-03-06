import matplotlib.pyplot as plt
import urllib.request
import pandas as pd
import numpy as np
import timeit
import pickle
import time
import sys
import re

def pickleOpearte(save = True, fileName = 'default.pckl', varToSave = None):
    if save:
        with open(fileName, 'wb') as f:
            pickle.dump(varToSave, f)
    else:
        with open(fileName, 'rb') as f:
            return pickle.load(f)
    return True

def download(targetURL, numRetries = 2, userAgent = 'noOne'):
    headers = {'User-agent': userAgent}
    request = urllib.request.Request(targetURL, headers = headers)
    print('Downloading:', targetURL)  
    try:
        html = urllib.request.urlopen(targetURL).read()
    except urllib.request.URLError as err:
        print('Error! ', err)
        html = None
        if numRetries:
            if hasattr(err, 'code') and 500 <= err.code < 600:
                return download(targetURL, numRetries - 1)
    return html

def matchVotes(html):
    favourites = r'.+title="Favourites">(\d+)</span>.+'
    upvotes    = r'.+title="Upvotes">(\d+)</span>.+'
    downvotes  = r'.+title="Downvotes">(\d+)</span>.+'
    comments   = r'.+<span class="comments_count" data-image-id="\d+">(\d+)</span>.+'
    tagName    = r'data-tag-slug="(\w+)"' 
    result = {}

    for pattern, name in zip([favourites, upvotes, downvotes, comments, tagName],
                   ["favourites", "upvotes", "downvotes", "comments", "tagName"]):
        result[name] = re.findall(pattern, html)
    for name in ["favourites", "upvotes", "downvotes", "comments"]:
        try:
            result[name] = int(result[name][0])
        except:
            result[name] = 0

    return result  

def runCase(readSampleFile = False, recordThreshold = 50,
            start = 1, stop = 458670, step = 15):
    tagPopularity = {}
    ''' DateStructure example:
    {
    safe: {
        "favourites": 2345,
        "upvotes": 6345,
        "downvotes": 653,
        "comments": 3623},
    solo: {
        "favourites": 45362,
        "upvotes": 23423,
        "downvotes": 23452,
        "comments": 23423},
    ...
    }
    '''

    iterateRecorder = 0
    for dbIndex in range(start, stop, step): #iterate through 0-17000
        if readSampleFile:
            with open('derpi.txt', 'r') as f:
                html = f.read()
                print('read')

        currentURL = r"https://derpibooru.org/"+str(dbIndex)
        print("currently dealing with: ", currentURL)
        html = download(currentURL, numRetries = 1)
        html = str(html).encode(sys.stdout.encoding, errors='replace')
        html = str(html) #how ugly
        print('Successfully encoded. ')

        currentDict = matchVotes(html)
        for oneOfTheTagName in currentDict['tagName']:
            if oneOfTheTagName not in tagPopularity:
                tagPopularity[oneOfTheTagName] = {"favourites": 0,
                "upvotes":0, "downvotes":0, "comments":0}
            for name in ["favourites", "upvotes", "downvotes", "comments"]:
                tagPopularity[oneOfTheTagName][name] += currentDict[name]
    
        iterateRecorder += 1
        if iterateRecorder >= recordThreshold:
            iterateRecorder = 0
            pickleOpearte(save = True, fileName = 'tagPopularity.pckl', 
                          varToSave = pd.DataFrame(tagPopularity))
        
        time.sleep(0.5); # https://derpibooru.org/robots.txt Crawl-delay: 0.5

    # code repetition :C
    pickleOpearte(save = True, fileName = 'tagPopularity.pckl', 
                  varToSave = pd.DataFrame(tagPopularity))
    pickleOpearte(save = True, fileName = 'tagPopularityBackup.pckl', 
                  varToSave = pd.DataFrame(tagPopularity))

    print('All Finished')
    return tagPopularity

def visualization(targetVote = 'upvotes', topLimit = 15,
                  showPlot = False, savePlotName = 'default.svg', 
                  wipeOffList = [], stackedPlot = False):
    '''targetVote: "favourites", "upvotes", "downvotes", "comments"
topLimit: up to which to stop
    '''
    tagPopularityOrigin = pickleOpearte(save = False, fileName = 'tagPopularity.pckl')
    tagPopularity = pd.DataFrame(tagPopularityOrigin)
    
    currentVote = tagPopularity.loc[targetVote].sort_values(ascending = False)[:topLimit]
    
    currentVote = currentVote.iloc[::-1] # largest on top
    fontSize = 15
    if showPlot:
        plt.style.use(u'ggplot')
        plt.title('2012 -2013 Popularity by ' + targetVote.capitalize(), 
                  fontsize = fontSize * 1.5, y = 1.02, color='dimgrey')
        ax = currentVote.fillna(currentVote).astype(currentVote.dtypes).plot.barh(
            color = 'violet', fontsize = fontSize, alpha = 0.9)
        plt.xlim(0, 770000)
        for i, num in zip(ax.patches, range(len(ax.patches))):
            ax.text(i.get_width()+100, i.get_y() + 0.165, str(currentVote[num]), 
                    fontsize = fontSize, color='dimgrey')
        plt.show()


    names = list(currentVote.index)
    for name, index in zip(names, range(len(names))):
        print("{}{}{}{}".format(name, "^", index + 1, " || "), end = "")
        
    if stackedPlot:
        sortedTagPopu = np.sqrt(tagPopularity.copy().T)
        sortedTagPopu = sortedTagPopu.sort_values(by = "upvotes", ascending = False)
        sortedTagPopu = sortedTagPopu[:topLimit].iloc[::-1]
        
        plt.style.use(u'ggplot')
        ax = sortedTagPopu.fillna(sortedTagPopu).astype(sortedTagPopu.dtypes).plot.barh(
            fontsize = fontSize, alpha = 0.9)
        plt.title("General Overview (Rooted, Sort By Upvotes)", fontsize = fontSize * 1.5, y = 1.02, color='dimgrey')
        plt.show()

    return True;

def test():
    #html = download(r'https://derpibooru.org/1851779', numRetries = 1)
    targetURL = r'https://derpibooru.org/1851779'
    html = urllib.request.urlopen(targetURL).read()
    soup = BeautifulSoup(html, 'html.parser')
    soup = str(soup).encode(sys.stdout.encoding, errors='replace')
    print(soup)

'''==============================================='''
#====================================================
'''==============================================='''
def Main():  
    
    start = timeit.default_timer()
    #====================================================

    #runCase()
    visualization(targetVote = "favourites", showPlot = False, 
                topLimit = 20, stackedPlot = True)

    #====================================================
    end = timeit.default_timer(); print('Time costed:',end - start)

if __name__ == '__main__':
    Main()

'''
Documentation:
"favourites", "upvotes", "downvotes", "comments"

1st run at 16 Oct, 2018: 
    image index:      1400000  -  1858666
    image uploaded:  Mar 2017  -  Oct 2018
    image step:       15
    image total:      30577

1st run at 18 Oct, 2018: 
    image index:      1     -     458656
    image uploaded:  Jan 2012  -  Oct 2013
    image step:       15
    image total:      30577
'''
