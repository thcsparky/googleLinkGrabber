import os
import requests
import json 
startpos = 0
urlsTotal = ''
def main():
    global startpos 
    global urlsTotal 
    a = input('what to search for?\n').rstrip()
    url = 'https://google.com/search?q='
    urlsgot = []
    txt = ''
    if startpos == 0:
        urlgrab = url + a
        txtGet = requests.get(urlgrab)
        if txtGet.ok:
            txt = txtGet.text
        else:
            print("Error Retrieving data.")
            main()
        ##will continue from this point because else recycles main
        url1 = txt.split('url?q=')
        for x in url1:
            url2 = x.split('&amp')[0]
            if url2.startswith('https'):
                urlsgot.append(url2)
        
        for x in urlsgot:
            print(x)
        startpos += 10
        #doesn't have to recycle to main yet because the next step is right below
    
    if startpos > 0:
        urlgrab = url + a + '&start=' + str(startpos)
        resp = requests.get(urlgrab)
        if resp.ok:
            txt = resp.text 
        if txt.find('url?q=') == -1:
            print('Last page reached.')

            quit()
        else:
            url1 = txt.split('url?q=')
            for x in url1:
                url2 = x.split('&amp')[0]
                if url2.startswith('https'):
                    urlsgot.append(url2)

            for x in urlsgot:
                print(x)
            startpos += 10

    

if __name__ == '__main__':
    main()