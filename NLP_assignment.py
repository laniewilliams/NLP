from nyc_trends import nyc_trends
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
from wordcloud import WordCloud
import imageio

print('---------------------------------------PART 1 ---------------------------------------------')
trend_dict = nyc_trends[0]
blob = trend_dict['trends']
tweet_volume = []
tweet_name = []
stops = [None]
for i in blob:
  tweet_volume.append(i['tweet_volume'])
  tweet_name.append(i['name'])



items = list(zip(tweet_name,tweet_volume))
items = [i for i in items if i[1] not in stops]

print(items)


from operator import itemgetter
sorted_items = sorted(items,key=itemgetter(1),reverse=True)
top10 = sorted_items[:10]
print(top10)



df = pd.DataFrame(top10,columns=["Trends","Volume"])


import matplotlib.pyplot as plt

df.plot.bar(x="Trends",y="Volume",legend=False)
plt.gcf().tight_layout()

plt.show()




print('---------------------------------------PART 2 ---------------------------------------------')
items =[i for i in items if i[1]>20000]
items_dict = dict(items)




wordcloud = WordCloud(colormap="prism",background_color="white")

wordcloud = wordcloud.generate_from_frequencies(items_dict)

wordcloud = wordcloud.to_file("Trends.png")

plt.imshow(wordcloud)
plt.show()
print("done")
