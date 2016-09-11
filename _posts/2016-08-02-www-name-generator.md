---
title: "A random website-name generator, based on Stack Exchange forum dataset"
excerpt: "How to come up with non-sensical but memorable names using text mining and natural language processing (NLP)."
excerpt_separator: "<!--more-->"
image:
    teaser: 2016-08-02-www-name-generator/teaser.jpg
categories:
  - Projects
---
After deciding that I should own a personal website, the first thing I did (and probably anyone else) was to think about the naming -- What should I call it? The name should sound nice and be memorable.

Since my goal for this website is to write about all things related to data science, data analytics, data mining, and statistics, etc... it should be an interesting idea to find the name based on text dataset.

I forum dataset I chose was a Q&A forum called [**"Cross Validated"**](http://stats.stackexchange.com/), dedicated to answering any statistics or data science related questions. It has been around a long time so we should have many posts to analyze.

The dataset can be found at [archive.org](https://archive.org/details/stackexchange). The main file [(stats.stackexchange.com.7z)](https://archive.org/download/stackexchange/stats.stackexchange.com.7z) is around 180MB zipped and contains various information of the forum such as posts, comments, users, and votes. The data are captured from 2014 up to Jun 2016, so around 2.5 years.

I decided to use posts file **("crossvalidated.posts.xml")** as our base data.

Let's import all the libaries and files:


```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

import math
import random as rd

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
from collections import Counter
```

Here I use *lxml* to extract xml-type data into the **df** Dataframe.


```python
# Original Source:
# https://archive.org/details/stackexchange
# https://archive.org/download/stackexchange/datascience.stackexchange.com.7z
# https://archive.org/download/stackexchange/stats.stackexchange.com.7z
# stackexchange discussion forum dataset -- for 'data science' and 'cross validated' sub-section

from lxml import objectify

path = 'crossvalidated.posts.xml'
xml = objectify.parse(open(path))
attribs = [dict(r.attrib) for r in xml.getroot().getchildren()]
df = pd.DataFrame.from_records(attribs)
```

Let's have a glimpse at the dataset.
It contains roughly 160,000 posts with 21 columns (or features), the main text is in the "Body" column.


```python
# the data looks like this.
print df.shape
df.head(3).T
```

    (163205, 21)





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AcceptedAnswerId</th>
      <td>15</td>
      <td>59</td>
      <td>5</td>
    </tr>
    <tr>
      <th>AnswerCount</th>
      <td>5</td>
      <td>7</td>
      <td>19</td>
    </tr>
    <tr>
      <th>Body</th>
      <td>&lt;p&gt;How should I elicit prior distributions fro...</td>
      <td>&lt;p&gt;In many different statistical methods there...</td>
      <td>&lt;p&gt;What are some valuable Statistical Analysis...</td>
    </tr>
    <tr>
      <th>ClosedDate</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>CommentCount</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>CommunityOwnedDate</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010-07-19T19:13:28.577</td>
    </tr>
    <tr>
      <th>CreationDate</th>
      <td>2010-07-19T19:12:12.510</td>
      <td>2010-07-19T19:12:57.157</td>
      <td>2010-07-19T19:13:28.577</td>
    </tr>
    <tr>
      <th>FavoriteCount</th>
      <td>20</td>
      <td>10</td>
      <td>39</td>
    </tr>
    <tr>
      <th>Id</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>LastActivityDate</th>
      <td>2010-09-15T21:08:26.077</td>
      <td>2012-11-12T09:21:54.993</td>
      <td>2013-05-27T14:48:36.927</td>
    </tr>
    <tr>
      <th>LastEditDate</th>
      <td>NaN</td>
      <td>2010-08-07T17:56:44.800</td>
      <td>2011-02-12T05:50:03.667</td>
    </tr>
    <tr>
      <th>LastEditorDisplayName</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>LastEditorUserId</th>
      <td>NaN</td>
      <td>88</td>
      <td>183</td>
    </tr>
    <tr>
      <th>OwnerDisplayName</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>OwnerUserId</th>
      <td>8</td>
      <td>24</td>
      <td>18</td>
    </tr>
    <tr>
      <th>ParentId</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>PostTypeId</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Score</th>
      <td>31</td>
      <td>27</td>
      <td>63</td>
    </tr>
    <tr>
      <th>Tags</th>
      <td>&lt;bayesian&gt;&lt;prior&gt;&lt;elicitation&gt;</td>
      <td>&lt;distributions&gt;&lt;normality&gt;</td>
      <td>&lt;software&gt;&lt;open-source&gt;</td>
    </tr>
    <tr>
      <th>Title</th>
      <td>Eliciting priors from experts</td>
      <td>What is normality?</td>
      <td>What are some valuable Statistical Analysis op...</td>
    </tr>
    <tr>
      <th>ViewCount</th>
      <td>1970</td>
      <td>17285</td>
      <td>5334</td>
    </tr>
  </tbody>
</table>
</div>



I think we have plenty of datapoints. In fact, it is a bit too many for my use.

I decided to cut down by extract the *"Body"* from just 2015 onwards (1.5 years), so that we also have more recent samples. we will have about 65,000 posts.

I joined all the post bodies together into one string variable called **raw**.


```python
print df.Body[df.CreationDate>='2015-01-01'].shape
# get from 2015-01-01 onwards, so that we get the most recent topics/words
raw = ' '.join(df[df.CreationDate>='2015-01-01']['Body'].values)
print 'raw excerpts - first 1000 characters'
print raw[:1000]
```

    (64820,)
    raw excerpts - first 1000 characters
    <p>The variance of the error term decreases (or, at worst, does not increase) when you add more regressors.
    The reason is that a new variable can explain some more variability in the data that wasn't explained by previous regressors. This will reduce the unexplained variations in the data, whch will cause the variance of the error term to decrease.</p>
     <p>Suppose $A$ is a very small subset of $\{0,\dots,n\}^3$ and I am trying to find an element of $A$. I first inspect maybe 50 random triples $(x_i,y_i,z_i), 1\le i\le 50$, and find that none of them are in $A$.</p>

    <p>Undeterred, I notice that the triple $(x_{17},y_{17},z_{17})$ (say) looks promising in some sense, and in particular it looks promising because of the presence of $x_{17}$ and $z_{17}$ (say).</p>

    <p>So I proceed to inspect triples of the form
    $$(x_{17},y,z_{17}),\quad y\in\{0,\dots,n\}.$$
    After trying maybe 8 different randomly chosen $y$-values I finally find an element of $A$.</p>

    <p>Question:</p>

    <blockquote>
      <p>


As expected, this is a raw HTML text. We need to clean this.

My favorite tool , RegEx.



```python
import string

re1 = re.compile('<[^>]*>>') # remove html tags
re2 = re.compile('[0-9]+') # remove numbers
re3 = re.compile('\t|\n') # remove newlines
regex = re.compile('[%s]' % re.escape(string.punctuation)) # remove punctuations
raw = re3.sub(' ',re2.sub(' ',re1.sub(' ',raw)))
raw_clean = regex.sub(' ',raw)
```


```python
print raw_clean[:1000]
```

    The variance of the error term decreases  or  at worst  does not increase  when you add more regressors The reason is that a new variable can explain some more variability in the data that wasn t explained by previous regressors  This will reduce the unexplained variations in the data  whch will cause the variance of the error term to decrease  Suppose  A  is a very small subset of      dots n     and I am trying to find an element of  A   I first inspect maybe  random triples   x i y i z i    le i le    and find that none of them are in  A  Undeterred  I notice that the triple   x    y    z       say  looks promising in some sense  and in particular it looks promising because of the presence of  x     and  z      say  So I proceed to inspect triples of the form   x    y z      quad y in    dots n     After trying maybe  different randomly chosen  y  values I finally find an element of  A  Question  blockquote   This method seems to make sense in practice  but how do I put it into cont


Now that we have properly spaced dataset, we can tokenize the words. I will use [*NLTK*](http://www.nltk.org/) (natural language toolkit) library here. It is a fantastic library for text analysis, but from what I read on the web, the performance is a bit slow and they take some time to add cutting-edge algorithms.

Nevertheless, I'm not an advanced user yet so I don't care.


```python
tokens = word_tokenize(raw_clean.lower())
```

Here we are going to remove all the common words ( 'to', 'a', 'the', .. ) in English and also the one-character only tokens.


```python
from nltk.corpus import stopwords
stop = stopwords.words('english')
#remove the stopwords and one-character tokens
tokens = [w for w in tokens if ((w not in stop) and (len(w)>1))]

```

Let's see the result, 10 most common words in the dataset:


```python
print 'most common tokens'
count = Counter(tokens)
count.most_common(10)
```

    most common tokens





    [(u'data', 58301),
     (u'model', 46831),
     (u'would', 35819),
     (u'one', 31463),
     (u'lt', 29956),
     (u'use', 26962),
     (u'using', 25861),
     (u'test', 24249),
     (u'distribution', 23077),
     (u'two', 22069)]



Not surprising, in the top 10 we see 'data' , 'model' , and 'distribution'.

Next, I feel that the processing time is a bit slow, so let's down-sample the tokens from 5.5 Mil to 200K word count only. We will also remove the too-short (2 characters) or too-long (10+ charactoers) of a word.

Then see the most common ones again:


```python
# down-sampling to 200k words
print 'number of tokens: ',len(tokens)
sampled_tokens = []
for i in range(0,2*10**5):
    w = tokens[rd.randint(0,len(tokens)-1)]
    while (len(w)<3 or len(w)>10): # get short, simple words
        w = tokens[rd.randint(0,len(tokens)-1)]
    sampled_tokens.append(w)

print 'number of sampled tokens: ',len(sampled_tokens)
count_sampled = Counter(sampled_tokens)
count_sampled.most_common(10)
```

    number of tokens:  5524393
    number of sampled tokens:  200000





    [(u'data', 2479),
     (u'model', 2039),
     (u'would', 1550),
     (u'one', 1418),
     (u'use', 1190),
     (u'using', 1116),
     (u'test', 1038),
     (u'variables', 992),
     (u'codepre', 974),
     (u'two', 953)]



To help us do further analysis, we can tag the word as different grammar-type: pronouns, adjectives, etc.

The default *pos_tag()* function is unbearably slow, we are going to do manual looping ourselves.


```python
# nltk.help.upenn_tagset()
# using pos_tag() is cumbersome and incredibly slow, so we just use the tagger itself
from nltk.tag.perceptron import PerceptronTagger
from nltk.tag import map_tag
tagger = PerceptronTagger()
%time tagged = tagger.tag(sampled_tokens)
#%time tagged = [tagger.tag(w) for w in sampled_tokens]
%time tagged = [(word,map_tag('en-ptb', 'universal',pos)) for (word,pos) in tagged]
```

    CPU times: user 30.6 s, sys: 595 ms, total: 31.2 s
    Wall time: 30.9 s
    CPU times: user 605 ms, sys: 70.7 ms, total: 676 ms
    Wall time: 630 ms


Done, let's see the result:


```python
print 'a glimpse of simplified tags'
print tagged[0:10]
```

    a glimpse of simplified tags
    [(u'change', u'NOUN'), (u'estimate', u'NOUN'), (u'codepre', u'NOUN'), (u'none', u'NOUN'), (u'trees', u'NOUN'), (u'differences', u'NOUN'), (u'option', u'NOUN'), (u'want', u'VERB'), (u'information', u'NOUN'), (u'cell', u'NOUN')]


What is the frequency for each tag?

We can plot a nice graph. About 50% of the words are nouns, 25% are verbs, and 20% are adjectives.


```python
fd_tag = nltk.FreqDist(tag for (word, tag) in tagged)
fd_tag.tabulate()
fd_tag.plot(cumulative=True)
```

     NOUN  VERB   ADJ   ADV   ADP   NUM   DET     X  CONJ  PRON   PRT
    93850 44929 41640 11539  3802  2906   530   330   197   174   103



![png]({{site.url}}/images/2016-08-02-www-name-generator/output_11_1.png)


And now we can try to generate a randomized set of names and phrases.
First we try ADJ + NOUN, 6 to 13 letters.


```python
lnoun = [w for (w,t) in tagged if (t == 'NOUN')]
ladj = [w for (w,t) in tagged if (t == 'ADJ')]
ladv = [w for (w,t) in tagged if (t == 'ADV')]
lverb = [w for (w,t) in tagged if (t == 'VERB')]
```


```python
# let's do a random sampling of ADJ + NOUN. maybe a good idea for website
# keep the whole phrase short -- 6 to 13 letters. Ideally 8.
i = 0
while i<12:
    phrase =  rd.choice(ladj) + rd.choice(lnoun)
    if(len(phrase)>=6 and len(phrase)<=13):
        print i+1, phrase
        i = i + 1
```

    1 gammatextfai
    2 singledata
    3 mutualthank
    4 contextbsc
    5 nulllithe
    6 addfishers
    7 highend
    8 similarphase
    9 symmetricnote
    10 numerictime
    11 stanway
    12 possiblewrap


Then ADV + ADJ:


```python
# howabout ADV + ADJ
i = 0
while i<12:
    phrase = rd.choice(ladv) + rd.choice(ladj)
    if(len(phrase)>=6 and len(phrase)<=13):
        print i+1, phrase
        i = i + 1
```

    1 spsschange
    2 ageqtileiid
    3 sometimesnet
    4 quitegeneral
    5 roughlytoy
    6 providedont
    7 howeverpapera
    8 probablynew
    9 farwhole
    10 alonesimilar
    11 samplenew
    12 addfinite


Another combination... VERB + NOUN


```python
# say... VERB + NOUN
i = 0
while i<12:
    phrase = rd.choice(lverb) + rd.choice(lnoun)
    if(len(phrase)>=6 and len(phrase)<=13):
        print i+1, phrase
        i = i + 1
```

    1 mildvalues
    2 formulatesize
    3 followssis
    4 wouldidentify
    5 xijmodel
    6 seemservice
    7 takenmethod
    8 guessrequire
    9 usingakstrong
    10 pairedparts
    11 getsize
    12 pvaluesmethod


Try generating longer names:


```python
# VERB + NOUN + NOUN. seems too long
i = 0
while i<12:
    w1 = rd.choice(ladv)
    w2 = rd.choice(ladj)
    w3 = rd.choice(lnoun)
    phrase =  w1 + w2 + w3
    if(len(phrase)>=6 and len(phrase)<=15):
        print i+1, phrase
        i = i + 1
```

    1 evenrelatedtell
    2 welllowstate
    3 yjtdontmodel
    4 alsolargeknock
    5 farwincreosote
    6 amnildlldlshelp
    7 errorlargemodel
    8 wellfalsecfirm
    9 directlylequse
    10 firstwrongrbm
    11 possiblystepetr
    12 yetrightclass


I played with it for a while and came up with something like below.

Forcing both first and second words to start with the same first letter. This makes the phrase more catchy.


```python
# (ADV or ADJ or NOUN) + (VERB or NOUN). And both words have the same first letter!
i = 0
while i<12:
    w1 = rd.choice([rd.choice(ladv),rd.choice(ladj),rd.choice(lnoun)])
    w2 = rd.choice([rd.choice(lverb),rd.choice(lnoun)])
    phrase =  w1 + w2
    if(len(phrase)>=6 and len(phrase)<=13 and w1[0] == w2[0] and w1 != w2):
        print i+1, phrase
        i = i + 1
```

    1 termstraining
    2 secondset
    3 alreadyarrp
    4 perfectlyputs
    5 countcant
    6 modelmultiple
    7 randomreading
    8 powerpaper
    9 statsvm
    10 easyestimate
    11 rightrandom
    12 mondaymatrix


After running that repeatedly for quite a few times, here are the generated names that make sense (to human) and could be used:

> rarelyrandom, properlyplot, oddoutcome, fitfeatures, barelybiased, binarybunch, mostlyanalog, thereforetest, alsoassumed, methodmissing, leastlinear, reportreality, returnrandom, explainerror, ratherright, gaussianguess, ideaincluded.

In the end, I picked *"Rarely Random"* because it's ironic. The name actually came from mostly random process. (with a few defined rules per above)

Yeah, that, and also my girlfriend likes it the most.

Thank you for reading!
