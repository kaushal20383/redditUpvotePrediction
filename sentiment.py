#from wordcloud import STOPWORDS
from textblob import TextBlob
import string
import re
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)


stopwords = set(STOPWORDS)
punctuation = string.punctuation + '\n'
def clean_text(text: str):
    # Punctuations removal
    text = "".join([word.lower() for word in 
                    text if word not in punctuation])
    tokens = re.split(' ', text)
    
    # Stopwords removal
    tokens = re.split(' ', text)
    text = [word for word in tokens if word not in stopwords]
    text = " ".join(text)
    return text

def cal_polarity(text: str):
    text = clean_text(text)
    return TextBlob(text).sentiment.polarity
