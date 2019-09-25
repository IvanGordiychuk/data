import requests
import json 
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
nltk.download('punkt')
nltk.download('stopwords')
response = requests.get('https://newsapi.org/v2/everything?q=russia&from=2019-08-25&to=2019-09-25&language=en&contry=US&apiKey=KEY')
jsonText = json.loads(response.text)
text=""
for obj in jsonText['articles']:
	text+=str(obj['content']).lower()

stopWords = set(stopwords.words('english')) 
wordTokens = word_tokenize(text)
filteredText = [word for word in wordTokens if not word in stopWords and word.isalpha() and word != 'chars'] 

dataFrequencies = {}

for word in filteredText:
    dataFrequencies[word] = dataFrequencies.get(word, 0) + 1 
  
dataFrequencies50 = dict(sorted(dataFrequencies.items(), key=lambda f:-f[1])[:50])

wordCloud = WordCloud(width=900,height=500, max_words=50, background_color="white", relative_scaling=1,normalize_plurals=False).generate_from_frequencies(dataFrequencies50)

plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()


