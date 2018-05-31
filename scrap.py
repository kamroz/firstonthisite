import urllib.request

def scraphtml (url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return html.decode('utf-8')


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def allerrand(baseurl):
    errand = str('<a href="/zlecenie/')
    print("przed!")
    html = scraphtml(baseurl)
    print("po!")
    #wypisz na ekran pozycję pierwszej litery z łańcucha znaków ze zmiennej `errand`
    #print(html.find(errand))

    errandlist = list(find_all(html, errand))
    szukaj = ".html"

    for x in errandlist:
        znakmniejszosci = x
        backslash = (znakmniejszosci + errand.__len__())
        pieceofhtml = html[backslash:backslash+200]
        endofurl = pieceofhtml.find(szukaj)

        #od pozycji `backslash` do pozycji znaku cudzyslowie `"`
        positionofend = endofurl + szukaj.__len__()
        print("http://favore.pl/zlecenie/" + html[backslash :(backslash+pozycjakoncaurla)])
