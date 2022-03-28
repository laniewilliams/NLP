from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words
'''
print(words)

print(blob.tags)

print(blob.noun_phrases)

print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)

for i in sentences:
    print(i)
    print(round(i.sentiment.polarity,3))


from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

sentences = blob.sentences

print(blob.sentiment)

for i in sentences:
    print(i.sentiment)

spanish = blob.translate(to='es')
print(spanish)

chinese = blob.translate(to='zh')
print(chinese)

french = blob.translate(to='fr')
print(french)

nep = blob.translate(to='ne')
print(nep)

english = nep.translate()
print(english)

'''
from textblob import Word

index = Word('index')
cacti = Word('cacti')

print(index.pluralize())

print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#Spellcheck and corrections
word = Word('theyr')

print(word.spellcheck()) #returns the cofidence level of what they were trying to say

print(word.correct()) #picks the word with the higher confidence level

#Stemming and Lemmatization
word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())


#print(word1.lemmatize())
#print(word2.lemmatize())

happy = Word('happy')

#print(happy.definitions)
#print(happy.synsets)