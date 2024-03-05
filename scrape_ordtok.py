import httpx
from selectolax.parser import HTMLParser

def get_ordtok():
    stafir = ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","p","q","r","s","t","u","ú","v","w","x","y","ý","z","þ","æ","ö"]
    
    for stafi in stafir:
        url = f"https://tilvitnun.is/ordtok/{stafi}"
        resp = httpx.get(url)
        html = HTMLParser(resp.text)

        section = html.css('section#first-section')
        quotes = html.css('div.quote')

        with open("ordtok.txt", "a", encoding="utf-8") as f:
            for quote in quotes:
                f.write(quote.css_first('p').text() + "\n")
        

get_ordtok()