from PIL import Image
from wordcloud import WordCloud,STOPWORDS
import numpy as np
import os

file = open("business_analytics_write_up.txt")
strings = file.read()
print (strings)
sw = set(STOPWORDS)
mask = np.array(Image.open("batman.png"))
wc = WordCloud(stopwords=sw,background_color="white",max_words=200,mask=mask)
wc.generate(strings)
wc.to_file("wordcloud.png")