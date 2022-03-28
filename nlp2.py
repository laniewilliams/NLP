from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

#nltk.download('stopwords') only need to run this once because the download is a one-time thing
from nltk.corpus import stopwords

stops = stopwords.words('english')

#print(stops)

blob = TextBlob('Today is a beautiful day.')
print(blob.words)

cleanlist = [word for word in blob.words if word not in stops] #takes out the stops words from the sentence
print(cleanlist)

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

#print(blob.word_counts["romeo"])

#print(blob.noun_phrases.count('lady capulet'))

#adding thee, thy, thou to the stops list
more_stops = ['thee','thy','thou']
stops += more_stops

items = blob.word_counts.items()
#print(items)

#use a list comprehension to eliminate any tuples
# contraining stop words:

items = [i for i in items if i[0] not in stops]
#print(cleanwords)
print(items[:10])

from operator import itemgetter
sorted_items = sorted(items)
print(sorted_items[:10]) #this just does a default sort

sorted_items = sorted(items,key=itemgetter(1),reverse=True) #we can use itemgetter to specify the key on which to sort and then do it in descending order
print(sorted_items[:10])

#creating a dataframe of the top 20 words
top20 = sorted_items[:20]

df = pd.DataFrame(top20,columns=["Words","Count"])
print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="Words",y="Count",legend=False)
plt.gcf().tight_layout()

plt.show()