---
title: "Visualizing country's export using python and d3.js"
excerpt: "Find out which countries are increasingly tied to another country's economic performance."
excerpt_separator: "<!--more-->"
image:
    teaser: 2016-06-15-countries-export-visualized-using-d3js/teaser.jpg
categories:
  - Projects
---
So this project came up because I was wondering that for certain countries, how vulnerables are their economies to the change of their export partners.

For example, Australia exports **a lot** of [raw materials and other resources to China](http://www.austrade.gov.au/news/economic-analysis/australias-export-performance-in-2014-15). If somehow one day the Chinese economy implodes, Australian economy will be dragged down regardless of how well they are doing in other area.

If you just want to look at the beautiful, finished result, [the interactive demo is here]({{site.url}}/images/2016-06-15-countries-export-visualized-using-d3js/sankey_chart.html).

What it looks like:
![Sankey Result]({{site.url}}/images/2016-06-15-countries-export-visualized-using-d3js/sankey_result.png)

Below are the steps to get the data and setup the chart.

So, there are 2 keys things we need to do here.

1. find the export amount in USD -- per country/per year dataset.
2. find a nice chart that is able to illustrate the export dependency.

For the first part, it's quite easy. 

Through google search I found a dataset hosted by MIT. (the site also have nice tables and graphs online). You can find it [here](http://atlas.media.mit.edu/en/resources/data/).

Specifically, we want the one called *"Product Trade between Origin and Destination Country by Year (4 digit depth, bilateral)"*. Even zipped it's still a 200MB download. whew.

Let's get started by importing data and setup dataframe.

we will use the latest years data (2014) only.


```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import math
```


```python
# Original Source: 
# http://atlas.media.mit.edu/en/resources/data/
# HS6 REV. 2007 (2008 - 2014)
# Product Trade between Origin and Destination Country by Year (4 digit depth, bilateral)

pathname = 'year_origin_destination_hs07_4.tsv.bz2'
iter_csv = pd.read_csv(pathname, iterator=True, chunksize=10**5,
                          compression='bz2',delimiter='\t',
                           low_memory=False,error_bad_lines=False)
df = pd.concat([chunk[chunk['year'] == 2014] for chunk in iter_csv])
df = df.drop(['year'],axis=1)
df = df.fillna(0)
```



I also imported product name mapping dataset, but it didn't get used at this time.


```python
# Original Source: 
# http://atlas.media.mit.edu/en/resources/data/
# HS6 REV. 2007 (2008 - 2014)
# Product Trade by Year and Country (4 digit depth)

pathname2 = 'products_hs_07.tsv.bz2'
pf = pd.read_csv(pathname2, compression='bz2',delimiter='\t',
                           low_memory=False)
```

Another thing I want to know is the country's export GDP compared to its total GDP of each country. 

So even if one such country relies on only sigle country trading partner, if their domestic GDP is a much larger share of total GDP, then they won't be impacted much from the trading partner's economy downturn.

Below is the datasource for export vs total GDP per country. It is from [the world bank](http://data.worldbank.org/indicator/NE.EXP.GNFS.ZS).


```python
# Original Source: 
# http://data.worldbank.org/indicator/NE.EXP.GNFS.ZS
# Download >> CSV

pathname3 = 'export_pct_en_csv_v2.csv'
cf = pd.read_csv(pathname3,low_memory=False,skiprows=3)
cf = cf[['Country Name','Country Code','2014']]
cf = cf.fillna(0)
cf.columns = ['name','code','pct_gdp']
cf['code'] = cf['code'].apply(str.lower)
cf.loc[cf['name'] == 'World','code'] = 'zzz'
cf.loc[cf['name'] == 'World','name'] = 'Other Countries'
```

Just to see what the data looks like:

+ **df** dataframe contains the export and import transaction per origin and destination country. 
+ **cf** dataframe contains the export gdp and total gdp per country.

the hs07 is the product code (For example, 302 = Fish, fresh or chilled, excluding fish fillets

But we will do for overall, not by product at this time.


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>origin</th>
      <th>dest</th>
      <th>hs07</th>
      <th>export_val</th>
      <th>import_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>66768</th>
      <td>ago</td>
      <td>ben</td>
      <td>302</td>
      <td>6303518.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>66769</th>
      <td>ago</td>
      <td>ben</td>
      <td>3923</td>
      <td>285788.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>66770</th>
      <td>ago</td>
      <td>bfa</td>
      <td>2710</td>
      <td>0.00</td>
      <td>70894.0</td>
    </tr>
    <tr>
      <th>66771</th>
      <td>ago</td>
      <td>bfa</td>
      <td>7010</td>
      <td>1141049.06</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>66772</th>
      <td>ago</td>
      <td>bfa</td>
      <td>8704</td>
      <td>2936.00</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cf.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>pct_gdp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aruba</td>
      <td>abw</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Andorra</td>
      <td>and</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>afg</td>
      <td>6.634452</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Angola</td>
      <td>ago</td>
      <td>47.712942</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albania</td>
      <td>alb</td>
      <td>28.107365</td>
    </tr>
  </tbody>
</table>
</div>




```python
pf[pf.hs07 == 302]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>hs07</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>104</th>
      <td>10302</td>
      <td>302</td>
      <td>Fish, fresh or chilled, excluding fish fillets...</td>
    </tr>
  </tbody>
</table>
</div>



...

Generally, we want to see all the countries that have the large enough export volume to affect the world trade. 

let's see from the data, choose the ones with greather 500 Bil USD export in 2014:


```python
df_grouped = df.groupby(['origin']).sum()
df_grouped = df_grouped.reset_index()
df_grouped = df_grouped.drop(['import_val','hs07'],axis=1)

df_grouped[df_grouped.export_val > 500*10**9]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>origin</th>
      <th>export_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>38</th>
      <td>chn</td>
      <td>2.359386e+12</td>
    </tr>
    <tr>
      <th>54</th>
      <td>deu</td>
      <td>1.416808e+12</td>
    </tr>
    <tr>
      <th>69</th>
      <td>fra</td>
      <td>5.705236e+11</td>
    </tr>
    <tr>
      <th>99</th>
      <td>ita</td>
      <td>5.117265e+11</td>
    </tr>
    <tr>
      <th>102</th>
      <td>jpn</td>
      <td>7.004950e+11</td>
    </tr>
    <tr>
      <th>109</th>
      <td>kor</td>
      <td>5.874087e+11</td>
    </tr>
    <tr>
      <th>146</th>
      <td>nld</td>
      <td>5.301053e+11</td>
    </tr>
    <tr>
      <th>206</th>
      <td>usa</td>
      <td>1.447396e+12</td>
    </tr>
  </tbody>
</table>
</div>



For the countries of interest. I selected the ones I will consider moving to work or settle there longterm. 

The countries are Australia, New Zealand, Canada, USA, Germany, UK, Ireland, Japan, China, Singapore, Thailand, and zzz = The rest of the world.



```python
selected_countries = ['aus','nzl','can','usa','deu','gbr','irl','jpn','chn','sgp','tha','zzz']

cf = cf[cf.code.isin(selected_countries)]
cf = cf.set_index(cf['code'])
```

Let's do some cleaning up for the **df** dataframe.

+ Remap the rest of the countries to 'zzz'.
+ Get rid of product code and sum all the export amount together.
+ Normalize the export amount to fraction (**frac**) of total country GDP.


```python
df_simple = df.copy()
df_simple.loc[~df.origin.isin(selected_countries),'origin'] = 'zzz'
df_simple.loc[~df.dest.isin(selected_countries),'dest'] = 'zzz'
df_simple = df_simple.groupby(['origin','dest']).sum()
df_simple = df_simple.reset_index()
df_simple = df_simple.drop(['import_val','hs07'],axis=1)

df_simple_origin = df_simple.groupby(['origin']).sum()
df_simple_origin = df_simple_origin.reset_index()
df_simple_origin.rename(columns = {'export_val':'origin_total'},inplace=True)

df_simple = pd.merge(df_simple,df_simple_origin,on='origin')
df_simple['frac'] = df_simple['export_val'] / df_simple['origin_total']

df_simple.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>origin</th>
      <th>dest</th>
      <th>export_val</th>
      <th>origin_total</th>
      <th>frac</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aus</td>
      <td>can</td>
      <td>1.386333e+09</td>
      <td>2.458750e+11</td>
      <td>0.005638</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aus</td>
      <td>chn</td>
      <td>8.370677e+10</td>
      <td>2.458750e+11</td>
      <td>0.340444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>aus</td>
      <td>deu</td>
      <td>2.223841e+09</td>
      <td>2.458750e+11</td>
      <td>0.009045</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aus</td>
      <td>gbr</td>
      <td>3.243383e+09</td>
      <td>2.458750e+11</td>
      <td>0.013191</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aus</td>
      <td>irl</td>
      <td>8.594606e+07</td>
      <td>2.458750e+11</td>
      <td>0.000350</td>
    </tr>
  </tbody>
</table>
</div>



And we come to the final part of data preparation. Save it into an appropriate Format. The json string should look like this:

```javascript
{
"nodes":[
{"name":"Australia (20.9% of GDP)"},
{"name":"New Zealand (28.0% of GDP)"}],
"links":[
{"source":0,"target":14,"value":0.56},
{"source":0,"target":20,"value":34.04}]
}
```

And here is the processing code for json:


```python
json_string = '{\n'
node = '"nodes":[\n'

#spawn 2 sets of countries code
n_countries = len(selected_countries)
for i in np.arange(0,n_countries):
    ts = '{"name":"' + cf['name'].loc[selected_countries[i]] + ' (' + str(round(cf['pct_gdp'].loc[selected_countries[i]],1))  + '% of GDP)"},\n'
    node = node + ts
for i in np.arange(0,n_countries):
    ts = '{"name":"'+ cf['name'].loc[selected_countries[i]] +'"}'
    if (i < n_countries-1): ts = ts + ',\n'
    node = node + ts
node = node + ']'

json_string = json_string + node + ',\n'

link = '"links":[\n'
for i in np.arange(0,df_simple.shape[0]):
    ts = '{"source":'+ str(selected_countries.index(df_simple['origin'][i])) +','
    ts = ts + '"target":'+ str(selected_countries.index(df_simple['dest'][i])+n_countries) +','
    ts = ts + '"value":'+ str(round(df_simple['frac'][i]*100,2)) +'}'
    if (i < df_simple.shape[0]-1): ts = ts + ',\n'
    link = link + ts
link = link + ']'

json_string = json_string + link + '\n}'

#save to file
f = open("countries_export.json","w")
f.write(json_string)
f.close()
```

Now, we come to the 2nd part ... selecting the graph.

As mentioned before. It is not easy to find an appropriate chart to plot this data. However, after searching and looking around for an hour or so, I stumpled upon the 2 most interest graphs called **Circos** and **Sankey**.

[**Circos**](http://circos.ca/) is a circular layout chart which explore the size and relationship of objects in the circumference. As seen here:
![Circos chart example]({{site.url}}/images/2016-06-15-countries-export-visualized-using-d3js/drex_chord___circos_custom_2.png)

However, after trying out the Circos, I found that it couldn't give a *normalized* representation for each country due to the nature of the link-relationship. So in the end I chose [**Sankey**](https://en.wikipedia.org/wiki/Sankey_diagram). 

As we have seen before. Sankey is a digram that shows the *flow* of quantities from one object to another. This is perfect to visualize the export flow of countries.  

![Circos chart example]({{site.url}}/images/2016-06-15-countries-export-visualized-using-d3js/sankey_example.png)

There are a few implementations of sankey already on the net -- [Google has one](https://developers.google.com/chart/interactive/docs/gallery/sankey), and [many on github](https://github.com/search?&q=sankey).

In the end I used the [original D3.js version from Mike Bostock](https://bost.ocks.org/mike/sankey/). Mostly because  I wanted to learn how d3.js works. 

And the result is as you see it! Thank you for reading!
