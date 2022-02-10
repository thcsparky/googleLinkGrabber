import os
from urllib import request
import requests
import json 
startpos = 0
urlsTotal = []
def main():
    term = input('Search term: \n').rstrip()
    startpos = 0
    z = recursiveGrab(term)
    if not z:
        print('No more links located upon search execution.')
    try:
        for x in z:
            print(x)
    except Exception:
        print(Exception)


    
def grablinks(term, startpos):
    ##returns a list of links on the page
    urlsTotal2 = []
    url = "https://google.com/search?q=" + term + '&start=' + str(startpos)
    resp = requests.get(url)
    txt = ''
    if resp.ok:
        txt = resp.text
    else:
        print('Error gathering')
        quit()

    if len(txt) > 0:
        urls = txt.split('url?q=')
        for x in urls:
            url2 = x.split('&amp')[0]
            if url2.startswith('https') and url2.find('google.') == -1:
                if url2 not in urlsTotal:
                    print(url2)
                    urlsTotal.append(url2)

                urlsTotal2.append(url2)
        return(urlsTotal2)
    

def recursiveGrab(term):
    global startpos 
    global urlsTotal
    
    a = grablinks(term, startpos)
    if len(a) > 0:
        for x in a:
            if x not in urlsTotal:
                urlsTotal.append(x)

        startpos += 10
        recursiveGrab(term)
    else:
        return(urlsTotal)



    

if __name__ == '__main__':
    main()