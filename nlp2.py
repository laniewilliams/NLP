from textblob import TextBlob
import nltk
from pathlib import Path
#import pandas as pd

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

cleanwords = [i for i in items if i[0] not in stops]
print(cleanwords)