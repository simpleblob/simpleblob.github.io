---
title: "Web-scraping japanese text with python"
excerpt: "This is a short example on webscraping, specifically from Rakuten website."
excerpt_separator: "<!--more-->"
image:
    teaser: 2016-06-01-web-scraping-japanese-text/teaser.jpg
categories:
  - Projects
---
This is a short example on webscraping, specifically from Rakuten website (the Amazon equivalent for Japan)

This is their website: [www.rakuten.co.jp](http://www.rakuten.co.jp).

Here I will use the following python packages:

* requests - for piping http request can get the raw html response
* BeautifulSoup - for navigating the HTML mess and get the item we want
* re - regular expression library, handy for removing extra symbols and stuff
* jason - saving the result dataset to file

.. so let's import all of them.


```python
import requests
from bs4 import BeautifulSoup
import re
import json
```

Next, let's set up a keyword for product search. I choose TV.
and the no. of page result we want to scrape.


```python
keyword = 'テレビ' # = Television
no_of_page = 5
```

Here's the fun part!

First, let's try searching the rakuten website and decode their URL.

It turns out to be in the format like below, we can iterate the url to retrieve different page: 

> search.rakuten.co.jp /search/mall/**keyword**/?f=1&p=**page_no**&grp=product

Next, how to extract the name from the raw html text. Here's what it look like around the item name section. 

```html
<div class="rsrSResultItemTxt">
		<h2>
			<a href="http://item.rakuten.co.jp/townland-c/y-nhc-321b/">
				【送料無料】【NHC321B】32V型(32型/32インチ)　地デジLED液晶テレビ　ブルーライトガード搭載モデ...</a>
		</h2>
		<p class="copyTxt">
				【クレジットカード決済OK】【あす楽対応】ブルーライト抑制機能 地上デジタルチューナー搭載(省エネLEDバックライト)[延長保証]対象</p>
		<div class="step_double clfx">
```

Notice that the text we want is in the div("rsrSResultItemTxt") **>>** "h2" **>>** "a" section.

We can iterate the raw data using beautiful soup per below:


```python
url = ''
dict_item = {}
for i in range(1,no_of_page+1,1):
    #page by page
    url = 'http://search.rakuten.co.jp/search/mall/'+ keyword +'/?f=1&p='+str(i)+'&grp=product'
    r = requests.get(url)
    data = r.text
    
    #get name of the product for each group
    soup = BeautifulSoup(data,"lxml")
    for item in soup.find_all(class_='rsrSResultItemTxt'):
        shop_itemlink = item.h2.a.get("href").encode("utf-8")
        shop_itemheader = item.h2.a.get_text().encode("utf-8")
        dict_item[shop_itemlink] = shop_itemheader
```

Once finished, let's look at what is in the dict_item result:


```python
print 'no. of products =',len(dict_item)
print 'the first 3 keys and values:'
print dict_item.keys()[:3]
print dict_item.values()[:3]
```

    no. of products = 226
    the first 3 keys and values:
    ['http://item.rakuten.co.jp/htmr/m0500069/', 'http://item.rakuten.co.jp/jism/4548736022317-31-12406-n/', 'http://item.rakuten.co.jp/a-price/4974019857268/']
    ['\n\t\t\t\t\xe3\x80\x90\xe9\x80\x81\xe6\x96\x99\xe7\x84\xa1\xe6\x96\x99\xe3\x80\x91\xe3\x83\x86\xe3\x83\xac\xe3\x83\x93\xe5\x8f\xb0 \xe5\xa3\x81\xe5\xaf\x84\xe3\x81\x9b \xe5\xa3\x81\xe9\x9d\xa2 \xe3\x80\x90\xe3\x81\x82\xe3\x81\x99\xe6\xa5\xbd\xe5\xaf\xbe\xe5\xbf\x9c\xe3\x80\x91\xe3\x80\x8e\xe3\x83\x8f\xe3\x82\xa4\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x97\xe3\x83\xbb\xe8\x83\x8c\xe9\x9d\xa2\xe5\x8f\x8e\xe7\xb4\x8d\xe4\xbb\x98 \xe5\xa3\x81\xe3\x82\x88\xe3\x81\x9bTV\xe3\x82\xb9\xe3\x82\xbf\xe3\x83\xb3\xe3\x83\x89 \xe3\x80\x94...', '\n\t\t\t\tKJ-40W730C\xe3\x80\x90\xe7\xa8\x8e\xe8\xbe\xbc\xe3\x80\x91 \xe3\x82\xbd\xe3\x83\x8b\xe3\x83\xbc 40V\xe5\x9e\x8b\xe5\x9c\xb0\xe4\xb8\x8a\xe3\x83\xbbBS\xe3\x83\xbb110\xe5\xba\xa6CS\xe3\x83\x87\xe3\x82\xb8\xe3\x82\xbf\xe3\x83\xab\xe3\x83\x95\xe3\x83\xab\xe3\x83\x8f\xe3\x82\xa4\xe3\x83\x93\xe3\x82\xb8\xe3\x83\xa7\xe3\x83\xb3LED\xe6\xb6\xb2\xe6\x99\xb6\xe3\x83\x86\xe3\x83\xac\xe3\x83\x93 \xef\xbc\x88\xe5\x88\xa5\xe5\xa3\xb2...', '\n\t\t\t\t\xe3\x80\x90\xe9\x80\x81\xe6\x96\x99\xe7\x84\xa1\xe6\x96\x99\xe3\x80\x91SHARP LC-40H30 AQUOS(\xe3\x82\xa2\xe3\x82\xaf\xe3\x82\xaa\xe3\x82\xb9) [40V\xe5\x9e\x8b\xe5\x9c\xb0\xe4\xb8\x8a\xe3\x83\xbbBS\xe3\x83\xbb110\xe5\xba\xa6CS\xe3\x83\x87\xe3\x82\xb8\xe3\x82\xbf\xe3\x83\xab \xe3\x83\x95\xe3\x83\xab\xe3\x83\x8f\xe3\x82\xa4\xe3\x83\x93\xe3\x82\xb8\xe3\x83\xa7\xe3\x83\xb3L...']


We have collected 226 names out of 5 pages.

The keys look fine, but the values seem like they are still not displayed properly as UTF-8.

How about just the first value, print as string:


```python
print dict_item.values()[1]
```

    
    				KJ-40W730C【税込】 ソニー 40V型地上・BS・110度CSデジタルフルハイビジョンLED液晶テレビ （別売...


Seems fine. It is actually the problem with python version 2.7 -- the way it displays unicode output. Python version 3 apparently had this problem fixed.

The text still has new-line (\n) and tab (\t) characters. Let's remove them using RegEx:


```python
#remove newline, tab, and dots
RE_A = re.compile('\n|\t|\.')
for k, v in dict_item.iteritems():
    dict_item[k] = RE_A.sub('',v)
```

And here we should have a cleaned result:


```python
print dict_item.values()[1]
```

    KJ-40W730C【税込】 ソニー 40V型地上・BS・110度CSデジタルフルハイビジョンLED液晶テレビ （別売


Just to confirm that we are really using python version 2.7:


```python
import sys
print 'version =',sys.version
print 'encoding =',sys.stdout.encoding
```

    version = 2.7.12 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:43:17) 
    [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)]
    encoding = UTF-8


Let's try printing them one-by-one. Should look OK:


```python
for v in dict_item.values()[:5]:
    print v
```

    【送料無料】テレビ台 壁寄せ 壁面 【あす楽対応】『ハイタイプ・背面収納付 壁よせTVスタンド 〔
    KJ-40W730C【税込】 ソニー 40V型地上・BS・110度CSデジタルフルハイビジョンLED液晶テレビ （別売
    【送料無料】SHARP LC-40H30 AQUOS(アクオス) [40V型地上・BS・110度CSデジタル フルハイビジョンL
    【TVで放映】羽毛布団シングル限定！布団丸洗いクリーニング2枚！【送料無料　東北 北陸 関東 東海
    【在庫即納・送料無料！(沖縄、離島除く）】　VIERA TH-24D300 パナソニック 24V型デジタルハイビ


Looks good! And finally, we can save this dataset for future processing. 

Here's one way of doing that, using jason library:


```python
with open("item_desc_tv.json", 'w') as f:
    json.dump(dict_item, f)
```

And we should end this example here. Thank you for reading!
